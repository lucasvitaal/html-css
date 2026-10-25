CAP = {"n": 6, "t": "Dengue na criança", "short": "Dengue", "aula": "Aula 6 · slides da Patrícia",
       "icon": "🦟", "col": "#2E6B4F",
       "bul": ["Grupo B com 15 kg: caiu nas 3 provas — VO supervisionada ≥ 50 mL/kg em 4–6 h",
               "Alarme (1 basta) → C: SF 20 mL/kg/h até 3×, Ht após 2 h",
               "Choque → D: 20 mL/kg em até 20 min até 3×, UTI",
               "NS1/PCR até o 5º dia · IgM a partir do 6º · laço criança 3 min ≥ 10"],
       "medalha": ["🦟", "Mata-mosquito"]}

BLOCKS = [
 {"id": "g_doenca", "t": "O vírus, o mosquito e quem tem mais risco",
  "s": "<b>Flavivírus</b> (RNA), <b>4 sorotipos</b>; imunidade permanente só para o mesmo sorotipo. Vetor: <b>Aedes aegypti</b> fêmea. "
       "<br>Incubação <b>4–7 dias</b> (3–14); viremia de 1–2 dias antes até 5–7 dias de sintomas; mosquito transmite após 8–12 dias. "
       "<br>Risco de forma grave: <b>infecção secundária heterotípica</b>, criança, doença crônica. Sazonal: jan–jun.",
  "fala": "Dengue é um flavivírus com quatro sorotipos, transmitido pela fêmea do Aedes aegypti. Pegar um sorotipo protege só contra ele, e a segunda infecção por um sorotipo diferente é o principal risco de forma grave. A incubação é de quatro a sete dias, e a criança, assim como quem tem doença crônica, está no grupo de maior risco.",
  "pega": "Maior risco de grave: <b>segunda infecção por sorotipo diferente</b>.",
  "z": "Teve dengue uma vez e acha que está imune? Só contra aquele sorotipo. O segundo diferente é que vem quebrando tudo, porra.",
  "ills": ["g_doenca"]},
 {"id": "g_fases", "t": "As três fases: febril, crítica e recuperação",
  "s": "<b>Febril</b> (2–7 dias): 39–40 °C, cefaleia, <b>dor retro-orbitária</b>, mialgia, exantema em ~50%. "
       "<br><b>Crítica</b>: na <b>defervescência</b>, entre o <b>3º e o 7º dia</b> — extravasamento plasmático, <b>sinais de alarme</b>, choque. "
       "<br><b>Recuperação</b>: reabsorção do líquido, rash pruriginoso, bradicardia; cuidado com <b>hiper-hidratação</b> e infecção bacteriana.",
  "fala": "A dengue tem três fases. A febril dura de dois a sete dias, com febre alta, dor atrás dos olhos e dor no corpo. A crítica chega justamente quando a febre cai, entre o terceiro e o sétimo dia: é aí que o plasma extravasa, aparecem os sinais de alarme e pode vir o choque. Na recuperação o líquido volta para o vaso, e o risco passa a ser a hiper-hidratação.",
  "pega": "O perigo é na <b>defervescência</b> (3º–7º dia): febre caindo <b>não</b> é melhora garantida.",
  "z": "A febre passou e a mãe acha que acabou? É exatamente aí que a dengue mata. Reavalia essa criança no dia que a febre some, caralho.",
  "ills": ["g_fases"]},
 {"id": "g_def", "t": "Caso suspeito, sinais de alarme e de choque",
  "s": "<b>Suspeito</b>: área de transmissão + febre 2–7 dias + ≥ 2 sintomas (náusea, exantema, mialgia, cefaleia, dor retro-orbitária, petéquias/laço+, leucopenia…). <b>Criança: febre de 2–7 dias sem foco</b> já basta. Notificar. "
       "<br><b>Alarme (1 basta)</b>: dor abdominal intensa e contínua · vômitos persistentes · <b>hipotensão postural/lipotimia</b> · <b>hepatomegalia dolorosa &gt; 2 cm</b> · sangramento de mucosa · <b>letargia/irritabilidade</b> · ↓ diurese · hipotermia · <b>↑ Ht</b> · ↓ plaquetas · acúmulo de líquidos (ascite, derrames) · desconforto respiratório. "
       "<br><b>Choque</b>: pulso rápido e fino, <b>PA convergente</b> (diferencial ≤ 20 mmHg), <b>TEC &gt; 2 s</b>, extremidades frias, hipotensão.",
  "fala": "Na criança, febre de dois a sete dias sem foco em área de transmissão já é caso suspeito, sem precisar dos dois sintomas do adulto. Um único sinal de alarme muda tudo: dor abdominal intensa, vômitos persistentes, tontura ao levantar, fígado grande e doloroso, sangramento de mucosa, sonolência ou irritabilidade, pouca urina, acúmulo de líquido e hematócrito subindo. Choque é pulso fino, pressão convergente e enchimento capilar acima de dois segundos.",
  "pega": "Criança: <b>febre sem foco</b> em área de transmissão já é suspeita. <b>Um</b> sinal de alarme basta para o grupo C.",
  "z": "Criança com dengue, sonolenta e com fígado doendo não é grupo A com soro caseiro: é sinal de alarme, é veia, é grupo C, porra.",
  "ills": ["g_def"]},
 {"id": "g_diag", "t": "Diagnóstico: NS1, IgM, hemograma e prova do laço",
  "s": "Diagnóstico é <b>clínico</b>; o manejo <b>não espera</b> laboratório. "
       "<br><b>NS1 ou RT-PCR até o 5º dia</b>; <b>IgM a partir do 6º dia</b>. "
       "<br>Hemograma: leucopenia, linfócitos atípicos; gravidade: <b>hemoconcentração</b>, plaquetas &lt; 100.000, hipoalbuminemia. "
       "<br><b>Prova do laço</b>: manguito na PA média; <b>criança 3 min e ≥ 10 petéquias</b> (adulto 5 min, ≥ 20) num quadrado de 2,5 × 2,5 cm.",
  "fala": "O diagnóstico da dengue é clínico e a hidratação nunca espera exame. Para confirmar, até o quinto dia se pede antígeno NS1 ou PCR; a partir do sexto dia, sorologia igê eme. No hemograma, leucopenia é esperada, e hemoconcentração com plaqueta caindo é gravidade. A prova do laço na criança dura três minutos e é positiva com dez ou mais petéquias no quadrado.",
  "pega": "Laço: <b>criança 3 min / ≥ 10</b> · adulto 5 min / ≥ 20. 4º dia → <b>NS1/PCR</b>, não IgM.",
  "z": "Pediu igê eme no terceiro dia? Vai dar negativo e você vai achar que não é dengue. NS1 até o quinto, caralho.",
  "ills": ["g_diag"]},
 {"id": "g_grupos", "t": "Classificação em grupos A, B, C e D",
  "s": "<b>A</b>: sem alarme, sem sangramento, sem condição especial → <b>atenção primária</b>, casa. "
       "<br><b>B</b>: <b>sangramento de pele espontâneo ou laço +</b>, ou <b>condição especial</b> (<b>&lt; 2 anos</b>, gestante, &gt; 65, comorbidade, risco social) → <b>observação na unidade</b>. "
       "<br><b>C</b>: <b>sinal de alarme</b>, sem choque → <b>internação</b>. "
       "<br><b>D</b>: <b>choque</b> ou sangramento grave/disfunção de órgão → <b>UTI</b>. "
       "<br><b>Hidratar antes do exame</b> e <b>reclassificar a cada reavaliação</b>.",
  "fala": "A classificação define onde a criança fica e como se hidrata. Grupo A não tem alarme nem sangramento e vai para casa. Grupo B tem petéquias espontâneas, prova do laço positiva ou condição especial, como ter menos de dois anos, e fica em observação na unidade. Grupo C tem sinal de alarme sem choque e é internado. Grupo D é o choque, na terapia intensiva. E a classificação muda a cada reavaliação.",
  "pega": "<b>Petéquias espontâneas</b> sem alarme = <b>B</b> (não A). <b>&lt; 2 anos</b> = condição especial → <b>B</b>.",
  "z": "Petéquia na cara não é enfeite: tirou a criança do grupo A e jogou no B. Hemograma e soro na unidade, porra.",
  "ills": ["g_grupos"]},
 {"id": "g_ab", "t": "Grupos A e B: hidratação oral e o que observar",
  "s": "<b>Grupo A</b>: hidratação oral em casa — <b>≤ 10 kg: 130 mL/kg/dia</b> · <b>10–20 kg: 100</b> · <b>&gt; 20 kg: 80</b>; <b>1/3 em SRO</b> e o resto em líquidos caseiros. Dipirona ou paracetamol, <b>sem AINE</b>; antiemético (bromoprida/metoclopramida). Hemograma <b>obrigatório &lt; 5 anos</b>. Retorno na defervescência ou no 5º dia; orientar alarmes. "
       "<br><b>Grupo B</b>: <b>hemograma obrigatório</b> (resultado em até 4 h) e <b>hidratação ORAL supervisionada na unidade, antes do resultado</b>: <b>≥ 50 mL/kg em 4–6 h</b>. Reavaliar clínica, diurese (&lt; 1,5 mL/kg/h preocupa), Ht e plaquetas. <b>Ht &gt; 38%</b>, alarme ou recusa da VO → <b>venosa = conduta C</b>. Notificar.",
  "fala": "No grupo A a hidratação é oral em casa: cento e trinta mililitros por quilo por dia até dez quilos, cem entre dez e vinte, e oitenta acima de vinte, com um terço em soro de reidratação oral, febre tratada com dipirona ou paracetamol e nunca anti-inflamatório. No grupo B, hemograma obrigatório e hidratação oral supervisionada na própria unidade, já antes do resultado: pelo menos cinquenta mililitros por quilo em quatro a seis horas. Hematócrito acima de trinta e oito, alarme ou recusa, vira grupo C.",
  "div": "grupoB_ht",
  "pega": "Criança de <b>15 kg</b> no B: <b>≥ 750 mL VO</b> em 4–6 h na unidade. Erro dos compilados: “grupo A” e “50 mL/kg <b>venoso</b>”.",
  "z": "Quinze quilos vezes cinquenta dá setecentos e cinquenta mililitros pela boca, na unidade, com alguém olhando. Não é veia e não é pra casa, porra.",
  "ills": ["g_ab"]},
 {"id": "g_cd", "t": "Grupos C e D: expansão, reavaliação e o hematócrito",
  "s": "<b>Grupo C</b>: <b>SF 0,9% ou RL 20 mL/kg/hora</b>, até <b>3 vezes</b>; reavaliação <b>clínica horária</b>; <b>Ht após 2 h</b>. Melhorou → <b>manutenção (Holliday-Segar)</b> + reposição de perdas. Internação mínima 48 h. "
       "<br><b>Grupo D</b>: O₂, acesso calibroso, <b>20 mL/kg em até 20 min</b>, até <b>3 vezes</b>, reavaliação contínua; <b>Ht após 2 h</b>; UTI; PA 2/2 h, Ht 4/4 h, plaquetas 12/12 h. "
       "<br>Persistindo o choque: <b>Ht subindo</b> → <b>albumina</b> (coloide) · <b>Ht caindo com choque</b> → <b>hemorragia</b>: concentrado de hemácias, plasma, vitamina K, crioprecipitado · <b>Ht caindo sem sangramento</b> → hiper-hidratação: ↓ soro, diurético, inotrópico. "
       "<br><b>Nunca soro glicosado na expansão.</b>",
  "fala": "No grupo C a expansão é soro fisiológico ou Ringer, vinte mililitros por quilo por hora, até três vezes, com reavaliação clínica a cada hora e hematócrito depois de duas horas; melhorou, passa para manutenção. No grupo D, choque, são vinte mililitros por quilo em até vinte minutos, até três vezes, na terapia intensiva. Se o choque persiste, olhe o hematócrito: subindo pede albumina; caindo com choque pede sangue; caindo sem sangramento é excesso de volume.",
  "div": "grupoC_tempo",
  "pega": "C = 20 mL/kg <b>em 1 hora</b>; D = 20 mL/kg <b>em até 20 min</b>. Ht ↓ + choque = <b>sangrando</b> → hemácias.",
  "z": "Choque com hematócrito despencando e melena não é falta de soro, é sangue saindo. Concentrado de hemácias, não a quarta expansão, caralho.",
  "m": [["MEDCURSO · S30 P2 18:29–20:04", "Expansão sempre com cristaloide isotônico, nunca soro glicosado."]],
  "ills": ["g_cd"]},
 {"id": "g_vac", "t": "Prevenção e vacinas",
  "s": "Controle do vetor (água parada). "
       "<br><b>Dengvaxia</b>: <b>9–45 anos</b>, 3 doses (0-6-12 meses), <b>só soropositivo</b> (infecção prévia comprovada). "
       "<br><b>Qdenga</b>: atenuada, <b>2 doses com 3 meses</b> de intervalo, <b>pode em soronegativo</b>; vírus vivo → <b>contraindicada na lactante</b> (e gestante, imunodeprimido).",
  "fala": "A prevenção começa no vetor, sem água parada. Das vacinas, a Dengvaxia é de nove a quarenta e cinco anos, em três doses, e só para quem já teve dengue comprovada. A Qdenga é de vírus atenuado, em duas doses com três meses de intervalo, e pode ser dada em quem nunca teve dengue; por ser viva, é contraindicada na mulher que está amamentando.",
  "div": "dengvaxia",
  "pega": "Soronegativo → <b>Qdenga</b>, nunca Dengvaxia. Lactante <b>não</b> recebe Qdenga (vírus vivo).",
  "z": "Deu Dengvaxia em quem nunca teve dengue? Parabéns, transformou a primeira infecção dele numa segunda infecção grave. Qdenga, porra.",
  "m": [["MEDCURSO · S27 Aspectos iniciais 31:26–32:24", "Vacina viva contraindicada na lactante; o corte de 6 meses é da febre amarela, não da dengue."]],
  "ills": ["g_vac"]},
]

