CAP = {"n": 3, "t": "Dores recorrentes na infância", "short": "Dores recorrentes", "aula": "Aula 3 · slides da Patrícia",
       "icon": "🤕", "col": "#5B3F8C",
       "bul": ["Recorrente = ≥ 3 episódios em ≥ 3 meses, interferindo nas atividades",
               "Abdominal: 90–95% funcional; alarme: desperta, periférica, irradia",
               "Dor de crescimento: bilateral, noturna, exame normal, melhora com massagem",
               "Cefaleia: caiu 2× (2,4 pts) — sinais de alarme, PA e exame neurológico"],
       "medalha": ["🤕", "Diário da dor"]}

BLOCKS = [
 {"id": "c_geral", "t": "Dor recorrente: definição e abordagem",
  "s": "<b>Dor recorrente</b> = <b>≥ 3 episódios</b> em <b>≥ 3 meses</b>, com intensidade que <b>interfere nas atividades</b> habituais. "
       "<br>Prevalências: <b>cefaleia 20,6%</b> · membros 15,5% · abdominal 14,4%. Orgânicas: <b>10–15%</b>. "
       "<br>Abordagem: anamnese detalhada, <b>entrevistar criança e pais separadamente</b>, estressores (escola, família), diário da dor, exame físico completo com curva de crescimento. "
       "<br>Os dois erros (slide 10): atitude simplista (“<b>não é nada</b>”) × <b>investigação extensa</b> desnecessária.",
  "fala": "Dor recorrente tem definição de prova: pelo menos três episódios num período de pelo menos três meses, com intensidade que atrapalha a vida da criança. A cefaleia é a mais frequente, depois membros e abdome, e só dez a quinze por cento têm causa orgânica. A abordagem é escutar a criança e os pais separadamente, procurar estressores e examinar com a curva de crescimento na mão, sem dizer que não é nada e sem pedir exame de tudo.",
  "div": "organ",
  "pega": "Critério: <b>3 episódios / 3 meses / interfere nas atividades</b>. Os dois erros: “não é nada” e investigação extensa.",
  "z": "Dizer “não é nada” pra mãe é o jeito mais rápido de ela trocar de pediatra; pedir tomografia de tudo é o jeito mais rápido de irradiar uma criança à toa. O meio-termo é anamnese, porra.",
  "ills": ["c_geral"]},
 {"id": "c_abd", "t": "Dor abdominal recorrente: a maioria é funcional",
  "s": "Picos: <b>4–6</b> e <b>7–12 anos</b>. <b>90–95% funcional</b>: dispepsia funcional, síndrome do intestino irritável, enxaqueca abdominal, dor abdominal funcional não especificada. "
       "<br>Dor periumbilical, sem relação clara com alimentação, criança bem entre as crises, crescimento no canal. "
       "<br>Conduta sem alarme: <b>abordagem ambulatorial</b>, explicar o mecanismo, orientar os pais sobre <b>sinais de alerta</b> e acompanhar; antiparasitário “(?)” no slide. Remissão em ~30% em 6 meses.",
  "fala": "Na dor abdominal recorrente, noventa a noventa e cinco por cento é funcional: dispepsia funcional, intestino irritável, enxaqueca abdominal ou a dor funcional não especificada. É a dor em volta do umbigo, numa criança que cresce bem e fica ótima entre as crises. Sem sinal de alarme, a conduta é ambulatorial: explicar que a dor é real, orientar os pais sobre os sinais de alerta e acompanhar.",
  "pega": "Sem sinal de alarme → <b>abordagem ambulatorial</b> e orientação; seis parasitológicos negativos não pedem o sétimo.",
  "z": "Seis parasitológicos negativos e a mãe querendo o sétimo? O verme não está no cocô, está na ansiedade da casa. Conversa, orienta e acompanha, caralho.",
  "ills": ["c_abd"]},
 {"id": "c_abdal", "t": "Dor abdominal: sinais de alerta e exames de nível 1",
  "s": "<b>Sinais de alerta</b> (gabarito 2025/2 em negrito): <b>dor que desperta a criança</b> · <b>localização periférica</b> (longe do umbigo) · <b>irradiação</b> (costas, escápula, membros) · <b>perda de peso / desaceleração do crescimento</b> · febre recorrente · <b>vômitos biliosos</b> · disfagia, diarreia noturna · <b>sangramento</b> GI · visceromegalia/massa · <b>história familiar</b> (DII, celíaca, úlcera péptica) · laboratório alterado. "
       "<br>Exames de <b>nível 1</b>: hemograma, VHS/PCR, urina e urocultura, parasitológico.",
  "fala": "O que transforma dor funcional em suspeita orgânica são os sinais de alerta. Os três do gabarito oficial são dor que acorda a criança, dor longe do umbigo e dor que irradia para costas, escápula ou pernas. Some a isso perda de peso ou desaceleração do crescimento, vômito bilioso, sangramento, febre, massa e história familiar de doença inflamatória, celíaca ou úlcera. Com alerta, começa pelos exames de nível um: hemograma, provas inflamatórias, urina e parasitológico.",
  "pega": "Peso é o parâmetro <b>mais sensível</b>: <b>queda na curva</b> é alerta. História familiar que pesa é de doença <b>orgânica GI</b>, não de cefaleia tensional da mãe.",
  "z": "Dor que acorda a criança, longe do umbigo e que corre pras costas: aí sim tem coisa. O resto é barriga de prova de matemática, porra.",
  "m": [["MEDCURSO · S26 Aval. 10:52–11:10", "O peso é o parâmetro mais sensível a doença: desacelerar na curva é sinal precoce."]],
  "ills": ["c_abdal"]},
 {"id": "c_cresc", "t": "Dor em membros e a dor de crescimento",
  "s": "Dor recorrente em membros: <b>4–10 anos</b>; orgânica em só <b>3–4%</b>. "
       "<br><b>Dor de crescimento</b> (<b>6–13 anos</b>): dor <b>bilateral</b> em MMII (coxa anterior, poplítea, panturrilha), difusa, crises de 10–15 min no <b>fim da tarde/noite</b> (pode acordar), criança ativa de dia, <b>exame físico normal</b>, melhora com <b>calor, massagem, analgésico</b>. Prognóstico benigno. "
       "<br>Diferenciais: hipermobilidade articular, fibromialgia (adolescente, tender points, sono/humor).",
  "fala": "Dor de crescimento é diagnóstico clínico de uma criança entre seis e treze anos com dor nas duas pernas, na coxa, atrás do joelho e na panturrilha, no fim da tarde ou à noite, que passa em poucos minutos com massagem ou calor. De dia ela brinca normalmente e o exame físico é normal. Os três pilares de prova são bilateral, noturna e exame normal; aí é explicar que é benigno e orientar os sinais de alerta.",
  "div": "desperta",
  "pega": "Dor de crescimento é <b>bilateral</b> e com <b>exame normal</b>; unilateral, em ponto fixo ou com limitação = <b>investigar</b>.",
  "z": "Dor nas duas pernas à noite, passa com massagem e a criança joga bola de dia: é dor de crescimento. Não precisa cintilografia, precisa de uma mãe com mão boa, caralho.",
  "ills": ["c_cresc"]},
 {"id": "c_membal", "t": "Membros: sinais de alerta, tumor ósseo × leucemia",
  "s": "Alertas: dor em <b>ponto fixo</b>, <b>unilateral</b>, alteração de <b>força ou marcha</b>, edema/calor articular, <b>sintomas sistêmicos</b> (febre, perda de peso, palidez), <b>sem resposta a analgésico</b>, dor progressiva. "
       "<br>Exames iniciais: hemograma, VHS/PCR, RX. "
       "<br><b>Tumor ósseo</b> (osteossarcoma, Ewing): dor <b>localizada</b>, sem sinais sistêmicos → RX e <b>biópsia</b>. "
       "<br><b>Leucemia</b>: dor <b>não localizada</b> + sistêmicos (prostração, palidez, perda de peso, hepatoesplenomegalia, adenomegalia) → hemograma (blastos/citopenias) → mielograma (gabarito 2025/2).",
  "fala": "A dor de membros vira alerta quando é num ponto fixo, de um lado só, quando mexe com força ou marcha, quando vem com febre, emagrecimento ou palidez, ou quando não melhora com analgésico. E caiu a diferença entre os dois cânceres: o tumor ósseo dá dor localizada, sem sintomas gerais; a leucemia dá dor difusa, mal localizada, com a criança prostrada, pálida e perdendo peso.",
  "pega": "Gabarito 2025/2: tumor ósseo = dor <b>localizada</b> sem sistêmicos; leucemia = dor <b>não localizada</b> + sistêmicos.",
  "z": "Dor num ponto só, que não passa com dipirona: radiografia nesse osso, agora. Dor difusa com criança pálida e magra: hemograma, porque pode ser leucemia, porra.",
  "ills": ["c_membal"]},
 {"id": "c_cefal", "t": "Cefaleia: primária (migrânea × tensional)",
  "s": "Cefaleia recorrente: ~<b>20%</b>, mais em meninas. <b>Primárias</b>: "
       "<br>• <b>Migrânea</b>: 1–72 h, pulsátil, pode ser unilateral ou bilateral na criança, <b>náusea/vômito, foto e fonofobia</b>, piora com atividade, história familiar. "
       "<br>• <b>Tensional</b>: <b>em aperto, bilateral</b>, 30 min–7 dias, sem náusea importante, <b>melhora com o sono</b>. "
       "<br>Secundárias ~<b>5%</b> (HAS, sinusite, HIC). <b>Sempre</b>: medir <b>PA</b> e <b>exame neurológico completo</b> com fundo de olho (slide 42).",
  "fala": "Cefaleia recorrente atinge cerca de uma em cada cinco crianças. Entre as primárias, a migrânea dura de uma a setenta e duas horas, é pulsátil, vem com náusea, vômito e aversão a luz e som; a tensional é em aperto, dos dois lados, e melhora com o sono. Só cerca de cinco por cento são secundárias, mas o slide manda sempre duas coisas em toda criança com cefaleia: medir a pressão e fazer exame neurológico completo, com fundo de olho.",
  "pega": "Exame indispensável (caiu): <b>pressão arterial + exame neurológico com fundo de olho</b>. Seio frontal não existe em &lt; 5 anos (não é sinusite frontal).",
  "z": "Criança com cefaleia e ninguém mediu a pressão? Então ninguém examinou a criança. Manguito e oftalmoscópio, caralho.",
  "m": [["MEDCURSO · S33 02:42–03:05", "Em menor de 5 anos o seio frontal ainda não existe."]],
  "ills": ["c_cefal"]},
 {"id": "c_cefal_al", "t": "Cefaleia: sinais de alarme (caiu 2×, 2,4 pts)",
  "s": "Sinais de alarme (slide 43): <b>alterações neurológicas</b> ou crises epilépticas · <b>alterações oculares</b> (edema de papila, anisocoria, nistagmo, estrabismo recente, diplopia, queda da acuidade) · <b>vômitos</b> persistentes/crescentes ou recentes · dor precipitada por <b>esforço, Valsalva ou mudança de postura</b> · <b>mudança de padrão</b> (frequência/intensidade crescentes) · <b>unilateral</b> fixa · <b>matinal</b> · <b>desperta a criança</b> · <b>desaceleração do crescimento</b> · <b>idade &lt; 5 anos</b>. "
       "<br>Vários alarmes, progressiva, matinal e noturna em &lt; 5 anos → <b>secundária</b> (HIC / processo expansivo) → neuroimagem.",
  "fala": "Os sinais de alarme da cefaleia são a questão mais pontuada desse capítulo. Decore: alteração neurológica ou convulsão, alteração ocular como edema de papila, estrabismo novo ou diplopia, vômitos que aumentam, dor que piora com esforço, tosse ou mudança de posição, mudança do padrão, dor sempre do mesmo lado, dor matinal, dor que acorda, crescimento que desacelera e idade abaixo de cinco anos. Com vários deles, é cefaleia secundária até prova em contrário.",
  "div": "unilat",
  "pega": "Na Camila (4 anos) os 4 alarmes do enunciado eram: <b>&lt; 5 anos</b>, <b>mudança de padrão</b>, <b>matinal</b>, <b>desperta</b>. Resposta: <b>secundária</b>.",
  "z": "Quatro anos, dor todo dia, pior de manhã e acordando de madrugada: isso não é enxaqueca, é cérebro pedindo ressonância. Secundária, porra.",
  "ills": ["c_cefal_al"]},
 {"id": "c_escala", "t": "Escalas de dor e diário",
  "s": "<b>Escala numérica 0–10</b> (com faces associadas) para crianças maiores; <b>escala de faces</b> para os pequenos. Usar junto com o <b>diário da dor</b> (frequência, duração, desencadeantes, o que alivia, faltas escolares).",
  "fala": "Para medir dor em criança, a aula traz a escala numérica de zero a dez, combinada com desenhos de faces, e a escala de faces sozinha para os menores, que ainda não entendem números. Ela rende mais quando vem junto com um diário da dor, onde a família anota frequência, duração, gatilhos, o que aliviou e quantas aulas a criança perdeu.",
  "pega": "Criança pequena → <b>escala de faces</b>; maior → <b>numérica 0–10</b>; sempre com <b>diário da dor</b>.",
  "z": "Perguntar “de zero a dez” pra criança de três anos dá sempre dez ou banana. Usa a escala de faces, caralho.",
  "ills": ["c_escala"]},
]

