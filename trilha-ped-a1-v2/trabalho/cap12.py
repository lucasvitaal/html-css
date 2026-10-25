CAP = {"n": 12, "t": "Refluxo gastroesofágico", "short": "RGE", "aula": "Aula 12 · slides da Patrícia",
       "icon": "🍼", "col": "#1E5E6E",
       "bul": ["RGE fisiológico = “regurgitador feliz”: bom ganho, sem complicações",
               "DRGE = RGE + complicações esofágicas ou extraesofágicas",
               "Não há exame ideal: cada indicação, um exame (pHmetria = relação sintoma)",
               "Lactente: supino, espessar, evitar overfeeding; IBP só com indicação"],
       "medalha": ["🍼", "Regurgitador feliz"]}

BLOCKS = [
 {"id": "l_def", "t": "Regurgitação, vômito, RGE e DRGE", "slides": ["L3", "L5", "L6", "L7", "L8"],
  "s": "Muito frequente, preocupa a família e leva a <b>intervenções desnecessárias</b>. "
       "<br><b>Regurgitação</b>: retorno involuntário · <b>vômito</b>: expulsão ativa · <b>RGE</b>: processo <b>normal, fisiológico, autolimitado</b> · <b>DRGE</b>: RGE + <b>complicações</b> esofágicas e extraesofágicas (tosse, broncoespasmo, laringites…). "
       "<br>Esôfago: transporte + prevenção do retorno (<b>esfíncter esofágico inferior</b>). "
       "<br>Fisiológico = <b>lactentes</b>; DRGE = crianças maiores e <b>grupos de risco</b>: <b>neuropatas</b>, operados de <b>atresia de esôfago</b>, pneumopatias crônicas (<b>fibrose cística</b>), <b>obesidade</b>.",
  "fala": "Separe as palavras: regurgitação é o retorno involuntário, vômito é a expulsão ativa. Refluxo gastroesofágico é um processo normal, fisiológico e autolimitado, típico do lactente. Doença do refluxo é quando esse refluxo traz complicações, no esôfago ou fora dele, como tosse, broncoespasmo e laringite. Os grupos de risco para doença do refluxo são neuropatas, operados de atresia de esôfago, pneumopatas crônicos como na fibrose cística, e obesos.",
  "pega": "RGE = <b>fisiológico</b>; DRGE = RGE <b>+ complicação</b>. Grupos de risco: <b>neuropata, atresia de esôfago, fibrose cística, obesidade</b>.",
  "z": "Bebê que golfa e engorda bem não tem doença, tem estômago pequeno e mãe preocupada. Não trata a mãe com omeprazol no filho, porra.",
  "ills": ["l_def"]},
 {"id": "l_feliz", "t": "RGE fisiológico: o regurgitador feliz", "slides": ["L9"],
  "s": "<b>“Regurgitador feliz”</b>: <b>bom ganho ponderal</b>, <b>ausência de complicações</b>. "
       "<br>Raramente <b>antes de 3 semanas</b> e <b>depois de 6 meses</b> (início); mais evidente entre <b>2–4 meses</b>, pico aos <b>4–5 meses</b>. "
       "<br><b>4 meses: até 67%</b> dos lactentes regurgitam · <b>1 ano: só 1%</b> persiste. "
       "<br>Conduta: <b>tranquilizar</b>, manter aleitamento, sem exames nem medicação.",
  "fala": "O regurgitador feliz é o lactente que golfa várias vezes ao dia mas ganha peso bem e não tem nenhuma complicação. As regurgitações aparecem entre duas semanas e seis meses, ficam mais evidentes entre dois e quatro meses, com pico aos quatro ou cinco. Aos quatro meses até sessenta e sete por cento dos bebês regurgitam; com um ano, só um por cento. A conduta é tranquilizar, sem exame e sem remédio.",
  "pega": "Marcos com <b>ganho de peso normal</b> e sem sintomas = <b>RGE fisiológico</b> → tranquilizar (caiu em prova antiga).",
  "z": "Sessenta e sete por cento dos bebês de quatro meses golfam. Se todo mundo golfa, golfar não é doença: é ser bebê, caralho.",
  "ills": ["l_feliz"]},
 {"id": "l_drge", "t": "DRGE: as complicações que definem a doença", "slides": ["L10"],
  "s": "<b>DRGE = RGE + complicações</b>: "
       "<br>• desconforto, <b>choro, irritabilidade</b>, sono agitado · <b>desaceleração ou perda de peso</b> · halitose, erosões dentárias · dor epigástrica, azia · <b>hematêmese, melena</b>, sangue oculto · "
       "<br>• extraesofágicas: <b>tosse persistente, broncoespasmo, asma</b> · rouquidão, odinofagia · <b>apneia, cianose</b> · pneumonias de aspiração, sinusites e otites de repetição · laringites de repetição · <b>ALTE</b> (evento com aparente risco de vida). "
       "<br>Complicação crônica: <b>esôfago de Barrett</b> e adenocarcinoma de esôfago.",
  "fala": "A doença do refluxo é definida pelas complicações. Do lado digestivo: choro e irritabilidade, desaceleração ou perda de peso, azia, erosão dentária, hematêmese e melena. Do lado de fora do esôfago: tosse persistente, broncoespasmo e asma, rouquidão, apneia e cianose, pneumonias aspirativas, otites e sinusites de repetição, e os eventos com aparente risco de vida. No longo prazo, esôfago de Barrett e adenocarcinoma.",
  "pega": "Regurgitação <b>com perda de peso</b>, sangramento ou sintoma respiratório = <b>DRGE</b>, não fisiológico.",
  "z": "Refluxo que faz o bebê parar de ganhar peso, chiar ou ficar roxo não é golfada fofa, é doença do refluxo. Aí investiga, porra.",
  "ills": ["l_drge"]},
 {"id": "l_dif", "t": "Diagnóstico diferencial e sinais de outro diagnóstico", "slides": ["L11", "L12", "L13"],
  "s": "Diferenciais no lactente: <b>alergia à proteína do leite de vaca</b>, <b>cólicas</b>, malformações (RN): <b>estenose hipertrófica de piloro</b>, <b>má rotação intestinal</b>. "
       "<br><b>História e exame físico bastam na maioria</b>: história alimentar (frequência, quantidade, tipo, mudanças, posição) e <b>curva ponderal</b>. "
       "<br><b>Sinais de outro diagnóstico</b>: febre, letargia, dor excessiva, <b>falha de crescimento</b>, disúria, <b>vômitos que começam após 6 meses ou persistem após 12</b> · neurológicos: <b>fontanela tensa</b>, macro/microcefalia, convulsões · GI: <b>vômitos biliosos</b>, vômitos persistentes com perda de peso, noturnos, hematêmese/melena, diarreia crônica, distensão, sangramento retal.",
  "fala": "Antes de falar em refluxo, pense no que imita: alergia à proteína do leite de vaca, cólica e, no recém-nascido, estenose hipertrófica de piloro e má rotação intestinal. Na maioria, história e curva de peso bastam. Desconfie de outro diagnóstico se houver febre, letargia, falha de crescimento, vômito que começa depois dos seis meses ou persiste após um ano, fontanela tensa, convulsão, vômito bilioso ou sangramento.",
  "pega": "<b>Vômito bilioso</b> = má rotação até prova em contrário (não é refluxo). Início <b>após 6 meses</b> ou persistência <b>após 12</b> = outro diagnóstico.",
  "z": "Vômito verde em recém-nascido não é refluxo, é intestino torcido: cirurgia pediátrica agora, caralho.",
  "ills": ["l_dif"]},
 {"id": "l_exames", "t": "Exames: não existe exame ideal", "slides": ["L14", "L15", "L16", "L17", "L18", "L19"],
  "s": "<b>Não há exame ideal</b>: <b>cada indicação, um exame</b>. "
       "<br>• <b>REED</b> (seriografia): não diagnostica nem quantifica RGE; útil para <b>anormalidades anatômicas</b>. "
       "<br>• <b>Cintilografia</b>: RGE pós-prandial imediato, detecta aspiração (negativo não descarta) — não indicada em pediatria. "
       "<br>• <b>USG</b>: diagnóstico de <b>estenose hipertrófica de piloro</b>; não para DRGE. "
       "<br>• <b>pHmetria de 24 h</b>: <b>associação dos episódios com sintomas</b>, refluxo ácido. "
       "<br>• <b>Endoscopia + biópsia</b>: <b>complicações</b> (esofagite, Barrett). "
       "<br>• <b>Impedâncio-pHmetria</b>: melhor (ácido ou não), parâmetros pediátricos incertos. <b>Manometria</b>: motilidade (disfagia).",
  "fala": "Não existe exame ideal para refluxo: cada pergunta tem o seu exame. O raio-x contrastado de esôfago, estômago e duodeno não diagnostica refluxo, mas mostra anatomia. O ultrassom é para estenose de piloro. A pHmetria de vinte e quatro horas relaciona os episódios de refluxo com os sintomas, como tosse ou apneia. A endoscopia com biópsia mostra complicações. A impedâncio-pHmetria é a melhor, mas ainda sem valores bem definidos para crianças.",
  "pega": "Principal indicação da <b>pHmetria</b>: relacionar refluxo com <b>sintomas atípicos/extraesofágicos</b> (caiu em prova antiga). REED <b>não</b> diagnostica RGE.",
  "z": "Pedir seriografia pra provar refluxo é como fotografar o mar pra provar que tem onda: mostra a anatomia, não o refluxo. pHmetria, porra.",
  "ills": ["l_exames"]},
 {"id": "l_geral", "t": "Tratamento: medidas gerais", "slides": ["L20", "L21", "L22"],
  "s": "Tratamento <b>individualizado</b> (RGE × DRGE, lactente × criança maior). Objetivos na DRGE: aliviar sintomas, crescimento normal, tratar/prevenir esofagite e complicações. "
       "<br>Etapas: <b>1) medidas gerais</b> → 2) medicamentos → 3) cirurgia. "
       "<br><b>Posição</b>: <b>supina para lactentes</b> · decúbito lateral esquerdo com cabeceira elevada para crianças maiores. "
       "<br><b>Alimentação</b>: <b>espessar fórmulas</b> nos lactentes · <b>evitar overfeeding</b> · <b>teste com hidrolisado proteico 2–4 semanas</b> (vômitos recorrentes → APLV) · perder peso nos obesos · crianças maiores: evitar gordura, café, refrigerante, chá e chocolate · <b>evitar tabagismo passivo</b> (relaxa o EEI).",
  "fala": "O tratamento começa pelas medidas gerais. Lactente dorme em posição supina, de barriga para cima; criança maior pode ficar em decúbito lateral esquerdo com cabeceira elevada. No lactente, espessa a fórmula, evita oferecer volume demais e, se vomita muito, testa por duas a quatro semanas uma fórmula com proteína hidrolisada, pensando em alergia ao leite de vaca. Na criança maior, menos gordura, café, refrigerante e chocolate, e ninguém fumando perto.",
  "pega": "Lactente: <b>supino</b> (não elevar a cama/decúbito ventral — o compilado errou). Hidrolisado <b>2–4 semanas</b> = teste para <b>APLV</b>.",
  "z": "Colocar o bebê de bruços pra golfar menos troca refluxo por morte súbita. Barriga pra cima, caralho.",
  "ills": ["l_geral"]},
 {"id": "l_med", "t": "Medicamentos e cirurgia", "slides": ["L23", "L24", "L25", "L26"],
  "s": "Medicação só no <b>RGE patológico</b>, com bom senso. "
       "<br>• <b>Antiácidos/alginatos</b>: sem estudos de eficácia em pediatria · <b>sucralfato</b>: protege a mucosa. "
       "<br>• <b>Procinéticos</b> (bromoprida, domperidona, metoclopramida): <b>não indicados de rotina</b> — efeitos no SNC &gt; benefícios. "
       "<br>• <b>Anti-H2</b>: ranitidina <b>suspensa desde 2019</b>. "
       "<br>• <b>IBP</b> (omeprazol, esomeprazol): superiores aos anti-H2; uso criterioso (hipocloridria, microbiota). Indicações: <b>esofagite erosiva, estenose péptica, Barrett</b>, RGE + <b>doença respiratória crônica</b> ou <b>neurológicos</b>; teste terapêutico em crianças maiores <b>4–8 semanas</b>, retirada gradual (rebote). "
       "<br><b>Cirurgia</b>: <b>fundoplicatura de Nissen</b> — déficits neurológicos, estenoses pépticas, Barrett.",
  "fala": "Remédio só no refluxo patológico. Procinéticos como bromoprida, domperidona e metoclopramida não são de rotina, porque os efeitos no sistema nervoso superam os benefícios. A ranitidina foi suspensa em dois mil e dezenove. O inibidor de bomba de prótons, como o omeprazol, é o mais eficaz, indicado na esofagite erosiva, estenose péptica, Barrett, ou refluxo com doença respiratória crônica ou neurológica; teste de quatro a oito semanas na criança maior e retirada gradual. A cirurgia é a fundoplicatura de Nissen.",
  "pega": "Procinético <b>não</b> é rotina; ranitidina <b>suspensa</b>; IBP com <b>indicação</b> (esofagite, Barrett, respiratório, neuro). Cirurgia: <b>Nissen</b>.",
  "z": "Omeprazol para regurgitador feliz é o remédio mais caro pra tratar ansiedade materna. Só com indicação, porra.",
  "ills": ["l_med"]},
]

