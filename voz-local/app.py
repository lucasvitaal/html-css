"""App de voz local (XTTS v2) com Drive. Rode: python app.py  (no Colab: python app.py --share)

No Colab, com o Drive montado, tudo fica em Meu Drive/voz-local/:
  voz_lucas.wav      voz de referência padrão (5 a 10 s), usada quando nenhuma é enviada
  saidas/            áudios gerados (<nome>.mp3) e lotes (<nome>.zip + pasta <nome>/)
  pedidos/           um .txt aqui vira áudio sozinho: pedidos/aula1.txt -> saidas/aula1.mp3
                     (texto que começa com "## nome" é um lote: saidas/aula1.zip)
  link.txt           endereço gradio.live da sessão atual; status.txt diz se o app está no ar

API (gradio): falar(texto, nome) -> caminho do mp3 em saidas/.
"""
import datetime
import os
import re
import shutil
import sys
import tempfile
import threading
import time
import traceback
import urllib.request
import zipfile

BASE = os.environ.get("VOZ_BASE", "https://raw.githubusercontent.com/lucasvitaal/html-css/claude/serene-fermi-ytdjfk/voz-local/")
AQUI = os.path.dirname(os.path.abspath(__file__))


def baixar(caminho):
    with urllib.request.urlopen(BASE + caminho, timeout=30) as r:
        return r.read()


if not os.path.exists(os.path.join(AQUI, "narracao.py")):  # o notebook baixa só app.py e motor.py
    with open(os.path.join(AQUI, "narracao.py"), "wb") as f:
        f.write(baixar("narracao.py"))

import gradio as gr  # noqa: E402

from motor import gerar  # noqa: E402

DRIVE = os.environ.get("VOZ_DRIVE", "/content/drive/MyDrive/voz-local")
if not os.path.isdir(os.path.dirname(DRIVE)):  # fora do Colab (ou sem Drive): pasta local
    DRIVE = os.path.join(AQUI, "voz-local")
SAIDAS, PEDIDOS = os.path.join(DRIVE, "saidas"), os.path.join(DRIVE, "pedidos")
VOZ_PADRAO = os.path.join(DRIVE, "voz_lucas.wav")
LOTES = ["sua40", "sua5min", "pedA1"]  # testes prontos em lotes/ do repositório
for d in (SAIDAS, PEDIDOS, os.path.join(PEDIDOS, "feitos")):
    os.makedirs(d, exist_ok=True)


def agora():
    return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))).strftime("%Y-%m-%d %H:%M")


def nome_livre(nome, texto):
    """Nome de arquivo seguro; sem nome, data + começo do texto."""
    nome = re.sub(r"[^\w-]+", "_", (nome or "").strip()).strip("_")
    if not nome:
        inicio = re.sub(r"[^\w]+", "-", texto.lower())[:30].strip("-")
        nome = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + "_" + inicio
    return nome


def voz(referencia):
    if referencia:
        return referencia
    if os.path.exists(VOZ_PADRAO):
        return VOZ_PADRAO
    raise gr.Error("Sem voz: envie um áudio de 5 a 10 s ou salve voz_lucas.wav em Meu Drive/voz-local.")


def para_drive(origem, destino):
    """Gera fora do Drive e copia pronto, para o Claude nunca achar um mp3 pela metade."""
    shutil.copy(origem, destino + ".parcial")
    os.replace(destino + ".parcial", destino)
    return destino


def uma_fala(texto, referencia=None, nome="", pausa=0.45, velocidade=1.0, normalizar=True):
    if not texto or not texto.strip():
        raise gr.Error("Escreva o texto.")
    nome = nome_livre(nome, texto)
    tmp = os.path.join(tempfile.mkdtemp(), nome + ".mp3")
    gerar(texto, voz(referencia), tmp, pausa, velocidade, normalizar)
    return para_drive(tmp, os.path.join(SAIDAS, nome + ".mp3"))


def ler_lote(texto):
    """'## nome' abre uma fala; as linhas seguintes são as frases dela."""
    itens = re.findall(r"^##\s*(\S+)\s*\n(.*?)(?=^##|\Z)", texto, flags=re.M | re.S)
    return [(nome, corpo.strip()) for nome, corpo in itens if corpo.strip()]


def lote(texto, referencia=None, nome="lote", pausa=0.45, velocidade=1.0, normalizar=True, progresso=None):
    itens = ler_lote(texto or "")
    if not itens:
        raise gr.Error("Nenhuma fala encontrada. Cada fala começa com uma linha '## nome'.")
    ref, nome = voz(referencia), nome_livre(nome, "lote")
    tmp = tempfile.mkdtemp()
    for n, corpo in (progresso.tqdm(itens, desc="Gerando") if progresso else itens):
        gerar(corpo, ref, os.path.join(tmp, n + ".mp3"), pausa, velocidade, normalizar)
    zip_tmp = os.path.join(tmp, nome + ".zip")
    with zipfile.ZipFile(zip_tmp, "w") as z:
        for n, _ in itens:
            z.write(os.path.join(tmp, n + ".mp3"), n + ".mp3")
    pasta = os.path.join(SAIDAS, nome)
    os.makedirs(pasta, exist_ok=True)
    for n, _ in itens:
        para_drive(os.path.join(tmp, n + ".mp3"), os.path.join(pasta, n + ".mp3"))
    return para_drive(zip_tmp, os.path.join(SAIDAS, nome + ".zip")), len(itens)


