# Vídeos de estudo com HyperFrames

Cada pasta aqui dentro é um vídeo feito com [HyperFrames](https://github.com/heygen-com/hyperframes):
você escreve HTML/CSS com animações e ele renderiza um MP4.

- `demo-medicina/` é um exemplo de 15 s sobre o **Sistema Renina-Angiotensina-Aldosterona**.
  O vídeo pronto está em `demo-medicina/renders/sraa-demo.mp4`.

## Pedindo um vídeo novo ao Claude

Os skills do HyperFrames estão em `.claude/skills/`, então em qualquer sessão do Claude Code neste
repositório basta pedir, por exemplo:

> Faz um vídeo de 30 s sobre o ciclo cardíaco, com as fases e as bulhas B1 e B2.

Dá também para mandar slides, resumos ou a transcrição da aula como base.

## Rodando no seu computador

Você precisa de Node.js 22+ e FFmpeg.

```bash
npx hyperframes browser ensure          # baixa o Chrome usado na renderização (uma vez só)
cd videos/demo-medicina
npx hyperframes preview                 # abre o editor no navegador
npx hyperframes check                   # confere erros antes de renderizar
npx hyperframes render -o renders/video.mp4
```

Para começar um vídeo do zero: `npx hyperframes init videos/nome-do-video`.
