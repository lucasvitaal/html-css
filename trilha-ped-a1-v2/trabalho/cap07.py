CAP = {"n": 7, "t": "Hepatites virais", "short": "Hepatites", "aula": "Aula 7 · slides da Patrícia",
       "icon": "🟡", "col": "#B07D3A",
       "bul": ["Nunca caiu nas provas antigas — revisar rápido, sem descuidar",
               "B aguda = HBsAg + anti-HBc IgM · crônica = HBsAg + anti-HBc IgG/total",
               "RN de mãe HBsAg+: vacina + IGHAHB nas primeiras 24 h (slide), músculos diferentes",
               "HCV &lt; 18 meses: anti-HCV pode ser materno → PCR decide"],
       "medalha": ["🟡", "Leitor de sorologia"]}

BLOCKS = [
 {"id": "h_A", "t": "Hepatite A: fecal-oral, silenciosa na criança, não cronifica",
  "s": "Transmissão <b>fecal-oral</b> (saneamento, creche). Viremia do início dos sintomas ao fim da icterícia. "
       "<br><b>Assintomática em 70% dos &lt; 6 anos</b> (só 30% dos maiores/adultos); tríade <b>colúria, hipocolia, icterícia</b>. Cura em 30–40 dias; 15% prolongada (&lt; 6 meses). <b>Não cronifica.</b> "
       "<br>Anti-HAV <b>IgM</b> = aguda (a partir de 5–10 dias, por 1–2 meses); <b>IgG</b> = infecção passada ou vacina, por toda a vida. "
       "<br>Vacina: <b>SUS dose única aos 15 meses</b>; SBP/SBIm 2 doses (12 e 18 meses).",
  "fala": "Hepatite A se pega pela via fecal-oral e circula muito em creche. Na criança pequena ela costuma ser silenciosa: setenta por cento dos menores de seis anos não têm sintoma, e por isso eles são o reservatório que contamina os adultos, que ficam ictéricos. Ela cura em trinta a quarenta dias e não cronifica. Igê eme positivo é infecção aguda; igê gê é infecção passada ou vacina. No SUS, a vacina é dose única aos quinze meses.",
  "pega": "Hepatite A <b>não cronifica</b>. Anti-HAV <b>IgG</b> positivo <b>não</b> é infecção aguda. SUS: <b>dose única 15 meses</b>.",
  "z": "Na creche as crianças pegam hepatite A sem nem perceber e quem fica amarela é a professora. Lava a mão depois da fralda, porra.",
  "ills": ["h_A"]},
 {"id": "h_B", "t": "Hepatite B: transmissão e o risco de cronificar",
  "s": "~300 milhões de portadores (OMS). Transmissão por <b>sangue, sêmen e saliva</b> (slide); na criança: <b>perinatal (vertical)</b> e intrafamiliar (14–60%). <b>HBeAg</b> = replicação, mais infectante. "
       "<br><b>Quanto mais cedo a infecção, maior a cronificação</b>: filho de mãe <b>HBsAg+/HBeAg+ → 70–90%</b>; HBsAg+/HBeAg− → 10–40%. As crônicas vêm da infância → <b>cirrose e hepatocarcinoma</b>.",
  "fala": "A hepatite B passa por sangue, sêmen e saliva, e na criança a via principal é a vertical, na hora do parto, além da transmissão dentro de casa. A regra de ouro é que quanto mais cedo a infecção, maior a chance de cronificar: filho de mãe com antígeno de superfície e antígeno e positivos cronifica em setenta a noventa por cento. E são essas crônicas da infância que viram cirrose e câncer de fígado no adulto.",
  "div": "hb_tv",
  "pega": "Mesmo mãe <b>HBeAg negativa</b> tem risco (10–40%): a profilaxia do RN <b>independe</b> do HBeAg.",
  "z": "Hepatite B pega cedo é hepatite B pra vida toda: setenta a noventa por cento de cronificação no filho de mãe com HBeAg positivo. Protege esse bebê na sala de parto, caralho.",
  "ills": ["h_B"]},
 {"id": "h_marc", "t": "Marcadores da hepatite B (o slide inteiro em negrito)",
  "s": "<b>HBsAg</b> = presença do vírus (infecção). <b>Anti-HBc IgM</b> = infecção <b>aguda</b>. <b>Anti-HBc IgG/total</b> = contato com o vírus (passado ou crônico). <b>Anti-HBs</b> = imunidade. <b>HBeAg</b> = replicação / anti-HBe = soroconversão. "
       "<br><b>Aguda</b> = <b>HBsAg + anti-HBc IgM</b>. <b>Crônica</b> = <b>HBsAg + anti-HBc IgG/total</b> (HBsAg &gt; 6 meses). "
       "<br><b>Curada</b> = anti-HBc total + anti-HBs, HBsAg negativo. <b>Vacinado</b> = <b>só anti-HBs</b> (a vacina só tem HBsAg). PCR (DNA) só para quem vai tratar.",
  "fala": "O slide que a professora pôs inteiro em negrito é o dos marcadores. Hepatite B aguda é antígeno de superfície positivo com anti core igê eme. Crônica é antígeno de superfície positivo com anti core igê gê, ou total, persistindo além de seis meses. Quem se curou tem anti core e anti superfície, sem o antígeno. E o vacinado tem só o anti superfície, porque a vacina contém apenas o antígeno de superfície e nunca mostra o core ao sistema imune.",
  "pega": "Vacinado = <b>só anti-HBs</b>. Anti-HBc positivo = <b>viu o vírus</b> (nunca é só vacina).",
  "z": "Anti core positivo é carimbo de quem encontrou o vírus de verdade; vacina não deixa esse carimbo. Leu errado, tratou o vacinado como curado, porra.",
  "m": [["MEDCURSO · S27 P1 16:45–17:39", "A vacina contém só o HBsAg, então gera apenas anti-HBs."]],
  "ills": ["h_marc"]},
 {"id": "h_marc_idade", "t": "Filho de mãe HBsAg+: o que dosar em cada idade",
  "s": "<b>&lt; 6 meses</b>: <b>não dosar</b> (resultado transitório/materno). "
       "<br><b>6–12 meses</b> (exposto): HBsAg + VHB-DNA. "
       "<br><b>&gt; 12 meses</b>: <b>HBsAg e repetir em 6 meses</b> se positivo → confirma <b>crônica</b> (persistência).",
  "fala": "Na criança exposta, a idade define o exame. Antes dos seis meses não se dosa, porque o resultado pode ser transitório. Entre seis e doze meses, pede antígeno de superfície e DNA viral. Acima de doze meses, pede o antígeno de superfície e, se vier positivo, repete em seis meses: só a persistência confirma hepatite B crônica.",
  "pega": "Um HBsAg positivo isolado <b>não</b> prova cronicidade: <b>repetir em 6 meses</b>.",
  "z": "Um exame positivo é foto; crônica é filme de seis meses. Repete o antígeno antes de carimbar a criança, caralho.",
  "ills": ["h_marc_idade"]},
 {"id": "h_prevB", "t": "Prevenção da B: calendário e RN exposto",
  "s": "Vacina <b>ao nascer</b> (primeiras 12–24 h) + <b>pentavalente aos 2, 4 e 6 meses</b>. Prematuro <b>&lt; 33 sem</b> (ou &lt; 2 kg): <b>4 doses</b>. Não vacinado <b>≥ 7 anos</b>: hepatite B isolada <b>0-1-6</b> (penta só até 7 anos). Slide: adolescentes até 19 anos e grupos de risco; hoje: toda a população. "
       "<br><b>RN de mãe HBsAg+</b>: <b>vacina + imunoglobulina (IGHAHB)</b>, <b>preferencialmente nas primeiras 24 h</b> (slide) — MEDCURSO 12 h —, em <b>grupamentos musculares diferentes</b>, independentemente do HBeAg. <b>Amamentação liberada.</b>",
  "fala": "A vacina da hepatite B é dada ao nascer e depois aos dois, quatro e seis meses, na pentavalente; o prematuro abaixo de trinta e três semanas recebe quatro doses. O recém-nascido de mãe com antígeno de superfície positivo recebe vacina mais imunoglobulina específica, de preferência nas primeiras vinte e quatro horas, em músculos diferentes, e pode mamar normalmente. Não se dosa o antígeno do bebê antes de decidir.",
  "div": "ighahb",
  "pega": "RN exposto: <b>vacina + IGHAHB juntas</b>, músculos diferentes, <b>≤ 24 h</b>; HBeAg negativo da mãe <b>não dispensa</b>; aleitamento <b>permitido</b>.",
  "z": "Mãe com antígeno de superfície positivo: vacina numa coxa, imunoglobulina na outra, antes de vinte e quatro horas, e deixa o bebê mamar. Simples assim, porra.",
  "m": [["MEDCURSO · S27 P1 21:17–22:44", "Vacina + IGHAHB, de preferência em 12 h, juntas (vacina não viva não sofre interferência)."],
        ["MEDCURSO · S27 P1 20:00–20:47", "Pentavalente só até 7 anos; depois, hepatite B isolada 0-1-6."]],
  "ills": ["h_prevB"]},
 {"id": "h_C", "t": "Hepatite C na criança",
  "s": "Antiga “não A, não B”; <b>mutações → sem imunidade protetora, sem vacina</b>; <b>&gt; 80% cronifica</b>, raramente sintomática na fase aguda. "
       "<br>Via da criança: <b>vertical</b> (~5%; 10% com coinfecção HIV; slide: cesárea, sangue materno, alta viremia). "
       "<br><b>Anti-HCV</b> (20–150 dias) = <b>contato</b>; <b>RNA-VHC (PCR)</b> (7–21 dias) = <b>vírus circulante</b>. "
       "<br><b>&lt; 18 meses</b>: anti-HCV pode ser <b>IgG materna</b> → <b>PCR com 3 meses</b> e repetir 6–12 meses após. Viremia pode clarear até 3–4 anos.",
  "fala": "A hepatite C cronifica em mais de oitenta por cento, quase sempre sem sintomas, e não tem vacina. Na criança, a via é a vertical. A armadilha de prova é o lactente filho de mãe com hepatite C que tem anticorpo positivo: antes dos dezoito meses esse anticorpo pode ser da mãe, que atravessou a placenta. Quem decide é o PCR do RNA viral, feito a partir dos três meses e repetido depois.",
  "div": "hcv_cesar",
  "pega": "Anti-HCV + em &lt; <b>18 meses</b> = pode ser <b>materno</b> → <b>PCR</b>. Não existe vacina contra hepatite C.",
  "z": "Anticorpo de hepatite C positivo num bebê de cinco meses é presente da mãe, não diagnóstico. PCR decide, porra.",
  "ills": ["h_C"]},
 {"id": "h_dif", "t": "Icterícia no lactente: colestase e atresia de vias biliares",
  "s": "<b>Colúria + hipocolia/acolia</b> = bilirrubina <b>direta</b>. <b>BD &gt; 1 mg/dL</b> = colestase → investigar com urgência. "
       "<br><b>Atresia de vias biliares</b>: icterícia que persiste após 2 semanas, fezes claras → <b>cirurgia de Kasai antes de 8 semanas</b> (depois disso, benefício cai muito). "
       "<br>Icterícia do leite materno: só <b>indireta</b>, fezes normais.",
  "fala": "Icterícia no lactente de semanas com urina escura e fezes claras não é icterícia do leite materno: é bilirrubina direta, e direta acima de um é colestase. A grande urgência é a atresia de vias biliares, porque a cirurgia de Kasai precisa ser feita antes de oito semanas de vida. A icterícia do leite materno eleva só a indireta e as fezes continuam amarelas.",
  "pega": "Fezes claras + urina escura = <b>BD</b> → <b>atresia</b> até prova em contrário; <b>Kasai &lt; 8 semanas</b>. Fototerapia não trata colestase.",
  "z": "Cocô branco e xixi cor de Coca-Cola num bebê de cinco semanas: fração da bilirrubina hoje, porque o relógio do Kasai está correndo, caralho.",
  "m": [["MEDCURSO · S08 39:19–43:56", "Bilirrubina direta &gt; 1 = colestase; Kasai sem benefício a partir de 8 semanas."]],
  "ills": ["h_dif"]},
]

