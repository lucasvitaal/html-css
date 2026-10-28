# Voz local (clone grátis do ElevenLabs)

Texto em português → fala, com a voz de um áudio de referência de 5 a 10 s. Usa o XTTS v2
(Coqui, licença não comercial). Não gasta crédito nenhum.

## No Google Colab (grátis, recomendado)

Ambiente de execução → Alterar tipo → **GPU T4**. Depois, numa célula:

```
!git clone https://github.com/lucasvitaal/html-css && cd html-css && git checkout claude/serene-fermi-ytdjfk
%cd html-css/voz-local
!pip install -q -r requirements.txt
!python app.py --share
```

Abra o link `gradio.live` que aparecer. A primeira geração baixa o modelo (~1,8 GB, uns 2 min).

## No computador

Python 3.10 a 3.12. Instale o PyTorch pelo site (pytorch.org), depois:

```
pip install -r requirements.txt
python app.py            # abre em http://127.0.0.1:7860
python motor.py "Olá, Lucas." voz_modelo.wav saida.mp3   # sem interface (mp3 precisa de ffmpeg)
```

Sem placa NVIDIA funciona na CPU, mas devagar (cerca de 10 a 30 s por frase).

## Dicas

- Referência boa: 6 a 10 s, uma pessoa só, sem eco nem música, no tom que você quer.
- Cada frase é gerada à parte, com pausa real entre elas (ajuste no controle deslizante).
- Só clone a sua voz ou a de quem autorizou.
