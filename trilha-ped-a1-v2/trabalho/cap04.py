CAP = {"n": 4, "t": "Adenomegalias e câncer infantil", "short": "Adenomegalias", "aula": "Aula 4 · slides da Patrícia",
       "icon": "🔎", "col": "#22666A",
       "bul": ["Adenite submandibular + supraclavicular: caiu 3× (até 2,6 pts)",
               "Suspeição (slide 12): ~4 sem · supraclavicular · &gt; 2–3 cm · duro, fixo, progressivo",
               "Supraclavicular D → tórax · E → abdome",
               "Câncer: LLA 80% · SNC 95% com achado neurológico · Wilms massa assintomática"],
       "medalha": ["🔎", "Palpador de gânglio"]}

BLOCKS = [
 {"id": "a_base", "t": "Linfonodo normal da criança",
  "s": "Linfonodo captura antígenos da região que drena. O <b>tecido linfoide cresce até a puberdade</b> (supera o do adulto); gânglios cervicais e inguinais pequenos são comuns. <b>Sombra tímica</b> no RX até <b>3 anos</b>. "
       "<br><b>Hiperplasia reacional</b> = maior causa de adenomegalia. "
       "<br><b>Generalizada</b> = mais de duas cadeias <b>não contíguas</b> (slide 11).",
  "fala": "Criança tem mais tecido linfoide que adulto, então gânglio palpável pequeno no pescoço ou na virilha é comum, e a causa mais frequente de aumento é a hiperplasia reacional a uma infecção da região drenada. No raio-x de tórax, a sombra do timo é normal até os três anos. E a definição de generalizada da aula é aumento em mais de duas cadeias que não são vizinhas.",
  "pega": "Sombra tímica é normal <b>até 3 anos</b>; mediastino alargado num adolescente <b>não</b> é timo.",
  "z": "Gânglio de ervilha no pescoço de pré-escolar é a imunidade trabalhando, não é linfoma. Calma, porra.",
  "ills": ["a_base"]},
 {"id": "a_aval", "t": "Critérios de suspeição (slide 12, em vermelho)",
  "s": "Benigno se &lt; 2 semanas. <b>Suspeitar / biopsiar</b>: duração ~<b>4 semanas</b> sem regressão · <b>supraclavicular</b> (também cervical inferior e epitroclear) · <b>&gt; 2–3 cm</b> · <b>aumento progressivo</b> · <b>endurecido e fixo</b> · sintomas sistêmicos (febre, perda de peso, sudorese) · idade maior (malignidade ↑ com a idade). "
       "<br>Causas: <b>75% infecciosas</b>, 20% embrionárias/outras, <b>5% neoplasias</b>.",
  "fala": "O slide em vermelho da aula traz os critérios que fazem pensar em doença séria: gânglio que não regride em cerca de quatro semanas, localização supraclavicular, tamanho maior que dois a três centímetros, crescimento progressivo e consistência endurecida e fixa, além de febre, perda de peso ou sudorese. Mesmo assim, três quartos das adenomegalias da criança são infecciosas e só cinco por cento são neoplasias.",
  "div": "aden_corte",
  "pega": "Supraclavicular <b>nunca</b> é “só reacional”. Tempo de biópsia: ~<b>4 semanas</b> sem regressão.",
  "z": "Gânglio supraclavicular, duro, grudado e crescendo há um mês: não é íngua, é biópsia, porra.",
  "ills": ["a_aval"]},
 {"id": "a_etio", "t": "Agudo × crônico, uni × bilateral: o agente provável",
  "s": "<b>Aguda bilateral</b> → <b>viroses</b> respiratórias. <b>Aguda unilateral</b> → <b><i>S. aureus</i> / estreptococo do grupo A</b> (adenite piogênica). "
       "<br><b>Crônica unilateral</b> → <b>micobactéria atípica</b>, <b>arranhadura do gato</b> (<i>Bartonella henselae</i>). <b>Crônica bilateral</b> → <b>EBV, CMV</b>, toxoplasmose. "
       "<br>Aguda &lt; 2 semanas; subaguda 2–6; crônica &gt; 6.",
  "fala": "Um jeito rápido de pensar no agente é cruzar tempo e lado. Gânglio agudo dos dois lados é virose respiratória. Agudo de um lado só, quente e doloroso, é adenite por estafilococo ou estreptococo. Crônico de um lado só lembra micobactéria atípica e doença da arranhadura do gato. Crônico dos dois lados lembra Epstein-Barr, citomegalovírus e toxoplasmose.",
  "pega": "Aguda <b>unilateral</b> inflamada = <b>S. aureus/estrepto</b>; crônica unilateral sem flogose = <b>micobactéria atípica / gato</b>.",
  "z": "Gânglio de um lado, crônico, e um gato novo em casa? Pergunta do gato antes de pedir biópsia, caralho.",
  "ills": ["a_etio"]},
 {"id": "a_infl", "t": "Inflamatório × neoplásico e a regra da supraclavicular",
  "s": "<b>Inflamatório</b>: <b>doloroso</b>, pele quente/hiperemiada, <b>flutuação</b>, fístula. "
       "<br><b>Neoplásico</b>: <b>duro, aderido, indolor</b>, confluente (pacote), <b>supraclavicular</b>, ≥ 2,5 cm. "
       "<br><b>Supraclavicular direita → tórax</b> (mediastino, pulmão) · <b>esquerda → abdome</b> (sinal de Virchow).",
  "fala": "À palpação, gânglio inflamatório dói, tem pele quente e vermelha e pode flutuar ou fistulizar. Gânglio neoplásico é duro, aderido aos planos, indolor e costuma formar pacotes. E a regra de prova da supraclavicular: a direita drena o tórax, então pense em lesão intratorácica; a esquerda drena o abdome, então pense em tumor ou processo inflamatório abdominal.",
  "pega": "Supraclavicular <b>D = tórax</b>; <b>E = abdome</b>. Duro, aderido e indolor = neoplásico até prova em contrário.",
  "z": "Direita olha pro peito, esquerda olha pra barriga. Trocou os lados na prova, perdeu ponto e ainda pediu o exame errado, porra.",
  "ills": ["a_infl"]},
 {"id": "a_adenite", "t": "Adenite aguda localizada: conduta e doses (slide 29)",
  "s": "Localizada, <b>sem sinais de gravidade</b>, inflamatória, cervical superior/submandibular, geralmente com porta de entrada (piodermite, dente, orofaringe) → <b>hemograma, VHS, PCR</b>. "
       "<br>Antibiótico <b>oral por 10 dias</b> cobrindo <i>S. aureus</i> e estrepto: <b>cefalexina 25–50 mg/kg/dia 6/6 h</b> · cefuroxima 20–30 mg/kg/dia 12/12 h · azitromicina 10 mg/kg no 1º dia → 5 mg/kg/dia por mais 4 dias · <b>clindamicina 10–20 mg/kg/dia</b> (6/6 ou 8/8 h) se MRSA/anaeróbio. "
       "<br><b>Reavaliar em 24–48 h</b>; <b>flutuação → punção aspirativa/drenagem</b>; sem resposta ou persistência &gt; 4 semanas → <b>biópsia</b>.",
  "fala": "Gânglio único, submandibular, doloroso, quente e com o centro flutuante numa criança em bom estado é adenite piogênica. Pede hemograma e provas inflamatórias e trata por via oral por dez dias, cobrindo estafilococo e estreptococo; a droga da aula é a cefalexina, vinte e cinco a cinquenta miligramas por quilo por dia, de seis em seis horas. Reavalia em vinte e quatro a quarenta e oito horas; se flutuar, punciona ou drena; se não melhorar, biópsia.",
  "div": "azitro",
  "pega": "Tamanho isolado não indica biópsia num gânglio <b>agudo inflamado</b>: primeiro <b>antibiótico 10 dias</b>; flutuação → <b>drenagem</b>; sem resposta → biópsia.",
  "z": "Gânglio quente, vermelho e flutuando é pus pedindo saída. Cefalexina, reavalia em quarenta e oito horas e, se flutuar, drena essa porra.",
  "ills": ["a_adenite"]},
 {"id": "a_grav", "t": "Adenomegalia com gravidade ou generalizada: os fluxos",
  "s": "<b>Localizada com sinais de gravidade</b> ou <b>generalizada com estado geral comprometido</b> → <b>hemograma, VHS/PCR, RX de tórax</b>: "
       "<br>• <b>blastos / pancitopenia</b> → <b>mielograma</b> (leucemia); "
       "<br>• <b>mediastino alargado</b> → TB, linfoma, sarcoidose, outros → PPD/TC → <b>biópsia</b>; "
       "<br>• <b>exames normais</b> → <b>biópsia</b> do gânglio mais significativo mesmo assim. "
       "<br><b>Generalizada em bom estado</b> → sorologias <b>EBV, CMV, toxoplasmose</b> (HIV conforme risco) + RX.",
  "fala": "Quando a adenomegalia vem com sinais de gravidade, ou é generalizada numa criança doente, o caminho é hemograma, provas inflamatórias e raio-x de tórax. Blastos ou pancitopenia levam ao mielograma, porque é leucemia até prova em contrário. Mediastino alargado leva à investigação de tuberculose, linfoma e outros tumores, com biópsia. E se tudo vier normal, biopsia o gânglio mais significativo assim mesmo. Generalizada em criança bem começa por sorologias.",
  "pega": "Generalizada + palidez + petéquias + visceromegalia: o próximo passo é <b>hemograma</b> (→ mielograma), não biópsia do gânglio.",
  "z": "Criança pálida, cheia de petéquia, com fígado e baço grandes e gânglio em todo lugar: não é virose, é medula gritando. Hemograma agora e mielograma depois, caralho.",
  "ills": ["a_grav"]},
 {"id": "a_bcg", "t": "Linfonodo pós-BCG",
  "s": "Linfonodo <b>axilar direito</b> (drenagem do deltoide direito vacinado). "
       "<br>Slide 32 (aula): <b>notificar + isoniazida</b>, com ou sem sinais flogísticos. "
       "<br>MEDCURSO/protocolo: gânglio &lt; 3 cm é evolução esperada (~10%); &gt; 3 cm <b>não supurado</b> → acompanhar; <b>supurado</b> → isoniazida; <b>não puncionar</b> gânglio supurado pós-BCG.",
  "fala": "O gânglio da axila direita depois da BCG é a drenagem do deltoide direito, onde a vacina foi aplicada. A aula da faculdade é simples: notificar e dar isoniazida, com ou sem sinais inflamatórios. O protocolo, ensinado no cursinho, é mais conservador: gânglio pequeno é evolução esperada, o grande sem supuração só se acompanha, e a isoniazida fica para o supurado, que não se punciona.",
  "div": "bcg",
  "pega": "Prova da faculdade: <b>notificar + isoniazida</b> (slide 32). Nunca punção do gânglio pós-BCG supurado.",
  "z": "Caroço na axila direita de bebê vacinado é a BCG dando oi, não é linfoma. Notifica e isoniazida, que é o que a Patrícia quer, porra.",
  "m": [["MEDCURSO · S27 03:38–09:58", "Isoniazida para linfadenopatia supurada; &lt; 3 cm é esperado em ~10%; &gt; 3 cm não supurado só se acompanha; não puncionar."]],
  "ills": ["a_bcg"]},
 {"id": "a_cisto", "t": "Massas cervicais que não são gânglio",
  "s": "<b>Cisto do ducto tireoglosso</b>: <b>mediano</b>, sobe com a deglutição/protrusão da língua. "
       "<br><b>Cisto branquial</b>: <b>lateral</b>, borda anterior do esternocleidomastóideo. "
       "<br><b>Linfangioma / higroma cístico</b>: volumoso, mole, aparece cedo, aumenta com infecções. "
       "<br><b>Hemangioma</b>: vascular, avermelhado/arroxeado.",
  "fala": "Nem toda massa no pescoço é gânglio. Na linha média, que sobe quando a criança engole ou põe a língua para fora, é o cisto do ducto tireoglosso. Lateral, na borda do esternocleidomastóideo, é o cisto branquial. A massa grande, mole, que aparece cedo e cresce com infecções é o linfangioma, ou higroma cístico. E o hemangioma é a lesão vascular, avermelhada.",
  "pega": "Massa <b>mediana</b> que sobe com a língua = <b>tireoglosso</b>; <b>lateral</b> = branquial.",
  "z": "Caroço bem no meio do pescoço que sobe quando a criança mostra a língua? Tireoglosso. Não vai tratar com cefalexina, caralho.",
  "ills": ["a_cisto"]},
 {"id": "a_cancer", "t": "Câncer infantil: por que diagnosticar cedo",
  "s": "Não prevenível; <b>2–6%</b> dos cânceres; latência curta, crescimento rápido, sintomas vagos (imitam doenças comuns). <b>70–80% de cura</b> se diagnosticado cedo. Mensagem da aula: <b>não alarmar os pais, mas investigar precocemente</b>. "
       "<br>Alertas: palidez/pancitopenia, febre persistente, emagrecimento, hepatoesplenomegalia, gânglio duro/aderido/supraclavicular, mediastino alargado. "
       "<br><b>Campanha — 10 sinais</b>: dor óssea/abdominal, febre &gt; 1 semana, manchas roxas/sangramento, caroço, prurido sem lesão, cansaço/palidez, perda de peso, cefaleia matinal com vômitos, abdome que cresce, infecção que não melhora (+ leucocoria/estrabismo).",
  "fala": "O câncer da criança não se previne, mas se cura em setenta a oitenta por cento quando o diagnóstico é precoce. O problema é que ele cresce rápido e imita doença comum, com febre, palidez, dor e cansaço. A mensagem da professora é não alarmar a família, mas investigar cedo. Os sinais da campanha são dor óssea, febre por mais de uma semana, manchas roxas, caroço, palidez, perda de peso, cefaleia matinal com vômito e barriga que cresce.",
  "div": "cura",
  "pega": "Cura <b>70–80%</b> se precoce (número da professora). A conduta errada é <b>atrasar</b> o diagnóstico com antibiótico empírico.",
  "z": "Febre há duas semanas, palidez e manchas roxas não é virose que passa: é investigar hoje, porque o tempo é o que mais mata nesse câncer, porra.",
  "ills": ["a_cancer"]},
 {"id": "a_leuc", "t": "Leucemias e linfomas",
  "s": "<b>LLA</b>: <b>80%</b> das leucemias, pico <b>2–4 anos</b>; LMA 15–20% (&lt; 1 ano e adolescente). Pode começar com <b>dor óssea</b> e hemograma ainda normal. Falência medular: palidez, petéquias, infecções; hepatoesplenomegalia, adenomegalia. Diagnóstico: <b>mielograma</b>. "
       "<br><b>Hodgkin</b>: 15–40 anos, gânglio cervical/supraclavicular indolor &gt; 2 semanas. "
       "<br><b>Burkitt</b>: &lt; 10 anos, <b>abdome</b> ou mandíbula, crescimento rapidíssimo. <b>Linfoblástico</b>: &gt; 10 anos, <b>massa mediastinal</b> (50–70%), derrame, <b>compressão de via aérea</b> → urgência.",
  "fala": "A leucemia linfoide aguda é oitenta por cento das leucemias da criança, com pico entre dois e quatro anos, e pode abrir o quadro só com dor óssea. A falência da medula aparece como palidez, petéquias e infecções, e quem confirma é o mielograma. Nos linfomas, Hodgkin é do adolescente com gânglio cervical indolor; Burkitt é da criança menor, no abdome ou na mandíbula; e o linfoblástico é o adolescente com massa no mediastino que pode comprimir a via aérea.",
  "pega": "Adolescente com tosse, dispneia ao deitar e <b>mediastino alargado</b> = <b>linfoma linfoblástico</b> → risco de <b>compressão de via aérea</b> (não sedar/deitar sem avaliação).",
  "z": "Adolescente que não consegue deitar e tem mediastino gordo no raio-x não é pneumonia: é massa apertando a traqueia. Investigação urgente, caralho.",
  "ills": ["a_leuc"]},
 {"id": "a_solidos", "t": "Tumores sólidos: SNC, Wilms, neuroblastoma, osso, olho",
  "s": "<b>SNC</b>: tumor <b>sólido</b> maligno mais comum; <b>95%</b> das crianças com cefaleia por tumor têm <b>achado neurológico</b> (marcha, papiledema, estrabismo, queda escolar). "
       "<br><b>Wilms</b>: <b>3–4 anos</b>, <b>massa abdominal assintomática</b> achada pelos pais (<b>60%</b>), HAS (25%), hematúria (15%). <b>Neuroblastoma</b>: pico <b>2 anos</b>, criança <b>doente</b> (dor óssea, febre, perda de peso). "
       "<br><b>Osteossarcoma</b> 10–19 anos (metáfise do joelho); <b>Ewing</b> 10–15. <b>Testículo</b>: massa indolor, 75% maligna. "
       "<br><b>Retinoblastoma</b>: <b>leucocoria</b> em &gt; <b>50%</b>, média 2 anos → reflexo vermelho alterado = <b>oftalmologista imediatamente</b>.",
  "fala": "Entre os tumores sólidos, os do sistema nervoso central são os mais comuns, e noventa e cinco por cento das crianças com cefaleia por tumor já têm algum achado neurológico. No abdome, Wilms é a criança de três a quatro anos em bom estado, com uma massa que a mãe percebeu no banho; o neuroblastoma é a criança de dois anos doente, com dor e febre. E o olho que brilha branco na foto com flash é retinoblastoma até prova em contrário: encaminha ao oftalmologista no mesmo dia.",
  "pega": "Leucocoria: <b>não repetir o teste</b> em um mês — <b>encaminhar imediatamente</b>. Massa + bom estado = <b>Wilms</b>; massa + criança doente = <b>neuroblastoma</b>.",
  "z": "Olho branco na foto do flash não é defeito do celular: é retinoblastoma até alguém olhar o fundo de olho, hoje, porra.",
  "m": [["Aula 01 · Triagem 35:33–35:59", "Teste do reflexo vermelho alterado ou leucocoria → não repetir, encaminhar imediatamente."]],
  "ills": ["a_solidos"]},
]

