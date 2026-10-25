CAP = {"n": 2, "t": "Doenças exantemáticas", "short": "Exantemáticas", "aula": "Aula 2 · slides da Patrícia",
       "icon": "🦠", "col": "#7A2E4A",
       "bul": ["Escarlatina × mono: caiu 2× (Filatov, Pastia, framboesa × linfócitos atípicos)",
               "Sarampo: 3 C + Koplik + retroauricular → craniocaudal",
               "Profilaxia: bloqueio sarampo 72 h · Ig 6 dias · VZIG 96 h",
               "Kawasaki: febre ≥ 5 d + 4/5 · IGIV 2 g/kg + AAS até o 10º dia"],
       "medalha": ["🦠", "Caçador de Koplik"]}

BLOCKS = [
 {"id": "e_conc", "t": "Exantema: o que é e como classificar",
  "s": "Exantema = erupção cutânea de doença sistêmica (geralmente infecciosa). Tipos: <b>maculopapular</b> (morbiliforme, rubeoliforme, escarlatiniforme), <b>vesicular</b> (varicela, mão-pé-boca), <b>petequial/purpúrico</b> (meningococcemia — emergência). "
       "<br>Digitopressão separa eritema de púrpura. Transmissão por <b>aerossol</b>: só <b>sarampo e varicela</b> (isolamento respiratório para aerossóis).",
  "fala": "Exantema é a pele contando que existe uma doença sistêmica por trás. Classifique primeiro: maculopapular, como sarampo, rubéola e escarlatina; vesicular, como varicela e mão-pé-boca; e petequial ou purpúrico, que em criança febril é meningococcemia até prova em contrário. Guarde também que só sarampo e varicela se transmitem por aerossol.",
  "pega": "Aerossol = <b>sarampo e varicela</b> (máscara N95, quarto privativo). Exantema <b>petequial</b> + febre = <b>meningococcemia</b>.",
  "z": "Exantema que não some no aperto em criança com febre não é virose de creche, é meningococo querendo matar alguém. Antibiótico já, porra.",
  "ills": ["e_conc"]},
 {"id": "e_saramp", "t": "Sarampo: pródromo, Koplik e exantema craniocaudal",
  "s": "Paramixovírus. <b>Pródromo catarral</b> (os <b>3 C</b>: tosse, coriza, conjuntivite) com <b>febre que sobe</b>; <b>manchas de Koplik</b> (patognomônicas, mucosa jugal). "
       "<br>Exantema <b>morbiliforme</b> que começa <b>retroauricular / linha do cabelo</b> e desce (craniocaudal), no <b>auge</b> dos sintomas. "
       "<br>Complicações: <b>otite média</b> = bacteriana mais comum; <b>pneumonia</b> = principal causa de morte; encefalite, PEES (tardia). "
       "<br>Conduta: <b>vitamina A</b>, isolamento de aerossóis, <b>notificação compulsória</b>.",
  "fala": "Sarampo começa com tosse, coriza e conjuntivite e uma febre que vai subindo. Aí aparecem as manchas de Koplik na bochecha por dentro, que são patognomônicas, e o exantema nasce atrás da orelha, na linha do cabelo, e desce pelo corpo, justamente no pior momento da doença. A otite é a complicação bacteriana mais comum, a pneumonia é o que mais mata, e todo caso leva vitamina A e notificação.",
  "div": "saramp_iso",
  "pega": "No sarampo o exantema aparece no <b>auge</b> (febre alta), não quando melhora — quem aparece quando a febre <b>cai</b> é o exantema súbito.",
  "z": "Três C e uma mancha branca na bochecha: é sarampo, e não é frescura de antivacina, é pneumonia matando criança. Vitamina A e notificação, caralho.",
  "m": [["MEDCURSO · S41 B01 17:53", "Notificação compulsória e imediata (o próprio cursinho se contradiz mais adiante; a apostila diz só “compulsória”)."]],
  "ills": ["e_saramp"]},
 {"id": "e_sarprof", "t": "Sarampo: profilaxia pós-exposição",
  "s": "<b>Vacina de bloqueio</b>: a partir de <b>6 meses</b>, até <b>72 h</b> do contato. Entre 6 e 11 meses é <b>dose zero</b> (não vale para a rotina). "
       "<br><b>Imunoglobulina</b>: até <b>6 dias</b> do contato — slide 28: <b>&lt; 1 ano</b>; MEDCURSO: <b>&lt; 6 meses</b>; também gestante suscetível e imunodeprimido.",
  "fala": "Depois do contato com sarampo há duas armas e dois relógios. A vacina de bloqueio pode ser dada a partir dos seis meses de idade, até setenta e duas horas do contato; entre seis e onze meses ela é uma dose extra, que não conta para o calendário. A imunoglobulina vai até seis dias do contato, para quem não pode receber a vacina: gestante, imunodeprimido e o lactente pequeno.",
  "div": "saramp_ig",
  "pega": "Prazos: <b>vacina 72 h</b> · <b>imunoglobulina 6 dias</b>. Dose entre 6–11 meses <b>não vale</b> para a rotina.",
  "z": "Setenta e duas horas pra vacina, seis dias pra imunoglobulina. Errou o relógio, a creche inteira vira surto, porra.",
  "m": [["MEDCURSO · S41 B01 28:58–32:16", "Bloqueio a partir de 6 meses até 72 h; imunoglobulina para &lt; 6 meses até 6 dias."],
        ["MEDCURSO · S41 B01 33:35–34:53", "Dose entre 6 e 11 meses não é válida para a rotina."]],
  "ills": ["e_sarprof"]},
 {"id": "e_rub", "t": "Rubéola: o sarampinho com gânglio atrás da orelha",
  "s": "Exantema róseo, craniocaudal, mais leve que o do sarampo; <b>adenomegalia retroauricular, occipital</b> e cervical posterior; artralgia no adolescente. Benigna na criança. "
       "<br><b>Rubéola congênita</b>: <b>catarata, surdez e cardiopatia (PCA)</b>. "
       "<br>Vacina (vírus vivo) <b>contraindicada na gestação</b>; evitar engravidar por <b>30 dias</b> após.",
  "fala": "Rubéola é um sarampo mais brando, com exantema róseo que também desce da cabeça para o corpo, mas com uma pista própria: gânglios atrás da orelha e na nuca. Na criança é benigna; o drama é a rubéola congênita, com a tríade catarata, surdez e cardiopatia, sobretudo persistência do canal arterial. Por isso a vacina, que é de vírus vivo, não se dá na gestante, e a mulher espera trinta dias para engravidar.",
  "pega": "Rubéola = adenomegalia <b>retroauricular e occipital</b>. Congênita: <b>catarata + surdez + PCA</b>.",
  "z": "Gânglio atrás da orelha e na nuca com exantema leve: rubéola. Benigna pra criança, desgraça pro feto. Gestante longe, caralho.",
  "m": [["MEDCURSO · S41 B01", "Acrescenta a adenomegalia <b>occipital</b> (definição do Ministério da Saúde); o slide 32 cita só a retroauricular."]],
  "ills": ["e_rub"]},
 {"id": "e_escarl", "t": "Escarlatina: lixa, Filatov, Pastia e framboesa",
  "s": "<b>Estreptococo beta-hemolítico do grupo A</b> (toxina eritrogênica), 5–12 anos. Febre + <b>faringoamigdalite</b> + exantema <b>micropapular áspero (em lixa)</b> que começa no tronco. "
       "<br>Sinais: <b>Filatov</b> (palidez perioral), <b>Pastia</b> (linhas petequiais nas dobras/antebraços), <b>língua em framboesa</b>; descamação lamelar de mãos e pés depois. "
       "<br>Tratamento: <b>penicilina benzatina IM dose única</b> — <b>600.000 UI se &lt; 25 kg</b> · <b>1.200.000 UI se &gt; 25 kg</b> — ou <b>amoxicilina VO 10 dias</b> (penicilina V, macrolídeo; azitromicina 5 dias). "
       "<br>Afastar da escola até <b>24–48 h</b> de antibiótico eficaz. Complicações: supurativas (abscesso periamigdaliano, otite) e não supurativas (<b>febre reumática, GNPE</b>).",
  "fala": "Escarlatina é a faringite do estreptococo do grupo A com um exantema áspero, que parece lixa ao passar a mão, começando no tronco. Os sinais de prova são três: palidez em volta da boca, que é o sinal de Filatov; linhas petequiais nas dobras, que é o sinal de Pastia; e a língua em framboesa. Trata com penicilina benzatina em dose única, seiscentas mil unidades abaixo de vinte e cinco quilos e um milhão e duzentas acima, ou amoxicilina por dez dias.",
  "div": "escarl_gab",
  "pega": "Corte de peso da benzatina: <b>25 kg</b>. Exantema após amoxicilina com Filatov/Pastia/framboesa continua sendo <b>escarlatina</b>, não alergia nem mono.",
  "z": "Pele de lixa, boca pálida e língua de framboesa: é o estreptococo fazendo cosplay de sobremesa. Benzatina, e vinte e cinco quilos é o corte, porra.",
  "ills": ["e_escarl"]},
 {"id": "e_var", "t": "Varicela: polimorfismo e o que não dar",
  "s": "Vírus varicela-zóster. Vesículas <b>pruriginosas</b>, de distribuição <b>centrípeta</b>, com <b>polimorfismo regional</b> (mácula, pápula, vesícula e crosta ao mesmo tempo), couro cabeludo e mucosas. "
       "<br>Contágio de 1–2 dias antes até <b>todas as lesões em crosta</b>. "
       "<br><b>Sem salicilato</b> (síndrome de Reye). Complicação mais comum: infecção bacteriana da pele.",
  "fala": "Varicela é vesícula que coça, concentrada no tronco, e com lesões em todas as fases ao mesmo tempo: mácula, pápula, vesícula e crosta lado a lado. Esse polimorfismo é a assinatura dela. A criança transmite de um a dois dias antes até todas as lesões virarem crosta, e é proibido dar ácido acetilsalicílico, pelo risco de síndrome de Reye. A complicação mais comum é a infecção bacteriana das lesões.",
  "pega": "Fim do contágio = <b>todas as lesões em crosta</b>. Antitérmico: <b>nunca AAS</b> (Reye).",
  "z": "Na varicela a pele vira um álbum de fases: mácula, pápula, vesícula e crosta juntas. E se alguém der aspirina, ganha um Reye de brinde, caralho.",
  "ills": ["e_var"]},
 {"id": "e_varprof", "t": "Varicela: bloqueio vacinal e quem recebe VZIG",
  "s": "<b>Vacina de bloqueio</b>: a partir de <b>9 meses</b>, até <b>72–96 h</b> do contato (slide 66; MEDCURSO: até 5 dias). "
       "<br><b>VZIG até 96 h</b> para: <b>gestante</b> suscetível · <b>imunodeprimido</b> · <b>RN de mãe com varicela de 5 dias antes a 2 dias depois do parto</b> · <b>prematuro ≥ 28 sem</b> se a mãe <b>não</b> teve varicela · <b>prematuro &lt; 28 sem ou &lt; 1.000 g</b>, sempre.",
  "fala": "Na exposição à varicela, quem tem nove meses ou mais pode receber vacina de bloqueio, em até setenta e duas a noventa e seis horas. A imunoglobulina vai até noventa e seis horas para gestante suscetível, imunodeprimido, recém-nascido de mãe que teve varicela entre cinco dias antes e dois dias depois do parto, e prematuros: os muito pequenos sempre, e os de vinte e oito semanas ou mais só se a mãe nunca teve varicela.",
  "div": "var_bloq",
  "pega": "Prematuro <b>≥ 28 sem</b> com mãe que <b>já teve</b> varicela recebeu anticorpo pela placenta → <b>observar</b>. &lt; 28 sem ou &lt; 1.000 g → VZIG <b>sempre</b>.",
  "z": "Mãe pegou varicela dois dias antes do parto? Esse bebê nasceu sem anticorpo e com vírus: imunoglobulina, sem discussão, porra.",
  "m": [["MEDCURSO · S41 B03 29:59–31:19", "Prematuro ≥ 28 semanas de mãe imune recebeu anticorpos transplacentários — por isso só recebe VZIG se a mãe não tem história."]],
  "ills": ["e_varprof"]},
 {"id": "e_b19", "t": "Eritema infeccioso (parvovírus B19)",
  "s": "<b>Face esbofeteada</b> → depois exantema <b>rendilhado</b> em membros, que vai e volta (calor, sol). "
       "<br>Quando o exantema aparece, a criança <b>já não transmite</b>. "
       "<br>B19 infecta o precursor eritroide: em <b>hemoglobinopatas (falciforme)</b> → <b>crise aplásica transitória</b> com <b>reticulocitopenia</b> (nessa fase é contagioso → isolar de outras falcêmicas; transfundir se grave). Gestante: hidropsia fetal.",
  "fala": "O eritema infeccioso é o do parvovírus B dezenove: bochechas vermelhas, como se a criança tivesse levado um tapa, e depois um exantema rendilhado nos membros que some e volta com calor. Quando a pele mostra o exantema, a criança já não transmite mais. O perigo está na anemia falciforme: o vírus para a medula vermelha e causa crise aplásica, com hemoglobina despencando e reticulócitos quase zerados.",
  "pega": "Crise aplásica = anemia com <b>reticulocitopenia</b> (sequestro e hemólise têm reticulocitose). Com exantema, <b>não</b> é mais contagioso.",
  "z": "Bochecha de quem levou um tapa e rendado nos braços: parvovírus. Na falcêmica ele desliga a fábrica de hemácia, e aí é transfusão, caralho.",
  "m": [["MEDCURSO · S41 B02 21:44–24:46", "B19 interrompe a eritropoiese: anemia com reticulocitopenia; na crise aplásica a criança é contagiosa."]],
  "div": "b19_inc",
  "ills": ["e_b19"]},
 {"id": "e_subito", "t": "Exantema súbito (roséola, HHV-6)",
  "s": "Lactente de <b>6 meses a 2 anos</b>: <b>febre alta por 3–4 dias</b> com bom estado geral → a febre <b>cai em crise</b> e surge exantema róseo maculopapular no <b>tronco</b>, que vai ao pescoço e some em 1–2 dias. "
       "<br>Complicação: <b>convulsão febril</b>. Tratamento sintomático. Se houver antibiótico mal indicado, <b>suspender</b> (não é alergia).",
  "fala": "Exantema súbito é o lactente com febre alta por três ou quatro dias, mas brincando entre os picos. Quando a febre desaparece de repente, nasce um exantema róseo no tronco que sobe para o pescoço e some em um ou dois dias. É o herpes vírus seis. Se alguém começou amoxicilina no meio do caminho, a coincidência engana: não é alergia, suspende o antibiótico e observa.",
  "div": "subito_rot",
  "pega": "Exantema que surge <b>quando a febre some</b> = exantema súbito. No sarampo, surge no <b>pico</b> da febre.",
  "z": "Três dias de febre, aí a febre vai embora e a mancha chega: roséola. Não é alergia à amoxicilina, é o antibiótico que não precisava, porra.",
  "m": [["MEDCURSO · S41 B02 25:59–28:39", "Se a indicação do antibiótico estava errada, suspende-se — a coincidência temporal é da doença."]],
  "ills": ["e_subito"]},
 {"id": "e_mono", "t": "Mononucleose infecciosa (EBV)",
  "s": "Adolescente: <b>tríade febre + faringite + linfadenopatia</b> (generalizada, cervical posterior), <b>esplenomegalia</b>, hepatomegalia, <b>edema palpebral</b> (Hoagland), fadiga arrastada. "
       "<br>Hemograma: <b>linfocitose com linfócitos atípicos</b>. Exantema típico <b>após amoxicilina/ampicilina</b>. "
       "<br>Conduta: sintomáticos; <b>evitar esporte de contato</b> (ruptura esplênica).",
  "fala": "Mononucleose é o adolescente com febre, dor de garganta e gânglios em vários lugares, muitas vezes com baço grande e pálpebras inchadas. O hemograma mostra linfocitose com linfócitos atípicos. A pegadinha clássica é o exantema que aparece depois de tomar amoxicilina por conta própria. O tratamento é de suporte, e ele fica longe de esporte de contato, para não romper o baço.",
  "div": "mono_inc",
  "pega": "Mono: adenomegalia <b>generalizada</b> + esplenomegalia + linfócitos <b>atípicos</b>; não tem Filatov, Pastia nem framboesa.",
  "z": "Adolescente tomou amoxicilina por conta e ficou todo vermelho? Não é alergia, é o Epstein-Barr rindo da automedicação. E nada de futebol com baço gigante, caralho.",
  "m": [["MEDCURSO · S41 B04", "Incubação de 30 a 50 dias; exantema em ~10%, a maioria após amoxicilina."]],
  "ills": ["e_mono"]},
 {"id": "e_mpb", "t": "Doença mão-pé-boca (Coxsackie A16)",
  "s": "Coxsackie <b>A16</b> (enterovírus): febre baixa, <b>úlceras dolorosas em toda a boca</b>, <b>vesículas em mãos, pés</b> (e glúteos). Benigna, autolimitada; cuidado com a recusa alimentar e a hidratação.",
  "fala": "Mão-pé-boca é o enterovírus Coxsackie A dezesseis. A criança tem febre baixa, aftas dolorosas espalhadas pela boca e vesículas nas palmas, nas plantas e às vezes nos glúteos. É benigna e passa sozinha; o cuidado é com a dor ao engolir, que leva a recusa alimentar e desidratação.",
  "pega": "Úlceras <b>em toda a boca</b> + vesículas em <b>palmas e plantas</b> = mão-pé-boca (herpangina fica no palato posterior).",
  "z": "Bolha na mão, no pé e afta na boca toda: Coxsackie. O risco não é a bolha, é a criança parar de beber água de tanta dor, porra.",
  "ills": ["e_mpb"]},
 {"id": "e_kawa", "t": "Doença de Kawasaki: critérios e tratamento até o 10º dia",
  "s": "Vasculite de médios vasos, <b>&lt; 5 anos</b>. <b>Febre ≥ 5 dias</b> + <b>4 de 5</b>: <b>conjuntivite</b> bilateral não exsudativa · <b>lábios/boca</b> (eritema, fissuras, framboesa) · <b>extremidades</b> (edema, eritema, depois descamação) · <b>exantema polimorfo</b> · <b>adenomegalia cervical</b> &gt; 1,5 cm. "
       "<br>Tratamento: <b>imunoglobulina EV 2 g/kg em 10 h</b>, idealmente <b>até o 10º dia</b> + <b>AAS 80–100 mg/kg/dia</b> até afebril → <b>3–5 mg/kg/dia por 6–8 semanas</b>. "
       "<br>Aneurisma coronariano: sem tratamento <b>20–30%</b>; tratado <b>4–5%</b>.",
  "fala": "Kawasaki é uma vasculite da criança pequena: febre por cinco dias ou mais, com quatro de cinco critérios, que são conjuntivite sem secreção, lábios e boca vermelhos e fissurados, mãos e pés inchados que depois descamam, exantema polimorfo e um gânglio cervical grande. O tratamento é imunoglobulina venosa, dois gramas por quilo, de preferência até o décimo dia, junto com ácido acetilsalicílico, e é isso que derruba o risco de aneurisma coronariano.",
  "div": "kawa_aneu",
  "pega": "Kawasaki <b>não tem exsudato</b> amigdaliano e exige <b>febre ≥ 5 dias</b>. Prognóstico: <b>bom se tratado</b> até o 10º dia — não escreva “ruim”.",
  "z": "Cinco dias de febre, olho vermelho sem remela, boca de morango e mão inchada: é Kawasaki, e o coração da criança depende da sua imunoglobulina até o décimo dia, porra.",
  "m": [["MEDCURSO · S41 B04 24:38–25:51", "Kawasaki × escarlatina: Kawasaki exige febre ≥ 5 dias e conjuntivite, sem exsudato; adenomegalia &gt; 1,5 cm."]],
  "ills": ["e_kawa"]},
]

