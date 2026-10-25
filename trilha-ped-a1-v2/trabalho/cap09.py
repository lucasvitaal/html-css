CAP = {"n": 9, "t": "Infecção do trato urinário", "short": "ITU", "aula": "Aula 9 · slides da Patrícia",
       "icon": "🚽", "col": "#1E5E6E",
       "bul": ["Investigação após ITU febril: caiu 2× — USG, UCM (RVU) e DMSA (cicatriz)",
               "E. coli 80–90% · RN = ITU complicada → internar",
               "Piúria ≥ 5/campo · urocultura ≥ 100.000 · 10–100 mil repetir",
               "Antibiótico logo após colher · profilaxia não evita cicatriz"],
       "medalha": ["🚽", "Jato médio perfeito"]}

BLOCKS = [
 {"id": "i_conc", "t": "Conceito, epidemiologia e agentes",
  "s": "ITU = <b>germe único</b> + inflamação <b>sintomática</b> do trato urinário. Até 7 anos: <b>8% das meninas</b>, &lt; 2% dos meninos. Recorrência <b>30% em 1 ano</b>, 50% em 5 anos. "
       "<br>Via <b>ascendente</b> (hematogênica no RN e na sepse). "
       "<br><b><i>E. coli</i>: 80–90% do 1º episódio</b>. <i>Proteus</i>: 30% das cistites em meninos (prepúcio). <i>S. saprophyticus</i>: 30% nas adolescentes.",
  "fala": "Infecção urinária é a inflamação sintomática do trato urinário por um único germe. Até os sete anos, ela atinge cerca de oito por cento das meninas e menos de dois por cento dos meninos, e volta em trinta por cento no primeiro ano. A via é ascendente, exceto no recém-nascido, em que é hematogênica. A Escherichia coli responde por oitenta a noventa por cento do primeiro episódio.",
  "pega": "<b>E. coli 80–90%</b>. No <b>RN</b> a via é <b>hematogênica</b> (por isso bacteremia).",
  "z": "Oitenta a noventa por cento é Escherichia coli. Se a questão perguntar o germe e você não marcar isso, merece pegar uma cistite, caralho.",
  "ills": ["i_conc"]},
 {"id": "i_clin", "t": "Clínica por idade: o RN é sempre grave",
  "s": "<b>RN</b>: quadro de <b>sepse</b> ou arrastado (baixo ganho, icterícia, hipotermia, recusa alimentar); <b>alta probabilidade de bacteremia</b>, <b>mortalidade ~10%</b> → <b>ITU complicada, internar</b>. "
       "<br><b>Lactente</b>: <b>febre pode ser o único sinal</b> (febre sem sinais localizatórios); irritabilidade, vômitos. "
       "<br><b>Maiores</b>: <b>cistite</b> (disúria, polaciúria, urgência, sem febre) × <b>pielonefrite</b> (febre, calafrio, dor lombar/flanco, Giordano +). "
       "<br>Exame: PA, palpar rins e bexiga, fecaloma, genitália (fimose, sinéquia), <b>jato urinário</b>, região sacral.",
  "fala": "A apresentação da infecção urinária muda com a idade. No recém-nascido parece sepse, com hipotermia, icterícia e recusa alimentar, há bacteremia com frequência e a mortalidade chega a dez por cento, por isso todo recém-nascido é infecção complicada e interna. No lactente, a febre pode ser o único sinal. Na criança maior, separe cistite, sem febre e com disúria, de pielonefrite, com febre e dor lombar. E sempre olhe o jato e palpe a bexiga.",
  "pega": "Lactente com <b>febre sem foco</b> → pedir <b>urina</b>. RN com ITU = <b>internar sempre</b>.",
  "z": "Lactente febril sem foco e ninguém pediu urina? Então ninguém investigou a febre. Urina tipo um e cultura, porra.",
  "ills": ["i_clin"]},
 {"id": "i_coleta", "t": "Como colher a urina",
  "s": "<b>Com controle esfincteriano</b>: <b>jato médio</b> após higiene, idealmente 2 h sem urinar. "
       "<br><b>Sem controle</b>: estímulo suprapúbico (sucesso ~60%), <b>saco coletor</b> (troca a cada 30 min; <b>só vale o resultado negativo</b>), <b>cateterismo vesical</b> (contraindicado em vulvovaginite/balanopostite), <b>punção suprapúbica</b> (padrão-ouro; indicada quando diarreia, vulvovaginite ou balanopostite tornam a coleta duvidosa).",
  "fala": "Na criança com controle esfincteriano, colhe jato médio depois da higiene. No lactente, o saco coletor é o mais fácil, mas contamina muito: urocultura positiva por saco é muito difícil de valorizar, e só o resultado negativo é confiável para afastar infecção. Para confirmar, use cateterismo vesical ou punção suprapúbica, que é o padrão-ouro e a escolha quando há diarreia ou vulvovaginite.",
  "pega": "Saco coletor: <b>negativo afasta</b>, <b>positivo não confirma</b>. Saco <b>não</b> é o método preferencial.",
  "z": "Saco coletor positivo é cultura de períneo, não de bexiga. Negativo afasta; positivo, cateteriza e colhe direito, caralho.",
  "m": [["MEDCURSO · S36 38:01–39:33", "Saco coletor tem alto valor preditivo negativo."], ["MEDCURSO · S36 50:11–50:35", "“Saco coletor é o preferencial em &lt; 2 anos” foi a alternativa incorreta de uma questão comentada."]],
  "ills": ["i_coleta"]},
 {"id": "i_lab", "t": "Urina e urocultura: os cortes",
  "s": "<b>Piúria</b>: <b>≥ 5 leucócitos/campo</b> ou <b>&gt; 10.000/mL</b> (VPP 40–80%). <b>Esterase leucocitária + nitrito</b> positivos = fortemente sugestivo (nitrito exige tempo na bexiga). "
       "<br><b>Urocultura</b> (slide 17): <b>≥ 100.000 UFC/mL de uma bactéria</b> = positiva · <b>&lt; 10.000</b> = negativa · <b>10.000–100.000</b> = <b>duvidosa → repetir</b> · <b>2 ou mais cepas</b> = contaminação. "
       "<br>Punção suprapúbica: <b>qualquer crescimento</b> é significativo.",
  "fala": "Piúria é cinco ou mais leucócitos por campo, ou mais de dez mil por mililitro. Esterase e nitrito positivos juntos sugerem muito a infecção. Na urocultura, cem mil unidades formadoras de colônia de uma única bactéria confirmam; menos de dez mil é negativo; entre dez mil e cem mil é duvidoso e se repete; e duas ou mais bactérias indicam contaminação. Na punção suprapúbica, qualquer crescimento vale.",
  "div": "urocult",
  "pega": "Jato médio com <b>40.000 UFC</b> = <b>duvidoso → repetir</b>. “Qualquer crescimento” vale só para <b>punção suprapúbica</b>.",
  "z": "Quarenta mil colônias no jato médio não é infecção nem é nada: repete a cultura antes de sair dando antibiótico, porra.",
  "m": [["MEDCURSO · S36 40:32–42:06", "Punção suprapúbica: qualquer crescimento; cateterismo ≥ 50 mil sem consenso; AAP ≥ 50 mil."]],
  "ills": ["i_lab"]},
 {"id": "i_bact", "t": "Bacteriúria assintomática: não tratar",
  "s": "<b>3 uroculturas consecutivas positivas</b> (mesmo germe) em <b>3 dias a 2 semanas</b>, <b>sem sintomas</b> e sem piúria importante. Persistente em <b>mielomeningocele, bexiga neurogênica, cateterismo intermitente</b>. "
       "<br><b>Não tratar</b>: o tratamento seleciona germes mais virulentos e pode levar a ITU sintomática. (Exceções do MEDCURSO: gestante, manipulação urológica.)",
  "fala": "Bacteriúria assintomática é ter três uroculturas positivas seguidas, num intervalo de três dias a duas semanas, sem nenhum sintoma. É comum e persistente em quem tem mielomeningocele, bexiga neurogênica ou faz cateterismo de alívio. A conduta é não tratar, porque o antibiótico seleciona germes mais agressivos e acaba provocando a infecção sintomática que se queria evitar.",
  "pega": "Bacteriúria assintomática na bexiga neurogênica: <b>não tratar</b> (nem profilaxia).",
  "z": "Criança que cateteriza a bexiga sempre vai ter bactéria na urina. Tratar cultura em vez de tratar paciente é fábrica de superbactéria, caralho.",
  "m": [["MEDCURSO · S36 21:53–22:52", "Tratar só gestante e antes de manipulação urológica com lesão de mucosa."]],
  "ills": ["i_bact"]},
 {"id": "i_trat", "t": "Tratamento: quando internar e as doses",
  "s": "<b>Iniciar o antibiótico logo após colher a urina</b> — a demora (&gt; 72 h) é fator de risco para <b>lesão renal</b>. "
       "<br><b>Internar</b>: toxemia, desidratação, <b>vômitos</b>/intolerância oral, choque, e <b>todo RN</b> (ITU complicada). "
       "<br><b>VO, 10 dias (7–14)</b>: SMX-TMP 40 + 8 mg/kg/dia 2× · cefadroxil 30–50 2× · <b>cefalexina 50–100 mg/kg/dia 4×</b> · ácido nalidíxico 60 4× · amoxicilina-clavulanato 40 2×. "
       "<br><b>EV/IM</b>: ceftriaxona 50–100 mg/kg/dia (1–2×) · gentamicina 7,5 (3×) · amicacina 15 (1–2×). <b>RN</b>: <b>ampicilina (ou penicilina) + aminoglicosídeo</b>. "
       "<br>Nitrofurantoína <b>não</b> trata pielonefrite (não atinge o parênquima).",
  "fala": "O antibiótico começa logo depois de colher a urina, porque a demora é fator de risco para cicatriz renal. Interna quem está toxemiado, desidratado, vomitando, em choque, e todo recém-nascido, que recebe ampicilina mais aminoglicosídeo. O resto trata por via oral por dez dias; a cefalexina é cinquenta a cem miligramas por quilo por dia em quatro doses. Pielonefrite sem gravidade também pode ser oral, mas nunca com nitrofurantoína.",
  "div": "duracao",
  "pega": "“Toda pielonefrite interna” é <b>mito</b>. <b>Não esperar</b> a urocultura para começar. Nitrofurantoína <b>não</b> para pielonefrite.",
  "z": "Esperar a urocultura pra começar antibiótico numa pielonefrite é dar setenta e duas horas de vantagem pra cicatriz renal. Colheu, começou, porra.",
  "m": [["MEDCURSO · S36 51:16–52:02", "Pielonefrite sem toxemia pode ser tratada ambulatorialmente."], ["MEDCURSO · S36 55:59–57:03", "Nitrofurantoína não atinge o parênquima renal."]],
  "ills": ["i_trat"]},
 {"id": "i_profil", "t": "Profilaxia antibiótica: quando e com o quê",
  "s": "Dose <b>subterapêutica</b> (≈ 1/3 da dose, à noite). Indicações (slide 26): <b>durante a investigação</b> · <b>anomalia obstrutiva até a cirurgia</b> · <b>RVU graus III a V</b> · RVU I–II com ITU de repetição ou DMSA alterada · <b>recidivas frequentes</b> (6–12 meses). "
       "<br>Drogas: <b>nitrofurantoína ou SMX-TMP</b> (&gt; 2 meses); <b>cefalexina</b> (&lt; 2 meses). "
       "<br>Metanálises: <b>reduz ITU sintomática</b>, mas <b>não reduz novas cicatrizes</b>.",
  "fala": "A profilaxia usa dose baixa, cerca de um terço da dose, à noite. Ela está indicada durante a investigação, nas uropatias obstrutivas até a cirurgia, no refluxo de graus três a cinco, no refluxo leve com infecções de repetição ou cintilografia alterada, e nas recidivas frequentes. Acima de dois meses usa nitrofurantoína ou sulfametoxazol com trimetoprim; abaixo, cefalexina. E lembre: ela reduz infecção, mas não reduz cicatriz.",
  "pega": "&lt; 2 meses → <b>cefalexina</b>. RVU <b>I–II isolado</b> não tem indicação. Profilaxia <b>não</b> previne cicatriz.",
  "z": "Sulfa em bebê de um mês é pedir kernicterus. Abaixo de dois meses a profilaxia é cefalexina, porra.",
  "ills": ["i_profil"]},
 {"id": "i_imagem", "t": "Investigação por imagem após ITU febril (caiu 2×)",
  "s": "Investigar após o <b>1º episódio bem documentado</b> de ITU febril (slide 28). "
       "<br>• <b>USG de rins e vias urinárias</b>: primeiro; não vê RVU. "
       "<br>• <b>Uretrocistografia miccional (UCM)</b>: <b>principal exame para RVU</b> (e VUP); <b>só após o término do tratamento</b>, em profilaxia. "
       "<br>• <b>Cintilografia DMSA</b> (estática): <b>morfologia, cicatriz renal</b>, função de cada rim — <b>3 meses após a cura</b>. "
       "<br>• <b>DTPA</b> (dinâmica): <b>obstrução</b>; não serve para RVU. Cistografia isotópica: RVU sem iodo. "
       "<br>Algoritmo: <b>&lt; 2 anos → profilaxia até o USG</b>.",
  "fala": "Essa é a pergunta que mais caiu do capítulo. Depois de uma infecção urinária febril bem documentada, a investigação começa pelo ultrassom de rins e vias urinárias, que não enxerga refluxo. O refluxo é visto pela uretrocistografia miccional, o principal exame, feita só depois de terminar o tratamento. A cintilografia com DMSA mostra cicatriz renal, três meses após a cura. E o DTPA é para obstrução. Abaixo de dois anos, a criança fica em profilaxia até o ultrassom.",
  "div": "dmsa",
  "pega": "Os compilados <b>esqueceram a UCM</b>: é o exame do <b>refluxo</b>, cobrado junto com o <b>DMSA</b>. DMSA = “M de morfológica” (cicatriz).",
  "z": "Ultrassom, uretrocistografia e DMSA: três exames, três perguntas — anatomia, refluxo e cicatriz. Esqueceu a uretrocistografia, perdeu metade da questão, caralho.",
  "m": [["MEDCURSO · S36 1:07:34–1:08:14", "DMSA = M de Morfológica; para cicatriz, 4–6 meses após (slide: 3 meses)."]],
  "ills": ["i_imagem"]},
 {"id": "i_rvu", "t": "Refluxo vesicoureteral, lesão renal e válvula de uretra posterior",
  "s": "<b>RVU</b>: ~1% das crianças, <b>30–40% das com ITU</b>; graus I–V; involução espontânea frequente, cirurgia rara; seguir até a idade adulta. "
       "<br><b>Risco de lesão renal</b>: <b>&lt; 1 ano</b>, <b>atraso no tratamento &gt; 72 h</b>, refluxo de alto grau, <b>obstrução</b>, recorrência. "
       "<br><b>Válvula de uretra posterior</b>: <b>menino</b>, hidronefrose bilateral pré-natal, <b>bexiga palpável</b>, <b>jato fraco/gotejamento</b>, ITU de repetição → confirma com <b>UCM</b>.",
  "fala": "O refluxo vesicoureteral está presente em trinta a quarenta por cento das crianças com infecção urinária, e costuma regredir sozinho. O risco de cicatriz renal é maior abaixo de um ano, quando o tratamento atrasa mais de setenta e duas horas, no refluxo de alto grau, na obstrução e nas recorrências. E o menino com hidronefrose bilateral no pré-natal, bexiga palpável e jato fraco tem válvula de uretra posterior até prova em contrário, confirmada pela uretrocistografia.",
  "pega": "Menino + bexiga distendida + jato em <b>gotejamento</b> = <b>VUP</b> → <b>UCM</b> (não DTPA).",
  "z": "Menino que faz xixi pingando e tem bexiga do tamanho de uma laranja não tem preguiça de urinar: tem válvula de uretra posterior. Uretrocistografia, porra.",
  "m": [["MEDCURSO · S36 Outros 16:54–20:17", "VUP: menino, hidronefrose bilateral, distensão vesical, jato fraco; confirma com UCM."]],
  "ills": ["i_rvu"]},
]