ILLS = {
 "a_base": cards("O gânglio da criança", [
     ("🛡️", "Tecido linfoide", "cresce até a puberdade e supera o do adulto", "t"),
     ("🔁", "Hiperplasia reacional", "maior causa de adenomegalia", "g"),
     ("🫁", "Sombra tímica", "normal no RX até 3 anos", "p"),
     ("🗺️", "Generalizada", "mais de duas cadeias não contíguas", "a")]),
 "a_aval": cards("Critérios de suspeição (slide 12)", [
     ("⏳", "~4 semanas", "sem regressão → biópsia (benigno se < 2 sem)", "r"),
     ("📍", "Supraclavicular", "também cervical inferior e epitroclear", "r"),
     ("📏", "> 2–3 cm", "e aumento progressivo", "r"),
     ("🪨", "Duro e fixo", "aderido, indolor, em pacote", "r"),
     ("🌡️", "Sistêmicos", "febre, perda de peso, sudorese", "a"),
     ("📊", "Causas", "75% infecciosas · 20% outras · 5% neoplasias", "t")]),
 "a_etio": table("Tempo × lado: o agente provável", [
     ("Aguda bilateral", "viroses respiratórias"),
     ("Aguda unilateral", "S. aureus / estreptococo do grupo A (adenite)"),
     ("Crônica unilateral", "micobactéria atípica · arranhadura do gato (Bartonella)"),
     ("Crônica bilateral", "EBV · CMV · toxoplasmose"),
     ("Tempo", "aguda < 2 sem · subaguda 2–6 · crônica > 6 sem")], cor="t"),
 "a_infl": versus("Palpação: inflamatório × neoplásico", ("🔥", "Inflamatório", "a", [
     "✔ doloroso", "✔ pele quente, hiperemiada", "✔ flutuação, fístula", "• antibiótico / drenagem"]),
     ("🪨", "Neoplásico", "r", [
     "✔ duro, aderido", "✔ indolor, em pacote", "✔ supraclavicular", "✔ ≥ 2,5 cm, progressivo", "• biópsia"]),
     foot="Supraclavicular DIREITA → tórax · ESQUERDA → abdome", fcor="p"),
 "a_adenite": flow("Adenite aguda localizada: o fluxo", [
     ("🔍", "Localizada, sem gravidade", "inflamatória, submandibular/cervical alta, porta de entrada", "t"),
     ("🧪", "Exames", "hemograma, VHS, PCR", "p"),
     ("💊", "Antibiótico VO 10 dias", "cefalexina 25–50 mg/kg/dia 6/6 h · cefuroxima 20–30 12/12 h · azitro 10 → 5 · clinda 10–20 se MRSA", "g"),
     ("⏱️", "Reavaliar 24–48 h", "flutuação → punção aspirativa / drenagem", "a"),
     ("🔬", "Sem resposta", "ou > 4 semanas → biópsia", "r")]),
 "a_grav": flow("Com gravidade ou generalizada doente", [
     ("🧪", "Hemograma, VHS/PCR, RX de tórax", "primeiro passo", "t"),
     ("🩸", "Blastos / pancitopenia", "→ mielograma (leucemia)", "r"),
     ("🫁", "Mediastino alargado", "→ PPD/TC → TB, linfoma, sarcoidose → biópsia", "a"),
     ("🔬", "Tudo normal", "→ biópsia do gânglio mais significativo", "v")],
     foot="Generalizada em bom estado: sorologias EBV, CMV, toxo + RX", fcor="g"),
 "a_bcg": versus("Gânglio pós-BCG (axila direita)", ("🎓", "Aula (slide 32)", "v", [
     "✔ notificar", "✔ isoniazida", "• com ou sem sinais flogísticos"]),
     ("📺", "MEDCURSO / protocolo", "t", [
     "• < 3 cm: esperado (~10%)", "• > 3 cm não supurado: acompanhar", "• supurado: isoniazida", "✘ não puncionar"]),
     foot="Prova da faculdade: notificar + isoniazida", fcor="v"),
 "a_cisto": cards("Massas cervicais não ganglionares", [
     ("⬆️", "Tireoglosso", "mediano, sobe com deglutição e língua", "t"),
     ("↔️", "Branquial", "lateral, borda do esternocleidomastóideo", "p"),
     ("🫧", "Higroma cístico", "volumoso, mole, precoce, cresce com infecção", "a"),
     ("🟥", "Hemangioma", "vascular, avermelhado", "r")]),
 "a_cancer": cards("Câncer infantil: os 10 sinais da campanha", [
     ("🦴", "Dor óssea / abdominal", "persistente, noturna", "r"),
     ("🌡️", "Febre > 1 semana", "sem foco", "r"),
     ("🟣", "Manchas roxas", "sangramentos, petéquias", "r"),
     ("🔘", "Caroço", "gânglio ou massa", "a"),
     ("😮‍💨", "Palidez, cansaço", "prurido sem lesão, perda de peso", "a"),
     ("🧠", "Cefaleia matinal + vômito", "abdome que cresce · infecção que não melhora", "a")],
     foot="70–80% de cura se precoce: não alarmar, mas investigar cedo", fcor="g"),
 "a_leuc": table("Leucemias e linfomas", [
     ("LLA", "80% · pico 2–4 anos · dor óssea pode ser o início · mielograma"),
     ("LMA", "15–20% · < 1 ano e adolescente"),
     ("Hodgkin", "15–40 anos · gânglio cervical indolor > 2 semanas"),
     ("Burkitt", "< 10 anos · abdome ou mandíbula · cresce rápido"),
     ("Linfoblástico", "> 10 anos · mediastino 50–70% · compressão de via aérea")], cor="r"),
 "a_solidos": table("Tumores sólidos: idade e pista", [
     ("SNC", "sólido mais comum · 95% com achado neurológico"),
     ("Wilms", "3–4 anos · massa assintomática 60% · HAS 25% · hematúria 15%"),
     ("Neuroblastoma", "pico 2 anos · criança doente (dor óssea, febre)"),
     ("Osteossarcoma / Ewing", "10–19 (joelho) / 10–15 anos"),
     ("Testículo", "massa indolor · 75% maligna"),
     ("Retinoblastoma", "leucocoria > 50% · média 2 anos → oftalmo já")], cor="v"),
}