ILLS = {
 "l_def": versus("RGE × DRGE", ("😊", "RGE fisiológico", "g", [
     "• processo normal, autolimitado", "• lactentes", "• sem complicações", "• tranquilizar"]),
     ("⚠️", "DRGE", "r", [
     "• RGE + complicações", "• esofágicas e extraesofágicas", "• crianças maiores e grupos de risco", "• neuropata, atresia de esôfago, FC, obeso"])),
 "l_feliz": flow("O regurgitador feliz", [
     ("📅", "Início", "raro antes de 3 semanas e depois de 6 meses", "t"),
     ("📈", "Pico", "mais evidente 2–4 meses, pico 4–5 meses", "a"),
     ("👶", "4 meses", "até 67% regurgitam", "v"),
     ("🎂", "1 ano", "só 1% persiste", "g")],
     foot="Bom ganho de peso + sem complicações → tranquilizar, sem exames", fcor="g"),
 "l_drge": cards("DRGE: complicações", [
     ("😭", "Choro, irritabilidade", "sono agitado, desconforto", "a"),
     ("📉", "Peso", "desaceleração ou perda", "r"),
     ("🩸", "Sangramento", "hematêmese, melena, sangue oculto", "r"),
     ("🫁", "Respiratório", "tosse, broncoespasmo, asma, pneumonia aspirativa", "p"),
     ("😶", "Via aérea alta", "rouquidão, laringites, otites, sinusites", "t"),
     ("🚨", "Apneia, cianose, ALTE", "crônico: Barrett e adenocarcinoma", "v")]),
 "l_dif": cards("Sinais de outro diagnóstico", [
     ("🌡️", "Gerais", "febre, letargia, falha de crescimento, disúria", "a"),
     ("📆", "Tempo", "início após 6 meses ou persistência após 12", "a"),
     ("🧠", "Neurológicos", "fontanela tensa, macro/microcefalia, convulsões", "p"),
     ("💚", "Gastrointestinais", "vômito bilioso, hematêmese, distensão, diarreia crônica", "r")],
     foot="Diferenciais: APLV, cólica, estenose de piloro, má rotação", fcor="t"),
 "l_exames": table("Cada indicação, um exame", [
     ("REED", "anatomia — não diagnostica RGE"),
     ("Cintilografia", "pós-prandial, aspiração — não indicada"),
     ("USG", "estenose hipertrófica de piloro"),
     ("pHmetria 24 h", "relação refluxo × sintomas (ácido)"),
     ("Endoscopia + biópsia", "complicações: esofagite, Barrett"),
     ("Impedâncio-pHmetria", "melhor (ácido ou não), parâmetros incertos"),
     ("Manometria", "motilidade (disfagia)")], cor="t", kw=190),
 "l_geral": versus("Medidas gerais", ("👶", "Lactente", "t", [
     "• posição supina", "• espessar fórmula", "• evitar overfeeding", "• hidrolisado 2–4 sem se vômitos (APLV)"]),
     ("🧒", "Criança maior", "a", [
     "• decúbito lateral esquerdo", "• cabeceira elevada", "• sem gordura, café, refri, chá, chocolate", "• perder peso se obeso"]),
     foot="Todos: evitar tabagismo passivo (relaxa o EEI)", fcor="p"),
 "l_med": flow("Medicamentos e cirurgia", [
     ("🧴", "Antiácidos, alginatos, sucralfato", "sem evidência em pediatria / protege mucosa", "t"),
     ("🚫", "Procinéticos", "não de rotina — efeitos no SNC > benefícios", "r"),
     ("⛔", "Ranitidina", "suspensa desde 2019", "r"),
     ("💊", "IBP (omeprazol)", "esofagite erosiva, estenose, Barrett, respiratório ou neuro · teste 4–8 sem", "g"),
     ("🔪", "Fundoplicatura de Nissen", "neuropatas, estenose péptica, Barrett", "v")]),
}