ILLS = {
 "c_geral": cards("Dor recorrente: a definição e os números", [
     ("3️⃣", "Definição", "≥ 3 episódios em ≥ 3 meses, interferindo nas atividades", "p"),
     ("🧠", "Cefaleia", "20,6% — a mais frequente", "v"),
     ("🦵", "Membros", "15,5%", "t"),
     ("🫃", "Abdominal", "14,4%", "a")],
     foot="Orgânicas: 10–15% · erros: “não é nada” × investigação extensa"),
 "c_abd": cards("Dor abdominal recorrente funcional (90–95%)", [
     ("🍽️", "Dispepsia funcional", "dor/desconforto epigástrico", "t"),
     ("🚽", "Intestino irritável", "dor que muda com a evacuação", "t"),
     ("🌀", "Enxaqueca abdominal", "crises paroxísticas, história familiar de migrânea", "p"),
     ("❔", "Não especificada", "dor periumbilical sem critério dos outros", "a")],
     foot="Sem alarme: ambulatório, explicar, orientar alertas, acompanhar", fcor="g"),
 "c_abdal": cards("Dor abdominal: sinais de alerta", [
     ("🌙", "Desperta a criança", "gabarito 2025/2", "r"),
     ("📍", "Periférica", "longe do umbigo · gabarito 2025/2", "r"),
     ("➡️", "Irradia", "costas, escápula, membros · gabarito 2025/2", "r"),
     ("📉", "Peso / crescimento", "perda de peso, desaceleração na curva", "a"),
     ("🤮", "Vômitos biliosos, sangue", "sangramento GI, diarreia noturna, disfagia", "a"),
     ("🧬", "História familiar", "DII, celíaca, úlcera péptica · lab alterado", "p")],
     foot="Nível 1: hemograma, VHS/PCR, urina + urocultura, parasitológico", fcor="t"),
 "c_cresc": cards("Dor de crescimento: os critérios", [
     ("🎂", "6–13 anos", "membros: dor recorrente 4–10 anos", "p"),
     ("↔️", "Bilateral", "coxa anterior, poplítea, panturrilha", "t"),
     ("🌙", "Fim da tarde / noite", "crises de 10–15 min, pode acordar", "v"),
     ("✅", "Exame normal", "melhora com calor, massagem, analgésico", "g")],
     foot="Unilateral, ponto fixo ou limitação → não é dor de crescimento"),
 "c_membal": versus("Dor óssea: tumor ósseo × leucemia", ("🦴", "Tumor ósseo", "a", [
     "✔ dor localizada, ponto fixo", "✔ sem sinais sistêmicos", "• osteossarcoma 10–19 a (joelho)", "• Ewing 10–15 a", "• RX → biópsia"]),
     ("🩸", "Leucemia", "r", [
     "✔ dor não localizada", "✔ palidez, prostração, perda de peso", "✔ hepatoesplenomegalia, gânglios", "• hemograma: blastos / citopenias", "• mielograma confirma"]),
     foot="Alarme em membros: unilateral, ponto fixo, força/marcha, sistêmicos, sem resposta a analgésico"),
 "c_cefal": versus("Cefaleia primária", ("🌩️", "Migrânea", "p", [
     "• 1–72 h, pulsátil", "• náusea / vômito", "• foto e fonofobia", "• piora com atividade", "• história familiar"]),
     ("🗜️", "Tensional", "t", [
     "• em aperto, bilateral", "• 30 min a 7 dias", "• sem náusea importante", "• melhora com o sono", "• estresse"]),
     foot="SEMPRE: pressão arterial + exame neurológico com fundo de olho"),
 "c_cefal_al": cards("Cefaleia: sinais de alarme (slide 43)", [
     ("🧠", "Neurológico", "déficit, convulsão, alteração de marcha", "r"),
     ("👁️", "Ocular", "papiledema, anisocoria, estrabismo novo, diplopia", "r"),
     ("🤮", "Vômitos", "persistentes, crescentes ou recentes", "r"),
     ("🏋️", "Esforço / postura", "Valsalva, tosse, mudança de posição", "a"),
     ("📈", "Mudança de padrão", "mais frequente, mais intensa", "a"),
     ("🌅", "Matinal / desperta", "dor ao acordar ou que acorda", "a"),
     ("📍", "Unilateral fixa", "sempre do mesmo lado", "p"),
     ("👶", "< 5 anos / crescimento", "idade < 5 anos · desaceleração da curva", "p")],
     foot="Vários alarmes → secundária (HIC / processo expansivo)"),
 "c_escala": versus("Medir a dor da criança", ("😀", "Escala de faces", "a", [
     "• pré-escolares", "• aponta a carinha", "• com diário da dor"]),
     ("🔟", "Numérica 0–10", "t", [
     "• escolares e adolescentes", "• associada às faces", "• com diário da dor"]),
     foot="Diário: frequência, duração, gatilho, alívio, faltas escolares", fcor="p"),
}