# ---------------------------------------------------------------- pedidos pelo Drive
def vigiar_pedidos():
    """Cada pedidos/<nome>.txt vira saidas/<nome>.mp3 (ou .zip, se for lote). Erro vai para saidas/<nome>.erro.txt."""
    ultimo = 0
    while True:
        try:
            if time.time() - ultimo > 60:  # sinal de vida para quem lê o Drive
                with open(os.path.join(DRIVE, "status.txt"), "w") as f:
                    f.write(f"no ar: {agora()} (Brasília)\n")
                ultimo = time.time()
            for arq in sorted(os.listdir(PEDIDOS)):
                if not arq.endswith(".txt") or arq.startswith("."):
                    continue
                caminho, nome = os.path.join(PEDIDOS, arq), arq[:-4]
                texto = open(caminho, encoding="utf-8").read()
                print("pedido:", arq, flush=True)
                try:
                    if texto.lstrip().startswith("##"):
                        lote(texto, nome=nome)
                    else:
                        uma_fala(texto, nome=nome)
                except Exception:
                    with open(os.path.join(SAIDAS, nome + ".erro.txt"), "w") as f:
                        f.write(traceback.format_exc())
                os.replace(caminho, os.path.join(PEDIDOS, "feitos", arq))
        except Exception:
            traceback.print_exc()
        time.sleep(10)


# ---------------------------------------------------------------- interface
def ui_fala(texto, referencia, nome, pausa, velocidade, normalizar):
    caminho = uma_fala(texto, referencia, nome, pausa, velocidade, normalizar)
    return caminho, "Salvo no Drive: `" + os.path.relpath(caminho, os.path.dirname(DRIVE)) + "`"


def ui_lote(texto, referencia, nome, pausa, velocidade, normalizar, progress=gr.Progress()):
    caminho, n = lote(texto, referencia, nome, pausa, velocidade, normalizar, progress)
    return caminho, f"{n} áudios. Salvo no Drive: `{os.path.relpath(caminho, os.path.dirname(DRIVE))}`"


def api_falar(texto, nome=""):
    """Para chamar de fora: texto -> caminho do mp3 no Drive (voz padrão, texto normalizado)."""
    return uma_fala(texto, None, nome)


def salvar_padrao(referencia):
    if not referencia:
        raise gr.Error("Envie a voz primeiro.")
    shutil.copy(referencia, VOZ_PADRAO)
    return "Voz padrão salva em voz-local/voz_lucas.wav"


def carregar_lote(nome):
    return baixar(f"lotes/{nome}.txt").decode("utf-8") if nome else ""


def voz_gorila():
    destino = os.path.join(tempfile.mkdtemp(), "dr_gorila.wav")
    with open(destino, "wb") as f:
        f.write(baixar("referencias/dr_gorila.wav"))
    return destino


with gr.Blocks(title="Voz local") as demo:
    gr.Markdown("# Voz local · XTTS v2\nClone só a sua voz ou a de quem autorizou.")
    tem_padrao = os.path.exists(VOZ_PADRAO)
    referencia = gr.Audio(label="Voz de referência (vazio = voz padrão do Drive)", type="filepath")
    gr.Markdown("Voz padrão: **voz_lucas.wav** do Drive." if tem_padrao else
                "Sem voz padrão ainda: envie uma voz e clique em *Salvar como padrão*.")
    with gr.Row():
        gr.Button("Salvar como padrão", size="sm").click(salvar_padrao, referencia, gr.Markdown())
        gr.Button("🦍 Usar a voz do Dr. Gorila", size="sm").click(voz_gorila, None, referencia)
    with gr.Row():
        pausa = gr.Slider(0.1, 1.5, value=0.45, step=0.05, label="Pausa entre frases (s)")
        velocidade = gr.Slider(0.7, 1.3, value=1.0, step=0.05, label="Velocidade")
        normalizar = gr.Checkbox(True, label="Escrever números e siglas por extenso")
    with gr.Tab("Uma fala"):
        texto = gr.Textbox(label="Texto em português", lines=6)
        nome = gr.Textbox(label="Nome do arquivo (opcional)")
        botao = gr.Button("Gerar Voz Clonada", variant="primary")
        resultado = gr.Audio(label="Resultado (o player tem botão de baixar)", type="filepath")
        onde = gr.Markdown()
        botao.click(ui_fala, [texto, referencia, nome, pausa, velocidade, normalizar], [resultado, onde])
    with gr.Tab("Lote (um áudio por slide)"):
        pronto = gr.Dropdown(LOTES, label="Lote de teste (ou cole o seu abaixo)", value=None)
        texto_lote = gr.Textbox(label="Cada fala começa com '## nome' e vira nome.mp3", lines=14)
        nome_lote = gr.Textbox(label="Nome do lote", value="lote")
        pronto.change(carregar_lote, pronto, texto_lote).then(lambda n: n or "lote", pronto, nome_lote)
        botao_lote = gr.Button("Gerar todos", variant="primary")
        zip_out = gr.File(label="Zip com os áudios")
        onde_lote = gr.Markdown()
        botao_lote.click(ui_lote, [texto_lote, referencia, nome_lote, pausa, velocidade, normalizar], [zip_out, onde_lote])
    # API: POST <link>/gradio_api/call/falar  {"data": ["texto", "nome"]}
    with gr.Row(visible=False):
        api_texto, api_nome, api_saida = gr.Textbox(), gr.Textbox(), gr.Textbox()
        gr.Button().click(api_falar, [api_texto, api_nome], api_saida, api_name="falar")

if __name__ == "__main__":
    threading.Thread(target=vigiar_pedidos, daemon=True).start()
    _, local, publico = demo.queue().launch(share="--share" in sys.argv, prevent_thread_lock=True)
    link = publico or local
    with open(os.path.join(DRIVE, "link.txt"), "w") as f:
        f.write(f"{link}\naberto em {agora()} (Brasília)\n")
    print("APP NO AR:", link, flush=True)
    demo.block_thread()
