# Notas para o Claude neste repositório

O Lucas é estudante de medicina e usa este repositório para vídeos de estudo feitos com HyperFrames
(`videos/`). Os skills do HyperFrames estão em `.claude/skills/`.

## Narração com ElevenLabs: gastar o mínimo de créditos

O plano dele é o Starter (cerca de 30 mil créditos por mês). Regras para qualquer narração:

- **1 take por fala** (`generations_count: 1`). Dois takes dobram o custo e ninguém escolhe entre eles.
- **Estime e avise antes.** Use `estimate_only` (no eleven_v4 é ~1 crédito por caractere). Acima de
  ~2 mil créditos, espere o ok do Lucas.
- **Narração longa no `eleven_flash_v2_5`**, que custa metade do eleven_v4. Ele não aceita tags como
  `[pause]` ou `[sarcastic]`: use poucas `<break time="0.5s" />` e silêncio na montagem (o
  `videos/sua-5min/build.py` já insere pausas entre falas e cenas). `eleven_v4` só em trechos curtos
  que precisam de emoção.
- **Híbrido:** explicação longa com a voz grátis (Kokoro local: `FONTE=kokoro python3 build.py`, com
  pausas reais entre frases) e ElevenLabs só onde a voz faz diferença (abertura, zoeira, Dr. Gorila).
- **Teste 1 cena ou 1 capítulo** antes de narrar o material todo.
- **Nunca regere fala que já existe.** Os áudios ficam salvos (`videos/sua-5min/assets/eleven/`);
  ao mudar o roteiro, gere só as falas alteradas.
- **Enxugue o texto antes** (o custo é por caractere) e não narre instruções, referências ou slides
  de transição.