ILLS = {
 "e_conc": cards("Exantema: classifique antes de diagnosticar", [
     ("🔴", "Maculopapular", "sarampo, rubéola, escarlatina, exantema súbito, eritema infeccioso", "v"),
     ("💧", "Vesicular", "varicela, mão-pé-boca, herpes", "p"),
     ("🩸", "Petequial / purpúrico", "meningococcemia: emergência — não some à digitopressão", "r"),
     ("😷", "Aerossol", "só sarampo e varicela → N95 e quarto privativo", "t")]),
 "e_saramp": flow("Sarampo: a linha do tempo", [
     ("🤧", "Pródromo catarral (3 C)", "tosse, coriza, conjuntivite + febre que sobe", "t"),
     ("⚪", "Manchas de Koplik", "pontos brancos na mucosa jugal — patognomônicas", "p"),
     ("🔴", "Exantema morbiliforme", "retroauricular / linha do cabelo → desce (craniocaudal), no auge da febre", "v"),
     ("⚠️", "Complicações", "otite = bacteriana mais comum · pneumonia = principal causa de morte", "r"),
     ("🥕", "Conduta", "vitamina A · isolamento de aerossóis · notificação compulsória", "g")]),
 "e_sarprof": versus("Sarampo: profilaxia pós-exposição", ("💉", "Vacina de bloqueio", "g", [
     "✔ a partir de 6 meses", "✔ até 72 h do contato", "• 6–11 meses = dose zero, não vale para rotina"]),
     ("🧪", "Imunoglobulina", "p", [
     "✔ até 6 dias do contato", "• slide: < 1 ano", "• MEDCURSO: < 6 meses", "• gestante e imunodeprimido"]),
     foot="Prova da faculdade: Ig para < 1 ano (slide 28)", fcor="a"),
 "e_rub": cards("Rubéola: pistas e riscos", [
     ("🌸", "Exantema róseo", "craniocaudal, mais leve que o sarampo", "v"),
     ("🔘", "Gânglios", "retroauricular, occipital, cervical posterior", "p"),
     ("🤰", "Congênita", "catarata + surdez + cardiopatia (PCA)", "r"),
     ("💉", "Vacina viva", "contraindicada na gestação · evitar gravidez 30 dias", "a")]),
 "e_escarl": cards("Escarlatina: sinais e tratamento", [
     ("🧽", "Exantema em lixa", "micropapular áspero, começa no tronco", "v"),
     ("😶", "Filatov", "palidez perioral", "p"),
     ("📏", "Pastia", "linhas petequiais nas dobras e antebraços", "p"),
     ("🍓", "Língua em framboesa", "papilas hipertrofiadas", "r"),
     ("💉", "Benzatina IM única", "600.000 UI se < 25 kg · 1.200.000 UI se > 25 kg", "g"),
     ("💊", "Ou VO 10 dias", "amoxicilina (ou penicilina V, macrolídeo) · afastar 24–48 h", "g")],
     foot="Complicações: febre reumática e GNPE", fcor="a"),
 "e_var": cards("Varicela: a assinatura", [
     ("🔀", "Polimorfismo regional", "mácula, pápula, vesícula e crosta juntas", "p"),
     ("🎯", "Centrípeta", "tronco > membros, couro cabeludo e mucosas", "v"),
     ("🟤", "Fim do contágio", "todas as lesões em crosta", "g"),
     ("🚫", "Sem AAS", "risco de síndrome de Reye", "r")]),
 "e_varprof": table("Varicela: quem recebe o quê", [
     ("Vacina de bloqueio", "≥ 9 meses · até 72–96 h (MEDCURSO: até 5 dias)"),
     ("VZIG — prazo", "até 96 h do contato"),
     ("Gestante suscetível", "VZIG"), ("Imunodeprimido", "VZIG"),
     ("RN de mãe com varicela", "−5 dias a +2 dias do parto → VZIG"),
     ("Prematuro ≥ 28 sem", "só se a mãe nunca teve varicela"),
     ("Prematuro < 28 sem ou < 1.000 g", "VZIG sempre")], cor="p"),
 "e_b19": flow("Parvovírus B19: da bochecha à medula", [
     ("😳", "Face esbofeteada", "eritema das bochechas", "v"),
     ("🕸️", "Exantema rendilhado", "membros, vai e volta com calor — já não transmite", "a"),
     ("🩸", "Hemoglobinopata", "crise aplásica: Hb cai, reticulócitos baixos → transfundir e isolar", "r")],
     foot="Reticulocitopenia separa crise aplásica de sequestro/hemólise"),
 "e_subito": flow("Exantema súbito: a febre sai, a mancha entra", [
     ("🌡️", "Dias 1–3/4", "febre alta, bom estado entre os picos, lactente 6 m–2 a", "r"),
     ("📉", "Febre cai em crise", "defervescência súbita", "a"),
     ("🌸", "Exantema róseo", "tronco → pescoço, some em 1–2 dias", "v"),
     ("⚡", "Atenção", "convulsão febril · suspender antibiótico mal indicado", "p")]),
 "e_mono": versus("Mononucleose × escarlatina", ("🧑", "Mononucleose (EBV)", "p", [
     "✔ adenomegalia generalizada", "✔ esplenomegalia", "✔ edema palpebral", "✔ linfócitos atípicos", "✔ exantema após amoxicilina", "✘ Filatov / Pastia"]),
     ("🍓", "Escarlatina (SBHGA)", "v", [
     "✔ exantema em lixa", "✔ Filatov e Pastia", "✔ língua em framboesa", "✔ 5–12 anos", "✘ esplenomegalia"]),
     foot="Mono: evitar esporte de contato (ruptura esplênica)"),
 "e_mpb": cards("Mão-pé-boca (Coxsackie A16)", [
     ("👄", "Boca", "úlceras dolorosas espalhadas", "r"),
     ("✋", "Mãos", "vesículas nas palmas", "v"),
     ("🦶", "Pés e glúteos", "vesículas nas plantas", "v"),
     ("💧", "Cuidado", "recusa alimentar → hidratação", "g")]),
 "e_kawa": flow("Kawasaki: critérios e tratamento", [
     ("🌡️", "Febre ≥ 5 dias", "+ 4 de 5 critérios, criança < 5 anos", "r"),
     ("👁️", "Conjuntivite + boca", "conjuntivite bilateral sem exsudato · lábios fissurados, língua em morango", "v"),
     ("🖐️", "Extremidades + pele", "edema/eritema de mãos e pés → descamação · exantema polimorfo", "v"),
     ("🔘", "Gânglio cervical", "> 1,5 cm, geralmente unilateral", "p"),
     ("💉", "Tratamento até o 10º dia", "IGIV 2 g/kg em 10 h + AAS 80–100 mg/kg/dia → 3–5 mg/kg/dia por 6–8 semanas", "g")],
     foot="Aneurisma coronariano: 20–30% sem tratamento → 4–5% tratado", fcor="g"),
}