QMAP = {}

Q = [
 {"id": "qa_rge", "cap": 12, "src": "antiga", "orig": "Prova A1 (7 pts) · Q6 — Profa. Patrícia", "tag": "prova antiga · regurgitador", "slides": ["L9"],
  "enun": "Marcos, 2 meses, aleitamento exclusivo, regurgita várias vezes ao dia; ganhou peso bem (3.200 → 4.800 g), dorme bem, sem irritabilidade, engasgos ou sintomas respiratórios. Qual a conduta?",
  "alts": ["Omeprazol por 4 semanas.", "pHmetria de 24 horas.", "Tranquilizar a mãe, manter aleitamento exclusivo, sem exames nem medicação.", "Trocar por fórmula espessada e decúbito ventral."], "ok": 2,
  "coment": "<b>C.</b> <b>RGE fisiológico</b> (“regurgitador feliz”): bom ganho, sem complicações; 67% regurgitam aos 4 meses e só 1% com 1 ano. <b>A/B</b>: sem indicação. <b>D</b>: desmamar é erro e lactente dorme <b>supino</b>.",
  "blk": ["l_feliz"]},
 {"id": "ql_ph", "cap": 12, "src": "antiga", "orig": "Prova A1 antiga · DRGE/pHmetria", "tag": "prova antiga · pHmetria", "slides": ["L16", "L19"],
  "enun": "Qual a principal indicação da pHmetria esofágica de 24 horas na criança, segundo a aula?",
  "alts": ["Diagnosticar estenose hipertrófica de piloro.", "Avaliar a associação dos episódios de refluxo com os sintomas (ex.: tosse, apneia).", "Detectar esôfago de Barrett.", "Avaliar anormalidades anatômicas."], "ok": 1,
  "coment": "<b>B.</b> pHmetria avalia a <b>relação RGE × sintomas</b> e o refluxo ácido. <b>A</b>: USG. <b>C</b>: endoscopia com biópsia. <b>D</b>: REED.",
  "blk": ["l_exames"]},
 {"id": "ql_ibp", "cap": 12, "src": "autoral", "orig": "Autoral · slides L24–L26", "tag": "IBP", "slides": ["L25"],
  "enun": "Sobre o tratamento medicamentoso da DRGE em pediatria, segundo a aula, é correto:",
  "alts": ["Procinéticos são indicados de rotina.", "Ranitidina é a primeira escolha.", "IBP é indicado em esofagite erosiva, estenose péptica, Barrett ou RGE com doença respiratória crônica/neurológica.", "Todo lactente que regurgita deve receber omeprazol."], "ok": 2,
  "coment": "<b>C.</b> Slide 25. <b>A</b>: efeitos no SNC superam benefícios. <b>B</b>: suspensa desde 2019. <b>D</b>: regurgitador feliz não recebe medicação.",
  "blk": ["l_med"]},
 {"id": "ql_bil", "cap": 12, "src": "autoral", "orig": "Autoral · slides L11, L13", "tag": "sinais de outro diagnóstico", "slides": ["L13"],
  "enun": "Qual achado num lactente que vomita afasta a hipótese de RGE fisiológico e exige investigação de outra causa?",
  "alts": ["Regurgitação após as mamadas com bom ganho de peso.", "Vômitos biliosos.", "Pico das regurgitações aos 4 meses.", "Regurgitação que melhora com a idade."], "ok": 1,
  "coment": "<b>B.</b> Vômito bilioso é sinal gastrointestinal de outro diagnóstico (má rotação). As demais descrevem o regurgitador feliz.",
  "blk": ["l_dif"]},
]