ILLS = {
 "g_doenca": cards("Dengue: o básico", [
     ("🧬", "Flavivírus", "RNA · 4 sorotipos · imunidade só ao mesmo", "t"),
     ("🦟", "Aedes aegypti", "fêmea · mosquito transmite após 8–12 dias", "g"),
     ("⏳", "Incubação", "4–7 dias (3–14)", "a"),
     ("⚠️", "Risco de grave", "infecção secundária heterotípica, criança, doença crônica", "r")]),
 "g_fases": flow("As três fases", [
     ("🌡️", "Febril (2–7 dias)", "39–40 °C, dor retro-orbitária, mialgia, exantema 50%", "a"),
     ("⚠️", "Crítica (3º–7º dia)", "na defervescência: extravasamento, alarme, choque", "r"),
     ("💧", "Recuperação", "reabsorção, rash pruriginoso — cuidado com hiper-hidratação", "g")]),
 "g_def": cards("Sinais de alarme (1 basta) e de choque", [
     ("🤕", "Dor abdominal intensa", "contínua, ou à palpação", "r"),
     ("🤮", "Vômitos persistentes", "e ↓ diurese", "r"),
     ("😵", "Hipotensão postural", "lipotimia · letargia ou irritabilidade", "r"),
     ("🫃", "Hepatomegalia dolorosa", "> 2 cm · ascite, derrames", "r"),
     ("🩸", "Sangramento de mucosa", "↑ hematócrito · ↓ plaquetas", "a"),
     ("🫀", "Choque", "pulso fino · PA diferencial ≤ 20 · TEC > 2 s", "p")],
     foot="Criança: febre 2–7 dias sem foco em área de transmissão = suspeito", fcor="t"),
 "g_diag": table("Diagnóstico laboratorial", [
     ("Até o 5º dia", "NS1 ou RT-PCR"), ("A partir do 6º dia", "sorologia IgM"),
     ("Hemograma", "leucopenia, linfócitos atípicos"), ("Gravidade", "hemoconcentração · plaquetas < 100.000 · hipoalbuminemia"),
     ("Laço criança", "3 minutos · ≥ 10 petéquias em 2,5 × 2,5 cm"), ("Laço adulto", "5 minutos · ≥ 20 petéquias")], cor="g",
     foot="Hidratação nunca espera exame", fcor="r"),
 "g_grupos": flow("Grupos A → D", [
     ("🏠", "A · atenção primária", "sem alarme, sem sangramento, sem condição especial", "g"),
     ("🏥", "B · observação na unidade", "petéquias espontâneas / laço + ou condição especial (< 2 anos, comorbidade)", "a"),
     ("🛏️", "C · internação", "qualquer sinal de alarme, sem choque", "r"),
     ("🚨", "D · UTI", "choque, sangramento grave, disfunção de órgão", "v")],
     foot="Hidratar antes do resultado · reclassificar a cada reavaliação", fcor="t"),
 "g_ab": table("Grupos A e B: os números", [
     ("A · ≤ 10 kg", "130 mL/kg/dia"), ("A · 10–20 kg", "100 mL/kg/dia"), ("A · > 20 kg", "80 mL/kg/dia"),
     ("A · composição", "1/3 SRO + 2/3 líquidos caseiros · dipirona/paracetamol · sem AINE"),
     ("B · hemograma", "obrigatório, resultado em até 4 h"),
     ("B · hidratação", "VO supervisionada ≥ 50 mL/kg em 4–6 h (15 kg = 750 mL)"),
     ("B → C", "Ht > 38% · alarme · recusa da VO · diurese < 1,5 mL/kg/h")], cor="g"),
 "g_cd": flow("Grupos C e D: expansão e o que fazer se não melhora", [
     ("💧", "C · SF/RL 20 mL/kg/hora", "até 3× · reavaliação clínica horária · Ht após 2 h → manutenção", "a"),
     ("🚨", "D · 20 mL/kg em até 20 min", "até 3× · O₂ · UTI · Ht após 2 h", "r"),
     ("📈", "Ht subindo + choque", "albumina (coloide)", "p"),
     ("🩸", "Ht caindo + choque", "hemorragia: hemácias, plasma, vitamina K, crio", "r"),
     ("💦", "Ht caindo sem sangrar", "hiper-hidratação: ↓ soro, diurético, inotrópico", "t")],
     foot="Nunca soro glicosado na expansão"),
 "g_vac": versus("Vacinas da dengue", ("💉", "Dengvaxia", "t", [
     "• 9–45 anos", "• 3 doses (0-6-12 m)", "✔ só soropositivo", "✘ soronegativo"]),
     ("💉", "Qdenga", "g", [
     "• atenuada (vírus vivo)", "• 2 doses, intervalo 3 meses", "✔ pode em soronegativo", "✘ lactante, gestante, imunodeprimido"])),
}