ILLS = {
 "i_conc": cards("ITU: números de prova", [
     ("🦠", "E. coli", "80–90% do 1º episódio", "t"),
     ("👧", "Meninas", "8% até 7 anos · meninos < 2%", "v"),
     ("🔁", "Recorrência", "30% em 1 ano · 50% em 5 anos", "a"),
     ("⬆️", "Via", "ascendente · RN: hematogênica", "p")],
     foot="Proteus: 30% das cistites em meninos · S. saprophyticus: adolescentes", fcor="t"),
 "i_clin": flow("Clínica por idade", [
     ("🍼", "Recém-nascido", "sepse ou quadro arrastado, icterícia · bacteremia · mortalidade ~10% → internar", "r"),
     ("👶", "Lactente", "febre pode ser o único sinal", "a"),
     ("🧒", "Cistite", "disúria, polaciúria, urgência, sem febre", "t"),
     ("🔥", "Pielonefrite", "febre, calafrio, dor lombar, Giordano +", "v")],
     foot="Exame: PA, rins e bexiga, fecaloma, genitália, jato, região sacral", fcor="t"),
 "i_coleta": table("Coleta de urina", [
     ("Jato médio", "com controle esfincteriano, após higiene"),
     ("Saco coletor", "troca a cada 30 min · só o NEGATIVO vale"),
     ("Cateterismo", "aceito · evitar em vulvovaginite/balanopostite"),
     ("Punção suprapúbica", "padrão-ouro · diarreia, vulvovaginite, balanopostite"),
     ("Estímulo suprapúbico", "sucesso ~60%")], cor="t"),
 "i_lab": table("Cortes do laboratório", [
     ("Piúria", "≥ 5 leucócitos/campo ou > 10.000/mL"),
     ("Esterase + nitrito", "fortemente sugestivo"),
     ("≥ 100.000 UFC", "positiva (uma bactéria)"),
     ("10.000–100.000", "duvidosa → repetir"),
     ("< 10.000", "negativa"),
     ("≥ 2 cepas", "contaminação"),
     ("Punção suprapúbica", "qualquer crescimento")], cor="t"),
 "i_bact": cards("Bacteriúria assintomática", [
     ("3️⃣", "Definição", "3 uroculturas + em 3 dias a 2 semanas, sem sintomas", "t"),
     ("♿", "Onde persiste", "mielomeningocele, bexiga neurogênica, cateterismo", "p"),
     ("🚫", "Conduta", "não tratar e não fazer profilaxia", "r"),
     ("⚠️", "Por quê", "seleciona germe mais virulento → ITU sintomática", "a")]),
 "i_trat": table("Tratamento e doses (mg/kg/dia)", [
     ("Internar", "toxemia · desidratação · vômitos · choque · todo RN"),
     ("Cefalexina VO", "50–100 em 4 doses · 10 dias (7–14)"),
     ("Cefadroxil VO", "30–50 em 2 doses"),
     ("SMX-TMP VO", "40 + 8 em 2 doses"),
     ("Amoxi-clav VO", "40 em 2 doses"),
     ("Ceftriaxona EV/IM", "50–100 em 1–2 doses"),
     ("Gentamicina / amicacina", "7,5 (3×) / 15 (1–2×)"),
     ("RN", "ampicilina (ou penicilina) + aminoglicosídeo")], cor="g",
     foot="Começar logo após colher · nitrofurantoína não trata pielonefrite"),
 "i_profil": cards("Profilaxia (dose subterapêutica)", [
     ("🔎", "Durante a investigação", "< 2 anos até o USG", "t"),
     ("🚧", "Obstrução", "até a cirurgia", "v"),
     ("↩️", "RVU III–V", "e I–II com recidiva ou DMSA alterada", "p"),
     ("💊", "Drogas", "nitrofurantoína ou SMX-TMP > 2 m · cefalexina < 2 m", "g")],
     foot="Reduz ITU sintomática, NÃO reduz novas cicatrizes"),
 "i_imagem": flow("Investigação após ITU febril", [
     ("🔊", "USG de rins e vias", "primeiro exame · não vê RVU", "t"),
     ("🎞️", "Uretrocistografia miccional", "principal para RVU (e VUP) · só após o tratamento, em profilaxia", "v"),
     ("☢️", "Cintilografia DMSA", "cicatriz renal / morfologia · 3 meses após a cura", "p"),
     ("⏳", "DTPA", "obstrução (dinâmica) · não serve para RVU", "a")],
     foot="< 2 anos: profilaxia até o USG", fcor="t"),
 "i_rvu": versus("RVU e válvula de uretra posterior", ("↩️", "Refluxo vesicoureteral", "p", [
     "• 30–40% das crianças com ITU", "• graus I–V, involui com frequência", "• UCM diagnostica", "• seguir até adulto"]),
     ("🚧", "Válvula de uretra posterior", "r", [
     "• menino", "• hidronefrose bilateral pré-natal", "• bexiga palpável", "• jato fraco / gotejamento", "• UCM confirma"]),
     foot="Risco de lesão: < 1 ano · atraso > 72 h · RVU alto · obstrução · recorrência"),
}