ILLS = {
 "h_A": cards("Hepatite A", [
     ("🚰", "Fecal-oral", "saneamento, creche", "t"),
     ("🤫", "Silenciosa", "assintomática em 70% dos < 6 anos", "a"),
     ("✅", "Não cronifica", "cura em 30–40 dias · 15% prolongada", "g"),
     ("💉", "Vacina", "SUS dose única 15 m · SBP 12 e 18 m", "p")],
     foot="Anti-HAV IgM = aguda · IgG = passada ou vacina", fcor="t"),
 "h_B": table("Hepatite B: risco de cronificar pelo momento da infecção", [
     ("Mãe HBsAg+ / HBeAg+", "70–90% no filho"), ("Mãe HBsAg+ / HBeAg−", "10–40%"),
     ("Transmissão (slide)", "sangue, sêmen e saliva · vertical e intrafamiliar"),
     ("HBeAg", "replicação = mais infectante"), ("Desfecho", "crônicas da infância → cirrose e hepatocarcinoma")], cor="a",
     foot="Quanto mais cedo a infecção, maior a cronificação"),
 "h_marc": table("Marcadores da hepatite B", [
     ("Aguda", "HBsAg + anti-HBc IgM"), ("Crônica", "HBsAg (> 6 m) + anti-HBc IgG/total"),
     ("Curada", "anti-HBc total + anti-HBs · HBsAg negativo"), ("Vacinado", "só anti-HBs"),
     ("Replicação", "HBeAg (anti-HBe = soroconversão)"), ("PCR (DNA)", "só para quem vai tratar")], cor="v",
     foot="Anti-HBc positivo = viu o vírus (nunca é só vacina)"),
 "h_marc_idade": flow("Criança exposta: o que dosar", [
     ("🍼", "< 6 meses", "não dosar (resultado transitório)", "t"),
     ("🧪", "6–12 meses", "HBsAg + VHB-DNA", "a"),
     ("🔁", "> 12 meses", "HBsAg e repetir em 6 meses se positivo → crônica", "v")]),
 "h_prevB": flow("Hepatite B: calendário e RN exposto", [
     ("👶", "Ao nascer", "1ª dose nas primeiras horas", "g"),
     ("💉", "2, 4 e 6 meses", "pentavalente · prematuro < 33 sem: 4 doses", "g"),
     ("🔢", "≥ 7 anos não vacinado", "hepatite B isolada 0-1-6", "t"),
     ("🛡️", "RN de mãe HBsAg+", "vacina + IGHAHB ≤ 24 h, músculos diferentes · pode mamar", "r")]),
 "h_C": versus("Hepatite C: anticorpo × PCR", ("🧫", "Anti-HCV", "a", [
     "• 20–150 dias", "• = contato", "✘ < 18 meses: pode ser IgG materna"]),
     ("🧬", "RNA-VHC (PCR)", "g", [
     "• 7–21 dias", "• = vírus circulante", "✔ decide no lactente", "• com 3 m, repetir 6–12 m após"]),
     foot="> 80% cronifica · sem vacina · vertical ~5% (HIV 10%)"),
 "h_dif": flow("Icterícia com colúria e acolia", [
     ("🚽", "Urina escura + fezes claras", "bilirrubina direta", "a"),
     ("🧪", "BD > 1 mg/dL", "colestase → investigar já", "r"),
     ("🔪", "Atresia de vias biliares", "Kasai antes de 8 semanas", "r")],
     foot="Icterícia do leite materno: só indireta, fezes normais", fcor="t"),
}