QMAP = {0: ["e_subito"], 1: ["e_sarprof"], 2: ["e_varprof"], 3: ["e_escarl", "e_kawa"], 4: ["e_b19"]}

Q = [
 {"id": "qa_saramp", "cap": 2, "src": "antiga", "orig": "Prova A1 (7 pts) · Q7 objetiva — caiu 2×", "tag": "prova antiga · 2×",
  "enun": "Sarah, 3 anos, há 3 dias com tosse, febre alta, coriza e conjuntivite. Hoje os sinais pioraram e surgiram manchas vermelhas <b>retroauriculares acompanhando a linha de implantação do cabelo</b>. Diagnóstico?",
  "alts": ["Rubéola", "Eritema infeccioso", "Sarampo", "Exantema súbito"], "ok": 2,
  "coment": "<b>C — Sarampo.</b> Pródromo dos 3 C com febre alta e exantema que começa atrás das orelhas/linha do cabelo e desce, no auge dos sintomas. <b>A</b>: rubéola é mais leve e tem adenomegalia retroauricular/occipital. <b>B</b>: face esbofeteada. <b>D</b>: exantema quando a febre cai.",
  "blk": ["e_saramp"]},
 {"id": "qa_mono", "cap": 2, "src": "antiga", "orig": "Prova A1 (7 pts) · Q8 objetiva — caiu 2×", "tag": "prova antiga · 2×",
  "enun": "Luís, 15 anos, há 2 semanas com febre baixa, tosse, mal-estar, fadiga e odinofagia. Tomou por conta própria um antibiótico e surgiu rash difuso. Exame: linfadenopatia generalizada, esplenomegalia e edema palpebral. Hemograma: linfocitose com grande atipia linfocitária. Diagnóstico?",
  "alts": ["Mononucleose", "Escarlatina", "Eritema infeccioso", "Dengue"], "ok": 0,
  "coment": "<b>A — Mononucleose (EBV).</b> Febre + faringite + adenomegalia generalizada, esplenomegalia, edema palpebral (Hoagland), linfócitos atípicos e exantema após amoxicilina/ampicilina. <b>B</b>: não há lixa/Filatov/Pastia. <b>C</b>: face esbofeteada. <b>D</b>: dengue tem leucopenia, não linfocitose atípica com esplenomegalia.",
  "blk": ["e_mono"]},
]