QMAP = {0: ["a_adenite"], 1: ["a_grav", "a_leuc"], 2: ["a_infl"], 3: ["a_bcg"], 4: ["a_solidos"], 5: ["a_solidos"], 6: ["a_solidos"], 7: ["a_leuc"]}

DIV = {
 "aden_corte": ["Ponto de corte do tamanho", "Slide 12: “maior que <b>2–3 cm</b>”", "Slide 24: <b>≥ 2,5 cm</b> · slide 43: linfadenopatia &gt; 2 cm",
                "Divergência interna: escreva “<b>&gt; 2–3 cm</b> (slide 12)”; no Kawasaki o corte é &gt; 1,5 cm"],
 "azitro": ["Duração do antibiótico na adenite", "Slide 26: “tratar com antibiótico (<b>10 dias</b>)”", "Slide 29: azitromicina 10 mg/kg + 5 mg/kg/dia por mais 4 dias (<b>5 dias</b>)",
            "10 dias vale para cefalexina/cefuroxima/clindamicina; azitromicina tem esquema próprio de 5 dias"],
 "bcg": ["Linfonodo pós-BCG", "Slide 32: <b>notificar + isoniazida</b>, com ou sem sinais flogísticos",
         "MEDCURSO (S27 07:14–09:58): isoniazida só se <b>supurado</b>; &lt; 3 cm é esperado; &gt; 3 cm não supurado só acompanha",
         "Faculdade = <b>slide</b>; residência = protocolo. Em qualquer caso: <b>não puncionar</b>"],
 "cura": ["Taxa de cura do câncer infantil", "Slide 37: <b>70–80%</b>", "Slides 56/58–62: “80%” e “maiores que 80%”", "Na prova: <b>70–80%</b> (texto da professora)"],
}

