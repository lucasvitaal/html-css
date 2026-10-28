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

## Narrar um material inteiro (modo Lote)

Na aba **Lote** do app, escolha um lote pronto (ou cole o seu) e clique em **Gerar todos**. Sai um zip com
um mp3 por fala, e uma cópia vai para *Meu Drive/voz-local* se o Drive estiver montado.

| Lote | O que narra | Nomes dos áudios |
|---|---|---|
| `lotes/sua40.txt` | Ensaio SUA 40 min, uma fala por slide | `01.mp3` … `62.mp3` |
| `lotes/sua5min.txt` | vídeo SUA 5 min, uma fala por trecho | `abertura-0.mp3` … |
| `lotes/pedA1.txt` | Trilha Ped A1: aula (`m`), zoeira (`z`) e pegadinha (`p`) de cada bloco | `a_adenite-m-00.mp3` … |

O texto já vem pronto para a voz: frases curtas, números, unidades e siglas por extenso
("40.000" → "quarenta mil", "3×/dia" → "três vezes ao dia", "β-hCG" → "beta agá cê gê").
Para um material novo, monte um JSON `{"nome": "texto"}` e rode `python narracao.py entrada.json lote.txt`.

O botão **🦍 Usar a voz do Dr. Gorila** carrega `referencias/dr_gorila.wav` (a voz grave grátis, sintética).

### Como os áudios entram no artefato

Deixe o zip no Drive (pasta *voz-local*) e peça ao Claude: "monta o zip sua40 no Ensaio". Ele baixa o zip e roda:

```
python montar.py ensaio sua40.zip ensaio/a/                 # Ensaio: a/NN.mp3, depois republica o artefato
python montar.py trilha pedA1.zip segs.json trilha/aud/     # Trilha: <bloco>-<grupo>.mp3 + clips.json (CFG.vozGravada)
python montar.py video sua5min.zip ../videos/sua-5min/assets/xtts/ && FONTE=xtts python3 build.py   # vídeo
```

No Ensaio cada slide toca o seu `a/NN.mp3`. Na trilha, o `clips.json` diz onde cada frase começa e termina
dentro do mp3 do bloco, para a palavra atual acender junto com a voz.

## Dicas

- Referência boa: 6 a 10 s, uma pessoa só, sem eco nem música, no tom que você quer.
- Cada frase é gerada à parte, com pausa real entre elas (ajuste no controle deslizante).
- Só clone a sua voz ou a de quem autorizou.