DIV = {
 "saramp_iso": ["Isolamento no sarampo", "Slide 15: até <b>4 dias</b> após o exantema", "Slide 28: <b>5 dias</b> após o exantema",
                "Divergência interna: escreva “isolamento respiratório até 4–5 dias após o início do exantema”"],
 "saramp_ig": ["Imunoglobulina no sarampo", "Slide 28: <b>&lt; 1 ano</b>, até 6 dias", "MEDCURSO: <b>&lt; 6 meses</b> (≥ 6 meses recebe vacina de bloqueio)",
               "Prova da faculdade: <b>slide (&lt; 1 ano)</b>; cite o bloqueio a partir de 6 meses do cursinho em uma linha"],
 "escarl_gab": ["Tratamento da escarlatina no gabarito", "Slide 53: <b>benzatina</b> dose única (600 mil &lt; 25 kg / 1,2 milhão &gt; 25 kg)",
                "Gabarito oficial 2025/2: “<b>amoxicilina 10 dias</b> (ou macrolídeo) + afastamento por <b>48 h</b>”",
                "Escreva <b>as duas opções</b> e o afastamento de 48 h"],
 "var_bloq": ["Prazo do bloqueio da varicela", "Slide 66: vacina até <b>72–96 h</b>", "MEDCURSO: até <b>5 dias</b>", "Prova: <b>72–96 h</b> (slide)"],
 "b19_inc": ["Incubação do eritema infeccioso", "Slide 72: <b>4–14 dias</b>", "MEDCURSO: ~<b>16 dias</b>", "Prova: <b>4–14 dias</b> (slide)"],
 "subito_rot": ["Rótulo dos slides do exantema súbito", "Slides 80–83 têm o título “Eritema infeccioso”", "O conteúdo é de <b>exantema súbito</b> (HHV-6)",
                "Erro de rótulo: estude o conteúdo como exantema súbito"],
 "mono_inc": ["Incubação da mononucleose", "Slide 84: “10 até 30–50 dias”", "MEDCURSO: 30 a 50 dias", "Prova: o slide"],
 "kawa_aneu": ["Aneurisma sem tratamento no Kawasaki", "Slide 99: <b>15–25%</b>", "Slide 100: <b>20–30%</b> → 4–5% tratado",
               "Divergência interna: “cerca de 20–25% sem tratamento; ~5% com IGIV até o 10º dia”. Prognóstico = <b>bom se tratado</b>"],
}