FLASH = [
 [4, "Sombra tímica normal até?", "3 anos."],
 [4, "Adenomegalia generalizada (slide)?", "Mais de duas cadeias não contíguas."],
 [4, "5 critérios de suspeição do slide 12?", "~4 semanas, supraclavicular, > 2–3 cm, progressivo, duro e fixo."],
 [4, "Causas de adenomegalia (%)?", "75% infecciosas, 20% outras, 5% neoplasias."],
 [4, "Aguda unilateral inflamada: agente?", "S. aureus e estreptococo do grupo A."],
 [4, "Crônica unilateral sem flogose?", "Micobactéria atípica, arranhadura do gato."],
 [4, "Supraclavicular direita × esquerda?", "Direita = tórax; esquerda = abdome."],
 [4, "Adenite: cefalexina?", "25–50 mg/kg/dia 6/6 h por 10 dias."],
 [4, "Adenite: clindamicina quando?", "MRSA ou anaeróbio, 10–20 mg/kg/dia."],
 [4, "Adenite com flutuação?", "Punção aspirativa / drenagem."],
 [4, "Generalizada doente com blastos?", "Mielograma."],
 [4, "Tudo normal na adenomegalia suspeita?", "Biópsia do gânglio mais significativo."],
 [4, "Pós-BCG pela aula?", "Notificar + isoniazida (não puncionar)."],
 [4, "LLA: % e pico?", "80% das leucemias; 2–4 anos."],
 [4, "Mediastino alargado em > 10 anos?", "Linfoma linfoblástico — risco de compressão de via aérea."],
 [4, "Tumor sólido maligno mais comum?", "SNC (95% com achado neurológico)."],
 [4, "Wilms × neuroblastoma?", "Wilms 3–4 a, bom estado, massa assintomática; neuroblastoma 2 a, criança doente."],
 [4, "Leucocoria?", "Retinoblastoma (> 50%) → oftalmologista imediatamente."],
 [4, "Cura do câncer infantil precoce?", "70–80%."],
]

