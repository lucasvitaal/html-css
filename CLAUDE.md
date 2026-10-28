# Notas para o Claude neste repositório

O Lucas é estudante de medicina e usa este repositório para vídeos de estudo feitos com HyperFrames
(`videos/`). Os skills do HyperFrames estão em `.claude/skills/`.

## Narração com ElevenLabs: gastar o mínimo de créditos

O plano dele é o Starter (cerca de 30 mil créditos por mês). Regras para qualquer narração:

- **1 take por fala** (`generations_count: 1`). Dois takes dobram o custo e ninguém escolhe entre eles.
- **Estime e avise antes.** Use `estimate_only` (no eleven_v4 é ~1 crédito por caractere). Acima de
  ~2 mil créditos, espere o ok do Lucas.
- **Trocar de modelo não economiza:** no plano dele o `eleven_flash_v2_5` custa o mesmo que o
  `eleven_v4` (1 crédito por caractere, conferido com `estimate_only` em 28/10/2026). Use o
  `eleven_v4`, que aceita `[pause]` e tags de emoção.
- **Híbrido:** explicação longa com a voz grátis (Kokoro local: `FONTE=kokoro python3 build.py`, com
  pausas reais entre frases) e ElevenLabs só onde a voz faz diferença (abertura, zoeira, Dr. Gorila).
- **Teste 1 cena ou 1 capítulo** antes de narrar o material todo.
- **Nunca regere fala que já existe.** Os áudios ficam salvos (`videos/sua-5min/assets/eleven/`);
  ao mudar o roteiro, gere só as falas alteradas.
- **Enxugue o texto antes** (o custo é por caractere) e não narre instruções, referências ou slides
  de transição.