FLASH = [
 [2, "Só duas exantemáticas por aerossol?", "Sarampo e varicela."],
 [2, "Pródromo do sarampo?", "3 C: tosse, coriza, conjuntivite + febre crescente."],
 [2, "Sinal patognomônico do sarampo?", "Manchas de Koplik."],
 [2, "Complicação bacteriana mais comum e principal causa de morte no sarampo?", "Otite média; pneumonia."],
 [2, "Bloqueio do sarampo: idade e prazo?", "≥ 6 meses, até 72 h."],
 [2, "Imunoglobulina do sarampo: prazo e quem (slide)?", "Até 6 dias; < 1 ano (MEDCURSO < 6 meses), gestante, imunodeprimido."],
 [2, "Rubéola: gânglios típicos?", "Retroauricular, occipital, cervical posterior."],
 [2, "Rubéola congênita: tríade?", "Catarata, surdez, cardiopatia (PCA)."],
 [2, "Filatov e Pastia?", "Filatov = palidez perioral; Pastia = linhas petequiais nas dobras."],
 [2, "Benzatina na escarlatina?", "600.000 UI < 25 kg; 1.200.000 UI > 25 kg, IM dose única."],
 [2, "Afastamento da escola na escarlatina?", "24–48 h após antibiótico eficaz (gabarito: 48 h)."],
 [2, "Varicela: quando acaba o contágio?", "Quando todas as lesões estão em crosta."],
 [2, "Bloqueio da varicela a partir de?", "9 meses, até 72–96 h."],
 [2, "VZIG: prazo?", "Até 96 h."],
 [2, "RN de mãe com varicela: janela da VZIG?", "Varicela materna de 5 dias antes a 2 dias depois do parto."],
 [2, "Crise aplásica do B19: reticulócitos?", "Baixos (reticulocitopenia)."],
 [2, "Exantema súbito: quando aparece a mancha?", "Quando a febre cai em crise (após 3–4 dias)."],
 [2, "Mono: 3 achados que separam da escarlatina?", "Adenomegalia generalizada, esplenomegalia, linfócitos atípicos."],
 [2, "Kawasaki: critério de febre e nº de critérios?", "Febre ≥ 5 dias + 4 de 5."],
 [2, "Kawasaki: tratamento?", "IGIV 2 g/kg em 10 h + AAS 80–100 → 3–5 mg/kg/dia 6–8 sem, até o 10º dia."],
]