QMAP = {0: ["g_grupos", "g_ab"], 1: ["g_ab"], 2: ["g_def", "g_grupos"], 3: ["g_cd"], 4: ["g_cd", "g_def"], 5: ["g_cd"], 6: ["g_diag"], 7: ["g_vac"]}

DIV = {
 "grupoB_ht": ["Hidratação do grupo B com Ht aumentado", "Slide 32: VO <b>≥ 50 mL/kg em 4–6 h</b>; <b>Ht &gt; 38%</b> → conduta do grupo C",
               "Fluxograma do MS (slide 26, baixa resolução): VO 50–100 mL/kg em 4 h ou venosa 40 mL/kg/4 h", "Prova: <b>slide 32</b>"],
 "grupoC_tempo": ["Expansão do grupo C", "Slide 36: <b>20 mL/kg/hora</b>, reavaliação <b>clínica horária</b>, Ht após 2 h",
                  "Gabarito oficial 2025/2: “20 mL/kg <b>em 2 horas</b>”; fluxograma: reavaliação a cada 2 h",
                  "Escreva o <b>volume por kg</b> (30 kg = 600 mL), a reavaliação horária e o <b>Ht em 2 h</b> — é o que pontua"],
 "dengvaxia": ["Faixa etária da Dengvaxia", "Slide 42: <b>9–45 anos</b>", "Apostila MEDCURSO: 6–45 anos; Qdenga 4–60 (PNI: 10–14)", "Prova: <b>9–45</b> (slide)"],
}