QMAP = {0: ["h_marc"], 1: ["h_marc"], 2: ["h_prevB"], 3: ["h_C"], 4: ["h_A"], 5: ["h_prevB", "h_A"], 6: ["h_dif"], 7: ["h_marc_idade"]}

DIV = {
 "hb_tv": ["Números da transmissão perinatal da B", "Slide 12: <b>70–90%</b> (HBeAg+) e <b>10–40%</b> (HBeAg−)", "Apostila MEDCURSO: 90% / 10%", "Prova: <b>slide</b>"],
 "ighahb": ["Prazo da imunoglobulina no RN exposto", "Slide 17: “preferencialmente nas primeiras <b>24 h</b>”",
            "MEDCURSO/apostila: vacina + IG em <b>12 h</b>; IG até 7 dias", "Faculdade: <b>24 h</b>; residência: protocolo vigente (12 h)"],
 "hcv_cesar": ["Cesariana na hepatite C", "Slide 20: cesariana = <b>maior risco</b> de transmissão",
               "Diretrizes usuais: via de parto não muda a transmissão (não se indica cesárea para prevenir)", "Prova: cite o slide; saiba que diretrizes não indicam cesárea"],
}

FLASH = [
 [7, "Hepatite A: % assintomática em < 6 anos?", "70%."],
 [7, "Hepatite A cronifica?", "Não."],
 [7, "Vacina hepatite A no SUS?", "Dose única aos 15 meses."],
 [7, "Hepatite B aguda: marcadores?", "HBsAg + anti-HBc IgM."],
 [7, "Hepatite B crônica: marcadores?", "HBsAg (> 6 m) + anti-HBc IgG/total."],
 [7, "Vacinado: perfil?", "Só anti-HBs."],
 [7, "Curado: perfil?", "Anti-HBc total + anti-HBs, HBsAg negativo."],
 [7, "Cronificação no filho de mãe HBsAg+/HBeAg+?", "70–90%."],
 [7, "RN de mãe HBsAg+: conduta?", "Vacina + IGHAHB ≤ 24 h (slide), músculos diferentes; pode mamar."],
 [7, "Prematuro < 33 sem: doses de hepatite B?", "4."],
 [7, "≥ 7 anos não vacinado?", "Hepatite B isolada 0-1-6."],
 [7, "> 12 meses com HBsAg+: próximo passo?", "Repetir HBsAg em 6 meses."],
 [7, "Hepatite C: % cronificação?", "> 80%."],
 [7, "Anti-HCV + em lactente de 5 meses?", "Pode ser IgG materna → PCR (RNA-VHC)."],
 [7, "Colúria + acolia no lactente?", "Bilirrubina direta → investigar atresia; Kasai < 8 semanas."],
]