QMAP = {0: ["c_geral", "c_abd"], 1: ["c_abdal"], 2: ["c_cresc"], 3: ["c_cefal_al", "c_cefal"]}

DIV = {
 "organ": ["Percentual de causa orgânica", "Slide 8: global <b>10–15%</b>", "Slides 15/25/41: abdominal 5–10%, membros 3–4%, cefaleia 5%",
           "Os parciais não somam o global: escreva <b>10–15% orgânicas</b> no geral e o % do tipo quando a pergunta for específica"],
 "desperta": ["“Desperta a criança”", "Slides 22 e 43: dor que desperta = <b>sinal de alerta</b>", "Slide 27: dor de crescimento <b>pode acordar</b> a criança",
              "Contradição do material: na dor de crescimento, acordar é aceitável <b>se bilateral e exame normal</b>; na abdominal e na cefaleia, acordar é <b>alarme</b>"],
 "unilat": ["Cefaleia unilateral", "Slide 43: unilateral = <b>alarme</b>", "Slide 38: migrânea pode ser unilateral",
            "Alarme é a dor <b>sempre do mesmo lado</b> (fixa); migrânea que alterna lados não é alarme"],
}

FLASH = [
 [3, "Definição de dor recorrente?", "≥ 3 episódios em ≥ 3 meses, interferindo nas atividades."],
 [3, "Dor recorrente mais frequente?", "Cefaleia (20,6%)."],
 [3, "% funcional na dor abdominal recorrente?", "90–95%."],
 [3, "4 tipos de dor abdominal funcional?", "Dispepsia, intestino irritável, enxaqueca abdominal, não especificada."],
 [3, "3 alertas da dor abdominal no gabarito 2025/2?", "Desperta, localização periférica, irradiação."],
 [3, "Exames de nível 1 na dor abdominal com alerta?", "Hemograma, VHS/PCR, urina/urocultura, parasitológico."],
 [3, "Parâmetro mais sensível a doença orgânica?", "Peso (queda na curva)."],
 [3, "Dor de crescimento: idade?", "6–13 anos."],
 [3, "3 critérios para dor de crescimento?", "Bilateral, fim da tarde/noite, exame físico normal (melhora com massagem)."],
 [3, "Tumor ósseo × leucemia: a dor?", "Tumor: localizada, sem sistêmicos. Leucemia: difusa + sistêmicos."],
 [3, "Migrânea × tensional?", "Migrânea: pulsátil, náusea, foto/fonofobia. Tensional: aperto bilateral, melhora com sono."],
 [3, "Exame indispensável na cefaleia?", "Pressão arterial + exame neurológico com fundo de olho."],
 [3, "Cefaleia: alarme pela idade?", "< 5 anos."],
 [3, "Cite 6 alarmes de cefaleia.", "Neurológico, ocular, vômitos, Valsalva/postura, mudança de padrão, matinal/desperta (+ unilateral fixa, desaceleração)."],
 [3, "Seio frontal em < 5 anos?", "Não existe — não é sinusite frontal."],
]

