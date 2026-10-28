---
name: voz-local
description: Gera narração grátis em português com o app voz-local do Lucas (XTTS v2 no Google Colab, voz clonada dele), no lugar do ElevenLabs. Use quando ele pedir áudio, narração, voz, "fala isso", ou narrar slides, trilhas e vídeos sem gastar crédito.
---

# Voz local: gerar áudio pelo Drive

O app roda no Colab do Lucas e conversa com o Claude pelo Google Drive, pasta **Meu Drive/voz-local/**:

| Arquivo | Para quê |
|---|---|
| `status.txt` | "no ar: AAAA-MM-DD HH:MM". Atualizado a cada minuto enquanto o app roda |
| `link.txt` | endereço gradio.live da sessão atual (só abre no navegador do PC dele) |
| `voz_lucas.wav` | voz padrão (5 a 10 s) |
| `pedidos/` | o Claude cria aqui `<nome>.txt`; o app gera e move o pedido para `pedidos/feitos/` |
| `saidas/` | `<nome>.mp3` (ou `<nome>.zip` + pasta `<nome>/` para lote); erro vira `<nome>.erro.txt` |

## Passo a passo

1. **O app está no ar?** Busque `status.txt` na pasta voz-local e leia. Se a hora tem mais de 3 min, o app
   está parado. Peça ao Lucas, ou à sessão Cowork que controla o navegador dele, para abrir
   https://colab.research.google.com/drive/1W06cifhz2MilX-DWY_9-1Gv4UQo0uD7i, conferir GPU T4
   (Ambiente de execução → Alterar o tipo), clicar em **Executar tudo**, autorizar o Drive e esperar
   "APP NO AR" na última célula (uns 4 min na primeira vez).
2. **Pedir o áudio.** Crie no Drive, dentro de `voz-local/pedidos/`, um arquivo `<nome>.txt`
   (`contentMimeType: text/plain`, `disableConversionToGoogleType: true`, senão vira Google Docs e o
   app não lê). Conteúdo:
   - uma fala: o texto puro;
   - lote: `## nome` antes de cada fala (um mp3 por fala). Monte com `voz-local/narracao.py`.
   Números, unidades e siglas são escritos por extenso sozinhos.
3. **Esperar.** O Drive leva de 10 s a 2 min para mostrar o pedido ao Colab; cada frase leva 1 a 2 s na T4.
   Procure `saidas/<nome>.mp3` (ou `.zip`); se aparecer `<nome>.erro.txt`, leia e corrija.
4. **Usar o mp3.** Baixe com o conector do Drive (o conteúdo vem em base64; se for grande, fica salvo num
   arquivo de resultado: decodifique com Python). Para artefatos e vídeos, veja `README.md ›
   Como os áudios entram no artefato` (`montar.py`).

## Pelo navegador (sessão Cowork)

Abra o endereço de `link.txt`. A interface tem *Uma fala* e *Lote*. Para chamar sem a interface:
`POST <link>/gradio_api/call/falar` com `{"data": ["texto", "nome"]}` devolve `event_id`;
`GET <link>/gradio_api/call/falar/<event_id>` devolve o caminho do mp3 em `saidas/`.

## Regras

- 1 pedido por arquivo; nome sem espaço (`aula1`, `sua40-slide12`). Nome repetido sobrescreve.
- Não narre referências, instruções nem slides de transição.
- Só a voz do Lucas ou vozes sintéticas (Dr. Gorila: botão no app). Não clone a voz de outra pessoa.
- O Colab grátis desliga depois de ~90 min sem uso ou ~12 h no total: aí é Executar tudo de novo.