QMAP = {0: ["i_coleta"], 1: ["i_lab"], 2: ["i_trat"], 3: ["i_trat", "i_clin"], 4: ["i_imagem"], 5: ["i_profil"], 6: ["i_rvu"], 7: ["i_bact"]}

DIV = {
 "urocult": ["Critério de urocultura positiva", "Slide 17: critério único <b>≥ 100.000 UFC</b>, sem distinguir método",
             "MEDCURSO: jato ≥ 100 mil; cateterismo ≥ 50 mil (sem consenso); punção qualquer; AAP ≥ 50 mil",
             "Faculdade: <b>≥ 100.000</b> (slide); cite “punção suprapúbica: qualquer crescimento”"],
 "duracao": ["Duração do tratamento", "Slides 23–24: “10 dias (7 a 14)” só no ambulatorial", "MEDCURSO: cistite 3–5 dias; pielonefrite 7–14 (Nelson 7–10)",
             "Prova: <b>10 dias (7–14)</b>"],
 "dmsa": ["Quando fazer o DMSA para cicatriz", "Slide 34: <b>3 meses</b> após a cura", "MEDCURSO (S36 1:04:00): 4–6 meses", "Prova: <b>3 meses</b> (slide)"],
}

FLASH = [
 [9, "Germe do 1º episódio de ITU?", "E. coli (80–90%)."],
 [9, "Via no RN?", "Hematogênica (bacteremia, mortalidade ~10%)."],
 [9, "RN com ITU: conduta?", "Internar; ampicilina + aminoglicosídeo."],
 [9, "Lactente: único sinal possível?", "Febre."],
 [9, "Saco coletor: o que vale?", "Só o resultado negativo."],
 [9, "Piúria?", "≥ 5 leucócitos/campo ou > 10.000/mL."],
 [9, "Urocultura positiva (slide)?", "≥ 100.000 UFC de uma bactéria."],
 [9, "10.000–100.000 UFC?", "Duvidoso → repetir."],
 [9, "Punção suprapúbica: corte?", "Qualquer crescimento."],
 [9, "Bacteriúria assintomática?", "3 culturas + em 3 d–2 sem, sem sintomas → não tratar."],
 [9, "Cefalexina na ITU?", "50–100 mg/kg/dia em 4 doses, 10 dias."],
 [9, "Quando iniciar o antibiótico?", "Logo após colher a urina."],
 [9, "Profilaxia < 2 meses?", "Cefalexina."],
 [9, "Profilaxia previne cicatriz?", "Não; reduz ITU sintomática."],
 [9, "Exame principal para RVU?", "Uretrocistografia miccional, após o tratamento."],
 [9, "Exame para cicatriz renal?", "DMSA, 3 meses após a cura."],
 [9, "DTPA serve para?", "Obstrução."],
 [9, "Menino, bexiga palpável, jato em gotejamento?", "Válvula de uretra posterior → UCM."],
]

