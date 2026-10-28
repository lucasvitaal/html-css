"""Interface web do motor de voz. Rode: python app.py  (no Colab: python app.py --share)"""
import sys

import gradio as gr

from motor import gerar


def acao(texto, referencia, pausa, velocidade):
    if not texto or not texto.strip():
        raise gr.Error("Escreva o texto.")
    if not referencia:
        raise gr.Error("Envie o áudio de referência (5 a 10 s).")
    return gerar(texto, referencia, "resultado.wav", pausa, velocidade)


with gr.Blocks(title="Voz local") as demo:
    gr.Markdown("# Voz local · XTTS v2\nClone só a sua voz ou a de quem autorizou.")
    texto = gr.Textbox(label="Texto em português", lines=6)
    referencia = gr.Audio(label="Voz de referência (5 a 10 s, fala limpa, sem música)", type="filepath")
    with gr.Row():
        pausa = gr.Slider(0.1, 1.5, value=0.45, step=0.05, label="Pausa entre frases (s)")
        velocidade = gr.Slider(0.7, 1.3, value=1.0, step=0.05, label="Velocidade")
    botao = gr.Button("Gerar Voz Clonada", variant="primary")
    resultado = gr.Audio(label="Resultado (o player tem botão de baixar)", type="filepath")
    botao.click(acao, [texto, referencia, pausa, velocidade], resultado)

if __name__ == "__main__":
    demo.queue().launch(share="--share" in sys.argv)