FLASH = [
 [6, "Dengue: sorotipos e imunidade?", "4 sorotipos; imunidade permanente só ao mesmo."],
 [6, "Fase crítica: quando?", "Na defervescência, 3º–7º dia."],
 [6, "Caso suspeito na criança?", "Febre 2–7 dias sem foco em área de transmissão."],
 [6, "Quantos sinais de alarme para grupo C?", "Um basta."],
 [6, "Choque na dengue: PA diferencial?", "≤ 20 mmHg (convergente) + TEC > 2 s, pulso fino."],
 [6, "NS1 × IgM?", "NS1/PCR até o 5º dia; IgM a partir do 6º."],
 [6, "Prova do laço na criança?", "3 min, ≥ 10 petéquias em 2,5 × 2,5 cm."],
 [6, "Petéquias espontâneas sem alarme: grupo?", "B."],
 [6, "< 2 anos sem alarme: grupo?", "B (condição especial)."],
 [6, "Grupo A: volume por peso?", "≤ 10 kg 130 · 10–20 kg 100 · > 20 kg 80 mL/kg/dia; 1/3 SRO."],
 [6, "Antitérmico na dengue?", "Dipirona ou paracetamol; nunca AINE."],
 [6, "Grupo B: hidratação?", "VO supervisionada ≥ 50 mL/kg em 4–6 h na unidade."],
 [6, "Grupo B: quando vira C?", "Ht > 38%, alarme, recusa VO."],
 [6, "Grupo C: expansão?", "SF/RL 20 mL/kg/h até 3×, Ht após 2 h."],
 [6, "Grupo D: expansão?", "20 mL/kg em até 20 min até 3×, UTI."],
 [6, "Choque persistente com Ht subindo?", "Albumina."],
 [6, "Choque com Ht caindo?", "Hemorragia: concentrado de hemácias (+ plasma, vit K, crio)."],
 [6, "Qdenga: doses e soronegativo?", "2 doses com 3 meses; pode em soronegativo; não na lactante."],
]