COLA = [["Cap. 4 · Adenomegalias e câncer", [
 ["Suspeição", "~4 sem · supraclavicular · > 2–3 cm · duro/fixo · progressivo"], ["Causas", "75% infec · 5% neo"],
 ["Supraclavicular", "D → tórax · E → abdome"], ["Cefalexina", "25–50 mg/kg/dia 6/6 h · 10 d"], ["Cefuroxima", "20–30 mg/kg/dia 12/12 h"],
 ["Azitromicina", "10 → 5 mg/kg/dia (5 d)"], ["Clindamicina", "10–20 mg/kg/dia (MRSA)"], ["Reavaliar", "24–48 h · flutua → drena"],
 ["Gravidade", "hemograma + VHS/PCR + RX → blastos: mielograma · normal: biópsia"], ["Pós-BCG (aula)", "notificar + isoniazida"],
 ["LLA", "80% · 2–4 a"], ["SNC", "95% com achado neuro"], ["Wilms", "3–4 a · massa 60% · HAS 25%"], ["Leucocoria", "> 50% retinoblastoma"], ["Cura", "70–80%"]]]]

KS = [
 {"id": "k_a_aden", "cap": 4, "blk": ["a_adenite", "a_infl", "a_grav"], "t": "O caroço no pescoço (caiu 3×, até 2,6 pts)",
  "src": "Prova A1 (7 pts) · Q3 / Q1 — caiu em 3 versões — Profa. Patrícia",
  "enun": "Criança de 5 anos, febre há 3 dias e “caroço no pescoço”. Um único gânglio <b>submandibular direito</b>, ~2 cm, <b>doloroso</b>, com <b>sinais flogísticos</b> e <b>região central flutuante</b>. Bom estado geral.",
  "p": [{"p": "Qual a primeira abordagem diagnóstica e a principal hipótese?",
         "m": "Localizada, sem sinais de gravidade, inflamatória, cervical superior → <b>adenite piogênica</b> (<i>S. aureus</i> / estreptococo do grupo A). Pedir <b>hemograma, VHS e PCR</b>.",
         "c": ["adenite", "S. aureus", "estreptococo", "hemograma", "PCR"]},
        {"p": "Qual o tratamento? Se não melhorar, qual a próxima abordagem?",
         "m": "Antibiótico oral <b>10 dias</b> cobrindo <i>S. aureus</i> e estrepto: <b>cefalexina 25–50 mg/kg/dia 6/6 h</b> (alternativas: cefuroxima 20–30 mg/kg/dia 12/12 h; azitromicina 10 → 5 mg/kg; clindamicina 10–20 mg/kg/dia se MRSA/anaeróbio). Reavaliar em <b>24–48 h</b>; flutuação → <b>punção/drenagem</b>. Sem resposta → <b>biópsia</b>.",
         "c": ["cefalexina", "25 a 50 mg/kg/dia", "10 dias", "24 a 48 h", "drenagem", "biópsia"]},
        {"p": "Meses depois surge adenomegalia supraclavicular direita. O que pensar e o que pedir?",
         "m": "Supraclavicular <b>direita → tumor intratorácico</b> ou processo inflamatório (esquerda → abdome). Pedir <b>hemograma, VHS/PCR e RX de tórax</b>: blastos → leucemia → <b>mielograma</b>; mediastino alargado → TB, linfoma, sarcoidose → <b>biópsia</b>; exames normais → <b>biópsia</b> mesmo assim.",
         "c": ["intratorácico", "RX de tórax", "hemograma", "mielograma", "mediastino", "biópsia"]}]},
 {"id": "k_a_leuc", "cap": 4, "blk": ["a_leuc", "a_grav", "c_membal"], "t": "Luísa: dor nas pernas que não é de crescimento",
  "src": "Prova A1 (3 pts) · Q2 média taxonomia — Profa. Patrícia",
  "enun": "Luísa, 6 anos, dor em MMII bilateral e recorrente há ~5 meses, antes semanal e agora <b>diária</b>. Anorexia, <b>perda de peso</b> (1.800 g em 2 meses), cansaço. Exame: <b>adenomegalia</b> cervical, submandibular e inguinal bilateral; <b>fígado a 3–4 cm</b> do RCD e <b>ponta de baço</b>; <b>palidez acentuada</b>. Exame dos membros normal.",
  "p": [{"p": "Primeira abordagem: quais exames? (0,2)",
         "m": "<b>Hemograma completo</b> (+ VHS/PCR, DHL/ácido úrico, RX de tórax).",
         "c": ["hemograma", "VHS", "RX de tórax"]},
        {"p": "Hipótese mais provável e justificativa. (0,2)",
         "m": "<b>Leucemia (LLA)</b>: dor óssea com sinais sistêmicos (palidez, perda de peso, astenia), adenomegalia generalizada e hepatoesplenomegalia. Dor de crescimento não tem nada disso.",
         "c": ["leucemia", "LLA", "palidez", "perda de peso", "hepatoesplenomegalia", "adenomegalia generalizada"]},
        {"p": "O que espera nos exames iniciais e qual exame confirma? (0,2)",
         "m": "<b>Blastos</b> no sangue periférico ou <b>pancitopenia</b> (anemia, plaquetopenia) → <b>mielograma</b> confirma.",
         "c": ["blastos", "pancitopenia", "mielograma"]}]},
 {"id": "k_a_osso", "cap": 4, "blk": ["c_membal", "a_solidos"], "t": "Dor do tumor ósseo × dor da leucemia (2025/2)",
  "src": "Prova 2025/2 · Q5 — gabarito mínimo oficial",
  "enun": "Adolescente de 13 anos com dor no joelho direito há 6 semanas, progressiva, que o acorda à noite e não melhora com analgésico. Sem febre, sem perda de peso, hemograma normal.",
  "p": [{"p": "Como diferenciar a dor do tumor ósseo da dor da leucemia?",
         "m": "Gabarito oficial: <b>tumor ósseo = dor localizada</b>, sem sinais sistêmicos; <b>leucemia = dor não localizada</b> + sintomas sistêmicos (prostração, palidez, perda de peso, visceromegalias).",
         "c": ["localizada", "não localizada", "sintomas sistêmicos", "palidez", "perda de peso"]},
        {"p": "Qual a hipótese e a investigação deste caso?",
         "m": "<b>Tumor ósseo primário</b> (osteossarcoma — 10–19 anos, metáfise do joelho; Ewing 10–15): <b>RX do joelho</b> e, com lesão, encaminhamento à oncologia para <b>biópsia</b>.",
         "c": ["osteossarcoma", "joelho", "RX", "biópsia"]}]},
]
