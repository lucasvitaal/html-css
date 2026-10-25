"""Missões (plano até sexta 30/10), medalhas temáticas e falas do Dr. Gorila.
SAY/NOSAY ficam vazios: esta versão não tem as gravações da Patrícia (sem citação literal não se escreve)."""

MISSIONS = [
 {"id": "m1", "nm": "🛡️ Violência (caiu 4×)", "dl": "2026-10-26T16:00:00-03:00", "tipo": "cap", "cap": 5},
 {"id": "m2", "nm": "🦟 Dengue (caiu 3×)", "dl": "2026-10-26T20:00:00-03:00", "tipo": "cap", "cap": 6},
 {"id": "m3", "nm": "🧴 Dermatoses", "dl": "2026-10-26T23:30:00-03:00", "tipo": "cap", "cap": 1},
 {"id": "m4", "nm": "🦠 Exantemáticas", "dl": "2026-10-27T16:00:00-03:00", "tipo": "cap", "cap": 2},
 {"id": "m5", "nm": "🔎 Adenomegalias e câncer", "dl": "2026-10-27T20:00:00-03:00", "tipo": "cap", "cap": 4},
 {"id": "m6", "nm": "🤕 Dores recorrentes", "dl": "2026-10-27T23:30:00-03:00", "tipo": "cap", "cap": 3},
 {"id": "m7", "nm": "🧠 Meningites", "dl": "2026-10-28T16:00:00-03:00", "tipo": "cap", "cap": 8},
 {"id": "m8", "nm": "🚽 ITU", "dl": "2026-10-28T20:00:00-03:00", "tipo": "cap", "cap": 9},
 {"id": "m9", "nm": "🫀 Choque", "dl": "2026-10-28T23:30:00-03:00", "tipo": "cap", "cap": 10},
 {"id": "m10", "nm": "🟡 Hepatites", "dl": "2026-10-29T10:30:00-03:00", "tipo": "cap", "cap": 7},
 {"id": "m10b", "nm": "💩 Constipação (aula nova)", "dl": "2026-10-29T12:30:00-03:00", "tipo": "cap", "cap": 11},
 {"id": "m10c", "nm": "🍼 RGE (aula nova, caiu 2×)", "dl": "2026-10-29T14:30:00-03:00", "tipo": "cap", "cap": 12},
 {"id": "m11", "nm": "📝 Todas as questões", "dl": "2026-10-29T17:00:00-03:00", "tipo": "questoes"},
 {"id": "m12", "nm": "✍️ 1 caso por capítulo", "dl": "2026-10-29T20:00:00-03:00", "tipo": "casos"},
 {"id": "m13", "nm": "⏱️ Um simulado", "dl": "2026-10-29T22:00:00-03:00", "tipo": "prova"},
 {"id": "m14", "nm": "⚡ Pegadinhas + ≠", "dl": "2026-10-29T23:30:00-03:00", "tipo": "vesp"},
]

MEDALS_EXTRA = [
 {"id": "dengue", "ic": "💧", "nm": "Hidratador oficial", "ds": "Acertar todas de dengue",
  "qs": ["q06_1", "q06_2", "q06_3", "q06_4", "q06_5", "q06_6", "q06_7", "q06_8"]},
 {"id": "lcr", "ic": "🧪", "nm": "Leitor de líquor", "ds": "Acertar as de líquor", "qs": ["q08_2", "q08_3", "qn_lcr"]},
 {"id": "hepb", "ic": "🟡", "nm": "Sorologista", "ds": "Acertar os marcadores da hepatite B", "qs": ["q07_1", "q07_2", "q07_3", "q07_8"]},
 {"id": "exan", "ic": "🍓", "nm": "Lixa e framboesa", "ds": "Acertar as exantemáticas que caíram", "qs": ["q02_4", "qa_saramp", "qa_mono"]},
 {"id": "choque", "ic": "🫀", "nm": "Setenta mais duas vezes a idade", "ds": "Acertar as de choque", "qs": ["q10_1", "q10_2", "q10_3", "q10_5", "q10_7"]},
]

GORILA_FALAS = [
 "Hematoma subdural, hemorragia retiniana, sem trauma. Caiu quatro vezes. Vai cair a quinta.",
 "Grupo B é soro pela BOCA. Na unidade. Cinquenta por quilo. Não me faz repetir.",
 "Supraclavicular direita, tórax. Esquerda, abdome. Banana na mão direita, cérebro na esquerda.",
 "Setenta mais duas vezes a idade. Calcula antes de dizer que a pressão está boa.",
 "Menor de dois meses: ampicilina. Listeria ri da sua ceftriaxona.",
 "Uretrocistografia é DEPOIS do tratamento. Os compilados esqueceram dela. Você não vai.",
 "Vinte e cinco quilos: o corte da benzatina. Seiscentas mil abaixo, um milhão e duzentas acima.",
 "Kawasaki tratado é prognóstico BOM. Quem escreveu “ruim” no compilado comeu casca de banana.",
 "Suspeitou de maus-tratos? Notifica. Dúvida não é desculpa.",
 "Cefaleia de manhã, acordando de madrugada, quatro anos: secundária. Pressão e fundo de olho.",
 "Quinze quilos no Holliday: mil duzentos e cinquenta. O cinquenta é só acima de dez.",
 "Anti-HBc positivo nunca é só vacina. Vacinado tem só anti-HBs.",
]
