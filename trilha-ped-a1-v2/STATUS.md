# Status — Trilha de Pediatria A1 · 2.0

- **Trilha publicada:** https://claude.ai/artifact/DGRj4UW3T5AczVHfyQ5YBH (privada; capacidades db, user, sample)
- **Meta:** afiado até sexta 30/10/2026 (relógio do app em 30/10 07:00 — hora e formato da prova não confirmados; formato assumido: misto, casos + objetivas, como nas A1 antigas)
- **Professora que faz a prova:** Profa. Patrícia Dahan (10 aulas, A–J)
- **Fontes usadas:** Trilha Ped A1 1.0 (artefato 5fnosUz2m7NakASDpvee9B: resumos, 70 questões, pontos duvidosos citando slides e MEDCURSO) + Tour Provas A1 Ped (Suyfgre1vLvRkZzpDFHygS: 3 provas antigas + gabarito mínimo 2025/2).
- **Faltam:** PDFs dos slides (aba Slides vazia; refs “Sl. N” no texto) e gravações da Patrícia (SAY/NOSAY vazios — sem citação literal).
- **Conteúdo:** 10 capítulos · 92 blocos narrados · 92 esquemas · 74 questões (70 autorais 1.0 + 2 de prova antiga + 2 novas) · 22 casos (17 de provas antigas/2025/2) · 169 flash · 36 divergências · 14 missões (26–29/10).
- **O que ela mais repete:** bebê sacudido (4×), dengue grupo B 15 kg (3×), adenite + supraclavicular (3×), escarlatina × mono (2×), cefaleia com alarme (2×), meningite < 2 m (2×), investigação de ITU (2×). Hepatites nunca caiu.
- **Divergências-chave resolvidas:** tríade do sacudido (slide 36 + gabarito 2025/2), escarlatina (benzatina ou amoxicilina 10 d + afastar 48 h), grupo C (20 mL/kg/h × gabarito “em 2 h”), pós-BCG (slide: isoniazida), Ig do sarampo (< 1 ano slide).

## Como regenerar
```
python3 trabalho/gerar.py                       # trabalho/cap*.py + extras.py -> dados/conteudo.json
# build com o motor corrigido (trabalho/motor/template.html: aba Slides sem PDFs não quebra)
cp trabalho/motor/template.html <skill>/assets/template.html   # numa cópia da skill
python3 <skill>/scripts/build.py . && python3 <skill>/scripts/smoke.py saida/index.html
# depois do build: trocar <title>Trilha de estudos</title> por <title>Trilha Ped A1 2.0</title>
# publicar SEMPRE com a url acima
```
