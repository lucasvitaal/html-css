"""Interface web do motor de voz. Rode: python app.py  (no Colab: python app.py --share)"""
import os
import re
import shutil
import sys
import tempfile
import urllib.request
import zipfile

import gradio as gr

from motor import gerar

DRIVE = "/content/drive/MyDrive/voz-local"  # no Colab, com o Drive montado, o zip do lote também vai para lá
BASE = os.environ.get("VOZ_BASE", "https://raw.githubusercontent.com/lucasvitaal/html-css/claude/serene-fermi-ytdjfk/voz-local/")
LOTES = ["sua40", "sua5min", "pedA1"]  # arquivos em lotes/ do repositório


def baixar(caminho):
    with urllib.request.urlopen(BASE + caminho, timeout=30) as r:
        return r.read()


def carregar_lote(nome):
    return baixar(f"lotes/{nome}.txt").decode("utf-8") if nome else ""


def voz_gorila():
    destino = os.path.join(tempfile.mkdtemp(), "dr_gorila.wav")
    with open(destino, "wb") as f:
        f.write(baixar("referencias/dr_gorila.wav"))
    return destino


def acao(texto, referencia, pausa, velocidade):
    if not texto or not texto.strip():
        raise gr.Error("Escreva o texto.")
    if not referencia:
        raise gr.Error("Envie o áudio de referência (5 a 10 s).")
    return gerar(texto, referencia, "resultado.wav", pausa, velocidade)


def ler_lote(texto):
    """'## nome' abre uma fala; as linhas seguintes são as frases dela."""
    itens = re.findall(r"^##\s*(\S+)\s*\n(.*?)(?=^##|\Z)", texto, flags=re.M | re.S)
    return [(nome, corpo.strip()) for nome, corpo in itens if corpo.strip()]


def acao_lote(texto, referencia, pausa, velocidade, nome_zip, progress=gr.Progress()):
    if not referencia:
        raise gr.Error("Envie o áudio de referência (5 a 10 s).")
    itens = ler_lote(texto or "")
    if not itens:
        raise gr.Error("Nenhuma fala encontrada. Cada fala começa com uma linha '## nome'.")
    pasta = tempfile.mkdtemp()
    for nome, corpo in progress.tqdm(itens, desc="Gerando"):
        gerar(corpo, referencia, os.path.join(pasta, nome + ".mp3"), pausa, velocidade)
    nome_zip = re.sub(r"[^\w-]", "_", nome_zip or "lote") + ".zip"
    zip_path = os.path.join(tempfile.mkdtemp(), nome_zip)
    with zipfile.ZipFile(zip_path, "w") as z:
        for nome, _ in itens:
            z.write(os.path.join(pasta, nome + ".mp3"), nome + ".mp3")
    aviso = f"{len(itens)} áudios em {nome_zip}."
    if os.path.isdir(os.path.dirname(DRIVE)):
        os.makedirs(DRIVE, exist_ok=True)
        shutil.copy(zip_path, DRIVE)
        aviso += f" Cópia salva no seu Drive em voz-local/{nome_zip}."
    return zip_path, aviso


with gr.Blocks(title="Voz local") as demo:
    gr.Markdown("# Voz local · XTTS v2\nClone só a sua voz ou a de quem autorizou.")
    referencia = gr.Audio(label="Voz de referência (5 a 10 s, fala limpa, sem música)", type="filepath")
    gr.Button("🦍 Usar a voz do Dr. Gorila", size="sm").click(voz_gorila, None, referencia)
    with gr.Row():
        pausa = gr.Slider(0.1, 1.5, value=0.45, step=0.05, label="Pausa entre frases (s)")
        velocidade = gr.Slider(0.7, 1.3, value=1.0, step=0.05, label="Velocidade")
    with gr.Tab("Uma fala"):
        texto = gr.Textbox(label="Texto em português", lines=6)
        botao = gr.Button("Gerar Voz Clonada", variant="primary")
        resultado = gr.Audio(label="Resultado (o player tem botão de baixar)", type="filepath")
        botao.click(acao, [texto, referencia, pausa, velocidade], resultado)
    with gr.Tab("Lote (um áudio por slide)"):
        pronto = gr.Dropdown(LOTES, label="Lote pronto (ou cole o seu abaixo)", value=None)
        lote = gr.Textbox(label="Cole o lote: cada fala começa com '## nome' e vira nome.mp3", lines=14)
        nome_zip = gr.Textbox(label="Nome do zip", value="lote")
        pronto.change(carregar_lote, pronto, lote).then(lambda n: n or "lote", pronto, nome_zip)
        botao_lote = gr.Button("Gerar todos", variant="primary")
        zip_out = gr.File(label="Zip com os áudios")
        aviso = gr.Markdown()
        botao_lote.click(acao_lote, [lote, referencia, pausa, velocidade, nome_zip], [zip_out, aviso])

if __name__ == "__main__":
    demo.queue().launch(share="--share" in sys.argv)