COLA = [["Cap. 6 · Dengue", [
 ["Incubação", "4–7 d"], ["Fase crítica", "3º–7º dia (defervescência)"], ["NS1/PCR · IgM", "≤ 5º dia · ≥ 6º dia"],
 ["Laço criança", "3 min · ≥ 10"], ["Choque", "PA diferencial ≤ 20 · TEC > 2 s"], ["A", "130 / 100 / 80 mL/kg/dia · 1/3 SRO"],
 ["Hemograma A", "obrigatório < 5 anos"], ["B", "VO ≥ 50 mL/kg em 4–6 h · hemograma em 4 h"], ["B → C", "Ht > 38%"],
 ["C", "20 mL/kg/h até 3× · Ht 2 h"], ["D", "20 mL/kg em 20 min até 3× · UTI"], ["Ht ↑", "albumina"], ["Ht ↓ + choque", "hemácias"],
 ["Holliday-Segar", "100 · 1000+50 · 1500+20"], ["Dengvaxia", "9–45 a · soropositivo"], ["Qdenga", "2 doses / 3 m · não lactante"]]]]

KS = [
 {"id": "k_g_B", "cap": 6, "blk": ["g_grupos", "g_ab", "g_def"], "t": "Dengue com 15 kg e petéquias (caiu nas 3 provas)",
  "src": "Caiu nas 3 provas antigas (0,6–1,2 pt) — Profa. Patrícia",
  "enun": "Paciente de 3 anos (<b>15 kg</b>), febre de 39 °C há 5 dias. Sem vômitos nem sangramentos. Sem foco. Hidratado, com <b>petéquias em face</b>.",
  "p": [{"p": "Quais sinais de alarme pesquisar no exame físico? (0,6)",
         "m": "Dor abdominal intensa/à palpação · <b>hepatomegalia dolorosa</b> (&gt; 2 cm) · acúmulo de líquidos (ascite, derrame pleural/pericárdico) · <b>hipotensão postural/lipotimia</b> · sangramento de mucosas · <b>letargia ou irritabilidade</b> · (anamnese: vômitos persistentes, diurese diminuída; laboratório: Ht subindo, plaquetas caindo).",
         "c": ["dor abdominal", "hepatomegalia dolorosa", "ascite", "hipotensão postural", "sangramento de mucosa", "letargia", "irritabilidade"]},
        {"p": "Sem sinais de alarme: qual o grupo e qual o primeiro atendimento? (0,6)",
         "m": "<b>Grupo B</b> — petéquias = manifestação hemorrágica espontânea de pele, sem alarme. <b>Hemograma obrigatório</b> (até 4 h); <b>hidratação ORAL supervisionada</b> na unidade, antes do resultado, <b>≥ 50 mL/kg em 4–6 h = ≥ 750 mL</b>; reavaliar clínica, diurese, Ht e plaquetas; <b>Ht &gt; 38%</b>, alarme ou recusa da VO → venosa, conduta do <b>grupo C</b>. Sem anti-inflamatório; notificar.",
         "c": ["grupo B", "hemograma", "oral supervisionada", "50 mL/kg", "750 mL", "4 a 6 horas", "Ht > 38%"]}]},
 {"id": "k_g_C", "cap": 6, "blk": ["g_cd", "g_diag", "g_def"], "t": "Dengue com alarme, 30 kg, 4º dia (2025/2)",
  "src": "Prova 2025/2 · Q2 (1,6 pt) — gabarito mínimo oficial",
  "enun": "Escolar de 9 anos, <b>30 kg</b>, no <b>4º dia</b> de febre, com dor abdominal, vômitos persistentes, irritabilidade e hemoconcentração. PA 100 × 68 mmHg, pulsos cheios, TEC 2 s.",
  "p": [{"p": "Classifique. (0,4)",
         "m": "<b>Grupo C</b>: sinais de alarme (dor abdominal, vômitos persistentes, irritabilidade, hemoconcentração) <b>sem choque</b> (PA diferencial 32, pulsos cheios, TEC 2 s).",
         "c": ["grupo C", "sinais de alarme", "sem choque"]},
        {"p": "Qual exame confirmatório no 4º dia? (0,3)",
         "m": "<b>NS1 ou RT-PCR</b> (até o 5º dia); sorologia IgM só a partir do 6º.",
         "c": ["NS1", "PCR", "IgM a partir do 6º dia"]},
        {"p": "Qual a conduta inicial? (0,9)",
         "m": "<b>Internação</b>, acesso venoso, <b>SF 0,9% ou Ringer 20 mL/kg = 600 mL em 1 hora</b>, reavaliação clínica <b>horária</b> e <b>Ht após 2 h</b>; até 3 expansões; melhorou → manutenção (Holliday-Segar: 1500 + 20 × 10 = <b>1700 mL/dia</b>) + reposição de perdas; não melhorou → conduta D.",
         "c": ["internação", "20 mL/kg", "600 mL", "reavaliação horária", "hematócrito após 2 horas", "3 expansões", "Holliday-Segar"]}]},
]