COLA = [["Cap. 9 · ITU", [
 ["E. coli", "80–90%"], ["Meninas", "8% · recorrência 30%/1 a"], ["RN", "bacteremia · ~10% mortalidade · internar"],
 ["Piúria", "≥ 5/campo · > 10 mil/mL"], ["Urocultura", "≥ 100 mil + · 10–100 mil repetir · < 10 mil −"], ["Saco coletor", "só negativo vale"],
 ["Cefalexina", "50–100 mg/kg/dia 4× · 10 d"], ["Ceftriaxona", "50–100 mg/kg/dia"], ["RN", "ampicilina + aminoglicosídeo"],
 ["Profilaxia", "nitrofurantoína/SMX-TMP > 2 m · cefalexina < 2 m"], ["Imagem", "USG → UCM (pós-tto) → DMSA 3 m"],
 ["Risco de lesão", "< 1 a · atraso > 72 h · RVU alto · obstrução"]]]]

KS = [
 {"id": "k_i_inv", "cap": 9, "blk": ["i_imagem", "i_profil"], "t": "Investigação após a 1ª ITU febril (caiu 2×)",
  "src": "Caiu em 2 provas antigas (0,6 pt) — Profa. Patrícia",
  "enun": "Menina de <b>1 ano</b> com ITU febril (febre alta, vômitos, comprometimento importante do estado geral), tratada adequadamente.",
  "p": [{"p": "Em que consiste a investigação? Cite os exames e o objetivo de cada um.",
         "m": "Investigar após o 1º episódio bem documentado (slide 28): <b>ultrassom de rins e vias urinárias</b> primeiro (em &lt; 2 anos, profilaxia até o USG); <b>uretrocistografia miccional</b> após o tratamento, para <b>refluxo vesicoureteral</b>; <b>cintilografia com DMSA</b> para <b>cicatriz renal</b>, <b>3 meses após a cura</b>. (DTPA só se suspeita de obstrução.)",
         "c": ["ultrassom", "uretrocistografia miccional", "refluxo vesicoureteral", "após o tratamento", "DMSA", "cicatriz renal", "3 meses"]},
        {"p": "Ela deve receber profilaxia? Com qual droga?",
         "m": "Sim, <b>durante a investigação</b> (&lt; 2 anos até o USG; manter se RVU III–V, obstrução ou recidivas): <b>nitrofurantoína ou SMX-TMP</b> em dose subterapêutica (≈ 1/3, à noite), pois tem &gt; 2 meses.",
         "c": ["durante a investigação", "nitrofurantoína", "sulfametoxazol", "dose subterapêutica"]}]},
 {"id": "k_i_trat", "cap": 9, "blk": ["i_trat", "i_lab", "i_coleta"], "t": "Pielonefrite no pré-escolar",
  "src": "Caso autoral no estilo da professora (slides 14–23)",
  "enun": "Menino de 3 anos, 14 kg, febre de 38,8 °C há 2 dias e dor lombar; bom estado geral, hidratado, aceitando dieta. EAS: piúria, esterase e nitrito positivos.",
  "p": [{"p": "Como colher a urocultura e qual resultado confirma?",
         "m": "Sem controle confiável: <b>cateterismo</b> ou <b>punção suprapúbica</b> (saco coletor só vale se negativo); com controle, <b>jato médio</b>. Confirma: <b>≥ 100.000 UFC/mL de uma bactéria</b> (punção: qualquer crescimento).",
         "c": ["cateterismo", "punção suprapúbica", "saco coletor", "100.000 UFC", "uma bactéria"]},
        {"p": "Precisa internar? Prescreva o tratamento.",
         "m": "<b>Não</b>: sem toxemia, desidratação ou vômitos (internar todo RN e os graves). <b>Iniciar logo após a coleta</b>: <b>cefalexina 50–100 mg/kg/dia em 4 doses</b> (14 kg: 700–1.400 mg/dia) por <b>10 dias (7–14)</b>. Nitrofurantoína não serve para pielonefrite.",
         "c": ["não internar", "logo após a coleta", "cefalexina", "50 a 100 mg/kg/dia", "4 doses", "10 dias"]}]},
]
