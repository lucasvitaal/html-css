"""Motor de voz local: XTTS v2 clona uma voz a partir de 5 a 10 s de áudio de referência.

Uso direto:  python motor.py "texto em português" voz_modelo.wav saida.mp3
"""
import os
import re
import subprocess
import sys

import numpy as np
import soundfile as sf
import torch

os.environ.setdefault("COQUI_TOS_AGREED", "1")  # licença CPML da Coqui: uso pessoal, não comercial
from TTS.api import TTS

SR = 24000  # taxa de saída do XTTS v2
_xtts = None
_latentes = {}  # referências -> (gpt_cond_latent, speaker_embedding), calculado uma vez por voz


def xtts():
    """Carrega o modelo uma vez só, na GPU se houver."""
    global _xtts
    if _xtts is None:
        disp = "cuda" if torch.cuda.is_available() else "cpu"
        print("Carregando XTTS v2 em", disp, "(o primeiro uso baixa ~1,8 GB)")
        _xtts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(disp).synthesizer.tts_model
    return _xtts


def frases(texto):
    """Uma frase por vez: o XTTS erra em trechos longos e assim dá para pôr pausa de verdade.
    Quebra em pontuação seguida de espaço (então "40.000" fica inteiro) e em quebra de linha."""
    return [f.strip() for f in re.split(r"(?<=[.!?:;])\s+|\n+", texto.strip()) if f.strip()]


def gerar(texto, referencia, saida="saida.wav", pausa=0.45, velocidade=1.0, normalizar=True):
    """Gera `texto` com a voz de `referencia` e salva em .wav ou .mp3. Devolve o caminho.
    Com `normalizar`, números, unidades e siglas viram texto falado (narracao.py) e frases longas são quebradas."""
    if normalizar:
        from narracao import falar, frases as curtas
        texto = "\n".join(curtas(falar(texto)))
    m = xtts()
    refs = tuple(referencia) if isinstance(referencia, (list, tuple)) else (referencia,)  # uma ou várias gravações
    if refs not in _latentes:
        _latentes[refs] = m.get_conditioning_latents(audio_path=list(refs))
    gpt, spk = _latentes[refs]
    partes = []
    for f in frases(texto):
        with torch.inference_mode():
            wav = m.inference(f, "pt", gpt, spk, speed=velocidade, temperature=0.7)["wav"]
        partes.append(np.asarray(wav, dtype=np.float32))
        # pausa menor depois de dois-pontos e ponto e vírgula
        partes.append(np.zeros(int((pausa * 0.55 if f[-1] in ":;" else pausa) * SR), np.float32))
    audio = np.concatenate(partes[:-1]) if partes else np.zeros(SR // 2, np.float32)
    audio = audio / max(1e-6, np.abs(audio).max()) * 0.9

    wav_path = saida if saida.endswith(".wav") else saida.rsplit(".", 1)[0] + ".wav"
    sf.write(wav_path, audio, SR)
    if saida.endswith(".mp3"):  # precisa do ffmpeg instalado
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav_path, "-b:a", "128k", saida], check=True)
        os.remove(wav_path)
    return saida


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    print(gerar(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "saida.wav"))