FLASH = [
 [12, "RGE × DRGE?", "RGE: fisiológico, autolimitado. DRGE: RGE + complicações."],
 [12, "Grupos de risco para DRGE?", "Neuropatas, operados de atresia de esôfago, fibrose cística, obesos."],
 [12, "Regurgitador feliz: % aos 4 meses e com 1 ano?", "Até 67%; 1%."],
 [12, "Pico das regurgitações?", "4–5 meses."],
 [12, "Diferenciais do RGE no lactente?", "APLV, cólica, estenose de piloro, má rotação."],
 [12, "Início de vômitos que sugere outro diagnóstico?", "Após 6 meses (ou persistência após 12)."],
 [12, "Exame ideal para RGE?", "Não existe: cada indicação, um exame."],
 [12, "pHmetria serve para?", "Relacionar refluxo com sintomas (ácido)."],
 [12, "USG no vômito do lactente?", "Estenose hipertrófica de piloro."],
 [12, "Posição do lactente com RGE?", "Supina."],
 [12, "Teste com hidrolisado?", "2–4 semanas nos vômitos recorrentes (APLV)."],
 [12, "Procinéticos?", "Não de rotina (SNC)."],
 [12, "Indicações de IBP?", "Esofagite erosiva, estenose péptica, Barrett, RGE + respiratório crônico ou neuro."],
 [12, "Cirurgia?", "Fundoplicatura de Nissen."],
]