COLA = [["Cap. 2 · Exantemáticas", [
 ["Aerossol", "sarampo e varicela"], ["Sarampo bloqueio", "≥ 6 m · 72 h"], ["Sarampo Ig", "6 dias · < 1 ano (slide)"],
 ["Rubéola vacina", "evitar gravidez 30 dias"], ["Benzatina", "600 mil < 25 kg · 1,2 mi > 25 kg"], ["Escarlatina VO", "amoxicilina 10 dias · afastar 48 h"],
 ["Varicela bloqueio", "≥ 9 m · 72–96 h"], ["VZIG", "até 96 h"], ["RN mãe varicela", "−5 a +2 dias do parto"],
 ["Prematuro", "≥ 28 sem: só se mãe não imune · < 28 sem/< 1.000 g: sempre"], ["B19", "crise aplásica: retic ↓"],
 ["Exantema súbito", "6 m–2 a · febre 3–4 d cai → exantema"], ["Kawasaki", "febre ≥ 5 d + 4/5 · < 5 anos"],
 ["IGIV / AAS", "2 g/kg em 10 h · AAS 80–100 → 3–5 mg/kg/dia"], ["Aneurisma", "20–30% → 4–5%"]]]]

KS = [
 {"id": "k_e_esc", "cap": 2, "blk": ["e_escarl", "e_mono"], "t": "Amigdalite + amoxicilina + exantema (caiu 2×)",
  "src": "Prova A1 (3 pts) · Q1 alta taxonomia (1,0 pt) — Profa. Patrícia",
  "enun": "Paciente de 7 anos, febre alta há 48 h e odinofagia. Diagnosticada amigdalite bacteriana e prescrita amoxicilina. No mesmo dia surge exantema eritematopapular <b>em lixa</b>, que começa no tórax e se espalha. Retorna após 24 h de antibiótico, com piora do exantema. Ao exame: linfonodos cervicais anteriores e posteriores, <b>palidez perioral</b>, <b>hipertrofia de papilas da língua</b> e <b>linhas petequiais em antebraços</b>.",
  "p": [{"p": "Cite dois diagnósticos possíveis. (0,4)",
         "m": "<b>Escarlatina</b> × <b>mononucleose infecciosa</b> (o exantema após amoxicilina da mono é o distrator).",
         "c": ["escarlatina", "mononucleose"]},
        {"p": "Qual o diagnóstico mais provável e por quê? (0,2)",
         "m": "<b>Escarlatina</b>: exantema em lixa + <b>Filatov</b> (palidez perioral) + língua em <b>framboesa</b> + <b>Pastia</b> (linhas petequiais nas dobras/antebraços). Na mono esperaria adenomegalia generalizada, esplenomegalia e linfócitos atípicos.",
         "c": ["escarlatina", "lixa", "Filatov", "Pastia", "framboesa", "sem esplenomegalia"]},
        {"p": "Tratamento e prazo de afastamento da escola. (0,4)",
         "m": "Manter antibiótico: <b>amoxicilina 10 dias</b> (ou penicilina V / macrolídeo; azitromicina 5 dias) <b>ou penicilina benzatina IM dose única</b> (600.000 UI se &lt; 25 kg; 1.200.000 UI se &gt; 25 kg). Afastar da escola até <b>24–48 h após o início do antibiótico</b> (gabarito: 48 h).",
         "c": ["amoxicilina", "10 dias", "penicilina benzatina", "600.000", "25 kg", "48 h"]}]},
 {"id": "k_e_3", "cap": 2, "blk": ["e_escarl", "e_subito", "e_kawa"], "t": "Três exantemas, três condutas",
  "src": "Prova A1 (7 pts) · Q2 média taxonomia (1,5 pt) — Profa. Patrícia",
  "enun": "<b>Caso 1:</b> 9 anos, amigdalite há 5 dias não tratada; hoje febre, exantema eritematoso difuso, palidez perioral, língua com hipertrofia de papilas.<br><b>Caso 2:</b> 18 meses, febre &gt; 39 °C por 3 dias; no último dia de febre, discreto exantema róseo papular no dorso que sumiu em &lt; 24 h.<br><b>Caso 3:</b> 15 meses, febre persistente há mais de 5 dias; hiperemia conjuntival bilateral, edema de mãos e pés, eritema e fissuras labiais, exantema polimorfo.",
  "p": [{"p": "Hipótese de cada caso. (0,9)",
         "m": "1) <b>Escarlatina</b>. 2) <b>Exantema súbito (roséola, HHV-6)</b> — exantema quando a febre cai. 3) <b>Doença de Kawasaki</b>.",
         "c": ["escarlatina", "exantema súbito", "HHV-6", "Kawasaki"]},
        {"p": "Prognóstico de cada um. (0,3)",
         "m": "Escarlatina: bom, mas pode complicar (abscesso periamigdaliano, otite; febre reumática, GNPE). Roséola: bom, autolimitada (atenção à convulsão febril). Kawasaki: <b>bom se tratado a tempo</b>; sem tratamento ~20–25% fazem aneurisma coronariano.",
         "c": ["febre reumática", "GNPE", "convulsão febril", "bom se tratado", "aneurisma coronariano"]},
        {"p": "Tratamento de cada um. (0,3)",
         "m": "Escarlatina: penicilina benzatina dose única ou amoxicilina 10 dias. Roséola: sintomático (antitérmico). Kawasaki: <b>imunoglobulina EV 2 g/kg em 10 h</b> (até o 10º dia) + <b>AAS 80–100 mg/kg/dia</b> até afebril → <b>3–5 mg/kg/dia por 6–8 semanas</b>.",
         "c": ["benzatina", "amoxicilina", "sintomático", "imunoglobulina", "2 g/kg", "AAS", "10º dia"]}]},
]