COLA = [["Cap. 7 · Hepatites", [
 ["A assintomática", "70% < 6 anos"], ["A vacina SUS", "dose única 15 m"], ["B aguda", "HBsAg + anti-HBc IgM"],
 ["B crônica", "HBsAg + anti-HBc IgG/total"], ["Vacinado", "só anti-HBs"], ["Cronificação perinatal", "HBeAg+ 70–90% · HBeAg− 10–40%"],
 ["RN exposto", "vacina + IGHAHB ≤ 24 h"], ["Calendário B", "nascer + penta 2-4-6"], ["< 33 sem", "4 doses"],
 ["> 12 m", "HBsAg + repetir em 6 m"], ["C", "> 80% cronifica · sem vacina"], ["C < 18 m", "PCR (anti-HCV pode ser materno)"],
 ["Colestase", "BD > 1 · Kasai < 8 sem"]]]]

KS = [
 {"id": "k_h_rn", "cap": 7, "blk": ["h_prevB", "h_marc", "h_B"], "t": "A gestante HBsAg+ e o filho",
  "src": "Caso autoral no estilo da professora (slides 12, 14, 16, 17) — tema nunca caiu",
  "enun": "Gestante de 24 anos chega em trabalho de parto com sorologia do pré-natal: <b>HBsAg reagente, anti-HBc IgG reagente, anti-HBc IgM não reagente, HBeAg reagente</b>. O RN nasce a termo, 3.200 g, de parto vaginal.",
  "p": [{"p": "Interprete a sorologia materna e o risco para o RN.",
         "m": "<b>Hepatite B crônica</b> (HBsAg + anti-HBc IgG, sem IgM) <b>com replicação</b> (HBeAg+). Risco de infecção crônica no filho sem profilaxia: <b>70–90%</b>.",
         "c": ["hepatite B crônica", "anti-HBc IgG", "HBeAg", "replicação", "70 a 90%"]},
        {"p": "Qual a conduta com o RN?",
         "m": "<b>Vacina hepatite B + imunoglobulina (IGHAHB)</b>, <b>preferencialmente nas primeiras 24 h</b> (MEDCURSO: 12 h), em <b>grupamentos musculares diferentes</b>; completar o esquema (pentavalente 2-4-6 meses). <b>Não</b> dosar HBsAg do RN ao nascer. <b>Aleitamento liberado.</b>",
         "c": ["vacina", "IGHAHB", "24 horas", "músculos diferentes", "pentavalente", "aleitamento"]},
        {"p": "Aos 15 meses o HBsAg da criança veio reagente. O que fazer para confirmar cronicidade?",
         "m": "Acima de 12 meses: <b>repetir o HBsAg em 6 meses</b>; persistência confirma hepatite B <b>crônica</b>.",
         "c": ["repetir HBsAg", "6 meses", "crônica"]}]},
]
