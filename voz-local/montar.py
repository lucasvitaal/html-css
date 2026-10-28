"""Leva o zip do modo Lote do app para dentro de um artefato ou vídeo.

    python montar.py ensaio lote.zip pasta/        # NN.mp3 leves (64 kbps) para o Ensaio: pasta a/
    python montar.py video  lote.zip pasta/        # <cena>-<fala>.mp3 para o vídeo (FONTE=xtts no build.py)
    python montar.py trilha lote.zip segs.json pasta/
        # junta <bloco>-<grupo>-<nn>.mp3 em <bloco>-<grupo>.mp3, com pausas reais,
        # e escreve clips.json para o CFG.vozGravada da trilha

Precisa de ffmpeg, numpy e soundfile.
"""
import json
import os
import subprocess
import sys
import tempfile
import zipfile

import numpy as np
import soundfile as sf

SR = 24000
P_FRASE, P_SECAO = 0.5, 0.85  # entre falas do mesmo tipo / ao mudar de tipo (aula -> divergência...)


def ler(caminho):
    wav = caminho + ".wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", caminho, "-ar", str(SR), "-ac", "1", wav], check=True)
    a, _ = sf.read(wav, dtype="float32")
    os.remove(wav)
    v = np.flatnonzero(np.abs(a) > 0.01)  # apara silêncio das pontas
    return a[max(0, v[0] - 720): v[-1] + 1200] if len(v) else a


def mp3(a, destino, kbps=48):
    wav = destino + ".wav"
    sf.write(wav, a, SR)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", wav, "-af", "loudnorm=I=-18:TP=-2:LRA=9",
                    "-ar", str(SR), "-ac", "1", "-b:a", f"{kbps}k", destino], check=True)
    os.remove(wav)


def extrair(zip_path):
    pasta = tempfile.mkdtemp()
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(pasta)
    return {os.path.splitext(n)[0]: os.path.join(pasta, n) for n in os.listdir(pasta) if n.endswith(".mp3")}


def ensaio(zip_path, saida):
    os.makedirs(saida, exist_ok=True)
    for nome, f in sorted(extrair(zip_path).items()):
        mp3(ler(f), os.path.join(saida, nome.zfill(2) + ".mp3"), 64)
        print(nome)


def video(zip_path, saida):
    os.makedirs(saida, exist_ok=True)
    for nome, f in sorted(extrair(zip_path).items()):
        sf.write(os.path.join(saida, nome + ".wav"), ler(f), SR)  # o build.py lê wav ou mp3
        print(nome)


def trilha(zip_path, segs_path, saida):
    os.makedirs(saida, exist_ok=True)
    arquivos = extrair(zip_path)
    segs = json.load(open(segs_path))
    clips_path = os.path.join(saida, "clips.json")
    clips = json.load(open(clips_path)) if os.path.exists(clips_path) else {}
    grupo = lambda x: "p" if x["k"] == "pega" else "z" if x["k"] == "zoe" else "m"
    for bid, S in segs.items():
        for g in "mzp":
            lst = [x for x in S if grupo(x) == g]
            nomes = [f"{bid}-{g}-{j:02d}" for j in range(len(lst))]
            if not lst or not all(n in arquivos for n in nomes):
                continue  # grupo incompleto no zip: mantém o que já havia
            audio, marcas, t, prev = [], [], 0.0, None
            for x, n in zip(lst, nomes):
                if prev is not None:
                    gap = P_FRASE if x["k"] == prev else P_SECAO
                    audio.append(np.zeros(int(gap * SR), "float32"))
                    t += gap
                a = ler(arquivos[n])
                audio.append(a)
                # o motor confere o tamanho do texto: tem que ser o texto da fala na trilha
                marcas.append([round(t, 3), round(t + len(a) / SR, 3), len(x["sp"] or x["t"])])
                t += len(a) / SR
                prev = x["k"]
            mp3(np.concatenate(audio), os.path.join(saida, f"{bid}-{g}.mp3"))
            clips.setdefault(bid, {})[g] = marcas
        print(bid)
    json.dump(clips, open(clips_path, "w"))


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else ""
    if modo == "ensaio" and len(sys.argv) == 4:
        ensaio(sys.argv[2], sys.argv[3])
    elif modo == "video" and len(sys.argv) == 4:
        video(sys.argv[2], sys.argv[3])
    elif modo == "trilha" and len(sys.argv) == 5:
        trilha(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        sys.exit(__doc__)