COLA = [["Cap. 12 · RGE", [
 ["RGE", "fisiológico · regurgitador feliz"], ["DRGE", "RGE + complicações"], ["4 meses / 1 ano", "67% / 1%"],
 ["Pico", "4–5 meses"], ["Outro diagnóstico", "bilioso · início > 6 m · persiste > 12 m"], ["pHmetria", "refluxo × sintomas"],
 ["Endoscopia", "complicações"], ["USG", "estenose de piloro"], ["Lactente", "supino · espessar · sem overfeeding"],
 ["Hidrolisado", "2–4 sem (APLV)"], ["IBP", "teste 4–8 sem · retirada gradual"], ["Cirurgia", "Nissen"]]]]

KS = [
 {"id": "k_l_rge", "cap": 12, "blk": ["l_feliz", "l_exames", "l_geral"], "t": "Marcos regurgita (prova antiga)",
  "src": "Prova A1 (7 pts) · Q6 e questão de pHmetria — Profa. Patrícia",
  "enun": "Marcos, 2 meses, aleitamento exclusivo, regurgita várias vezes ao dia; ganhou peso bem (3.200 → 4.800 g), dorme bem, sem irritabilidade, engasgos ou sintomas respiratórios.",
  "p": [{"p": "Qual o diagnóstico e a conduta?",
         "m": "<b>RGE fisiológico</b> (“regurgitador feliz”): bom ganho ponderal e sem complicações. <b>Tranquilizar</b> a mãe, manter <b>aleitamento exclusivo</b>, <b>sem exames nem medicação</b>; posição <b>supina</b>; melhora com o tempo (67% regurgitam aos 4 meses, 1% com 1 ano).",
         "c": ["RGE fisiológico", "regurgitador feliz", "ganho de peso", "tranquilizar", "aleitamento", "sem exames", "supina"]},
        {"p": "Qual a principal indicação de pHmetria na DRGE?",
         "m": "Avaliar a <b>associação dos episódios de refluxo com os sintomas</b>, sobretudo <b>atípicos/extraesofágicos</b> (tosse, apneia, broncoespasmo); refluxo ácido. Não é necessária no RGE típico.",
         "c": ["associação", "sintomas", "extraesofágicos", "refluxo ácido"]},
        {"p": "Que achados mudariam o diagnóstico para DRGE?",
         "m": "Complicações: <b>perda ou desaceleração de peso</b>, choro/irritabilidade, <b>hematêmese/melena</b>, tosse, broncoespasmo, <b>apneia/cianose</b>, pneumonias aspirativas, otites/laringites de repetição.",
         "c": ["perda de peso", "irritabilidade", "hematêmese", "tosse", "apneia", "pneumonia"]}]},
]