COLA = [["Cap. 3 · Dores recorrentes", [
 ["Definição", "≥ 3 episódios · ≥ 3 meses · interfere"], ["Prevalência", "cefaleia 20,6 · membros 15,5 · abdome 14,4%"],
 ["Orgânicas", "10–15% (abdome 5–10 · membros 3–4 · cefaleia 5)"], ["Abdominal funcional", "90–95%"],
 ["Alerta abdome", "desperta · periférica · irradia · peso ↓"], ["Nível 1", "hemograma · VHS/PCR · urina · EPF"],
 ["Dor de crescimento", "6–13 a · bilateral · noite · exame normal"], ["Tumor ósseo", "localizada → RX → biópsia"],
 ["Leucemia", "difusa + sistêmicos → hemograma → mielograma"], ["Cefaleia sempre", "PA + neuro + fundo de olho"],
 ["Alarme cefaleia", "< 5 a · matinal · desperta · padrão muda · vômitos · neuro/ocular"]]]]

KS = [
 {"id": "k_c_cef", "cap": 3, "blk": ["c_cefal_al", "c_cefal"], "t": "A cefaleia da Camila (caiu 2×, 2,4 pts)",
  "src": "Prova A1 (7 pts) · Q1 alta taxonomia — Profa. Patrícia",
  "enun": "Camila, 4 anos, cefaleia recorrente há mais de 2 meses. No início, ~2×/semana; agora <b>diária</b> e <b>principalmente pela manhã</b>. Em alguns dias <b>acorda no meio da noite</b> pela dor.",
  "p": [{"p": "Cite 4 dados do enunciado que são sinais de alarme. (0,8)",
         "m": "<b>Idade &lt; 5 anos</b> · <b>mudança de padrão</b> (aumento de frequência) · <b>cefaleia matinal</b> · <b>desperta a criança</b>.",
         "c": ["menor de 5 anos", "mudança de padrão", "matinal", "desperta"]},
        {"p": "Cite outros 4 sinais de alarme não citados. (0,8)",
         "m": "Alterações neurológicas ou crises epilépticas · alterações oculares (edema de papila, anisocoria, nistagmo, estrabismo recente, diplopia, queda da acuidade) · vômitos persistentes/crescentes · dor precipitada por esforço, Valsalva ou mudança de postura · cefaleia unilateral · desaceleração do crescimento.",
         "c": ["neurológicas", "oculares", "vômitos", "Valsalva", "unilateral", "desaceleração do crescimento"]},
        {"p": "Quais dados são indispensáveis no exame físico? (0,4)",
         "m": "<b>Pressão arterial</b> e <b>exame neurológico completo</b>, incluindo <b>fundo de olho</b> (“sempre”, slide 42).",
         "c": ["pressão arterial", "exame neurológico", "fundo de olho"]},
        {"p": "Primária ou secundária? Justifique. (0,4)",
         "m": "<b>Secundária</b> (suspeita de hipertensão intracraniana / processo expansivo): múltiplos alarmes, padrão progressivo, matinal e noturno em criança &lt; 5 anos → neuroimagem.",
         "c": ["secundária", "hipertensão intracraniana", "processo expansivo", "múltiplos sinais de alarme", "neuroimagem"]}]},
 {"id": "k_c_abd", "cap": 3, "blk": ["c_abdal", "c_abd"], "t": "Sinais de alerta da dor abdominal (2025/2)",
  "src": "Prova 2025/2 · Q1 — gabarito mínimo oficial",
  "enun": "Menino de 8 anos com dor abdominal periumbilical recorrente há 6 meses, 2 vezes por semana, faltando à escola. A mãe quer saber quando deve se preocupar.",
  "p": [{"p": "Essa dor preenche o critério de dor recorrente? Justifique.",
         "m": "Sim: <b>≥ 3 episódios</b> em <b>≥ 3 meses</b>, com intensidade que <b>interfere nas atividades</b> (faltas escolares).",
         "c": ["3 episódios", "3 meses", "interfere nas atividades"]},
        {"p": "Cite os sinais de alerta da dor abdominal recorrente.",
         "m": "Gabarito oficial: <b>dor que repetidamente desperta a criança</b>; <b>dor de localização periférica</b>; <b>dor que irradia</b> para costas, escápula ou membros inferiores. Acrescentar: perda de peso/desaceleração do crescimento, febre recorrente, vômitos biliosos, visceromegalias/massas, sangramento, história familiar (DII, celíaca, péptica), alteração de VHS/PCR/hemograma/urina.",
         "c": ["desperta", "periférica", "irradia", "perda de peso", "vômitos biliosos", "sangramento", "história familiar"]},
        {"p": "Sem sinais de alerta, qual a conduta?",
         "m": "<b>Abordagem ambulatorial</b>: anamnese com criança e pais separados, estressores, diário da dor, explicar a natureza funcional (90–95%), <b>orientar os sinais de alerta</b> e acompanhar; evitar “não é nada” e investigação extensa.",
         "c": ["ambulatorial", "funcional", "orientar sinais de alerta", "acompanhar", "evitar investigação extensa"]}]},
 {"id": "k_c_cresc", "cap": 3, "blk": ["c_cresc", "c_geral"], "t": "O irmão com dor nas pernas à noite",
  "src": "Prova A1 (7 pts) · versão longa da Q1 de adenomegalia — Profa. Patrícia",
  "enun": "O irmão de 7 anos de uma criança atendida por adenite refere dor nas pernas à noite, algumas vezes por semana, há 4 meses. Brinca normalmente durante o dia.",
  "p": [{"p": "Quais os critérios de dor recorrente?",
         "m": "<b>≥ 3 episódios</b> de dor, com intensidade que <b>interfere nas atividades habituais</b>, num período de <b>≥ 3 meses</b>.",
         "c": ["3 episódios", "3 meses", "interfere nas atividades"]},
        {"p": "Cite 3 critérios para suspeitar de dor de crescimento.",
         "m": "<b>6–13 anos</b> · dor intensa <b>bilateral</b> em MMII (coxa anterior, poplítea, panturrilha) · crises de 10–15 min no <b>fim da tarde/noite</b>, podendo acordar · difícil de localizar · sem outras queixas e <b>exame normal</b> · melhora com calor, massagem, analgésico.",
         "c": ["6 a 13 anos", "bilateral", "noite", "exame normal", "massagem"]}]},
]
