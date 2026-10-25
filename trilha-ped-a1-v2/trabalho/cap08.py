CAP = {"n": 8, "t": "Meningites bacterianas", "short": "Meningites", "aula": "Aula 8 · slides da Patrícia",
       "icon": "🧠", "col": "#5B3F8C",
       "bul": ["&lt; 2 meses: ampicilina + cefotaxima (caiu 2×)",
               "&gt; 2 meses: ceftriaxona/cefotaxima + vancomicina",
               "Líquor: bacteriana &gt; 1.000, neutrófilos, glicose &lt; 30 · TB: proteína muito alta",
               "Profilaxia: meningo rifampicina 10 mg/kg 12/12 h × 2 d · Hib 20 mg/kg/dia × 4 d"],
       "medalha": ["🧠", "Punção de mão firme"]}

BLOCKS = [
 {"id": "m_epi", "t": "Epidemiologia: quem, quando, quanto mata",
  "s": "Inflamação das <b>leptomeninges</b>; mais em <b>&lt; 5 anos</b>, sobretudo <b>3–12 meses</b>. A maioria é <b>viral</b>; bacteriana não tratada ≈ <b>100% de mortalidade</b>. "
       "<br>Brasil 2007–2020: 265.644 casos (121.955 virais, 87.993 bacterianas). <b>Meningococo</b> lidera as bacterianas; sorogrupo <b>C</b> predomina, mas o <b>B cresce</b> e já domina em 0–4 anos. "
       "<br><b>Hib caiu 95%</b> após a vacina (1999); pneumococo caiu em &lt; 2 anos com a VPC10 (2010), mas tem a maior letalidade (26,9–31,1%).",
  "fala": "Meningite é a inflamação das leptomeninges, e a faixa de maior risco é abaixo de cinco anos, principalmente entre três e doze meses. A maioria é viral, mas a bacteriana sem tratamento mata quase sempre. No Brasil o meningococo é o agente bacteriano mais comum, com o sorogrupo B crescendo nas crianças pequenas; o hemófilo praticamente sumiu com a vacina, e o pneumococo é o que mais mata.",
  "div": "letal",
  "pega": "Mais comum: <b>meningococo</b>; maior letalidade: <b>pneumococo</b>; Hib ↓ <b>95%</b> com a vacina.",
  "z": "O hemófilo virou peça de museu graças à vacina; o pneumococo continua matando um em cada três. Vacina em dia, caralho.",
  "ills": ["m_epi"]},
 {"id": "m_etio", "t": "Agente por faixa etária e por condição",
  "s": "<b>Até 2 meses</b>: <b>enterobactérias</b> (<i>E. coli</i>), <b>estreptococo do grupo B</b>, <b><i>Listeria</i></b>. "
       "<br><b>&gt; 2 meses</b>: <b>meningococo, pneumococo</b>, <i>H. influenzae</i> b. <b>6–21 anos</b>: meningococo e pneumococo. "
       "<br><b>Asplenia / falciforme / deficiência de complemento</b> → encapsulados. <b>DVP / neurocirurgia</b> → estafilococos, <i>Pseudomonas</i>. "
       "<br>Via principal: <b>hematogênica</b> a partir da colonização da nasofaringe.",
  "fala": "O agente depende da idade. Até dois meses, pense nos germes do canal de parto e do berçário: enterobactérias como a Escherichia coli, estreptococo do grupo B e Listeria. Depois de dois meses entram meningococo, pneumococo e hemófilo. Criança sem baço, falciforme ou com deficiência de complemento sofre com encapsulados, e quem tem derivação ventricular sofre com estafilococo e pseudomonas.",
  "pega": "<i>Listeria</i> no &lt; 2 meses é o motivo da <b>ampicilina</b> (cefalosporina não cobre Listeria).",
  "z": "Listeria não liga pra cefalosporina nenhuma. Recém-nascido sem ampicilina no esquema é recém-nascido descoberto, porra.",
  "ills": ["m_etio"]},
 {"id": "m_clin", "t": "Quadro clínico: do escolar ao recém-nascido",
  "s": "<b>Tríade</b>: <b>febre, cefaleia, vômitos</b> + sinais meníngeos (<b>rigidez de nuca, Kernig, Brudzinski</b>). Hib insidioso; pneumo e meningo abruptos. <b>Convulsão precoce</b> em 20–30% (sem pior prognóstico). "
       "<br><b>Meningococo</b>: petéquias/púrpura em ~60%. "
       "<br><b>Lactente/RN</b>: inespecífico — irritabilidade, choro ao ser pego, recusa alimentar, <b>hipotermia</b>, gemência, icterícia; febre e rigidez <b>nem sempre</b>; <b>fontanela abaulada</b> em 1/3; convulsões em 40%.",
  "fala": "Na criança maior a meningite se apresenta com febre, cefaleia e vômitos, mais rigidez de nuca e os sinais de Kernig e Brudzinski, e uma convulsão no início não piora o prognóstico. No meningococo, petéquias e púrpura aparecem em mais da metade. O problema é o lactente e o recém-nascido: o quadro é inespecífico, com irritabilidade, recusa alimentar, hipotermia e gemência, e febre e rigidez de nuca podem faltar. Fontanela abaulada aparece em um terço.",
  "pega": "RN com <b>hipotermia, recusa alimentar e gemência</b> sem rigidez de nuca <b>pode</b> ter meningite — punção.",
  "z": "Recém-nascido não lê livro: ele não tem rigidez de nuca, ele fica frio e para de mamar. Punciona, caralho.",
  "ills": ["m_clin"]},
 {"id": "m_puncao", "t": "Punção lombar imediata — mas nunca postergar o antibiótico",
  "s": "<b>Líquor imediatamente</b>, <b>exceto</b>: <b>instabilidade hemodinâmica</b>/respiratória · <b>sinais focais ou de HIC</b> · <b>coagulopatia</b>/plaquetopenia grave · infecção no local. "
       "<br>Em vermelho e sublinhado (slide 22): <b>MAS NUNCA POSTERGAR TRATAMENTO</b> — atraso de 3–6 h aumenta a mortalidade. "
       "<br>Com exceção: <b>hemocultura + antibiótico já</b>, punção depois; antígenos e PCR continuam úteis após o antibiótico.",
  "fala": "A regra da aula tem duas metades. A primeira: o líquor deve ser colhido imediatamente, a não ser que a criança esteja instável, tenha sinais focais ou de hipertensão intracraniana, ou coagulopatia. A segunda, que a professora escreveu em vermelho e sublinhou: nunca postergar o tratamento. Se não dá para puncionar agora, colhe hemocultura e começa o antibiótico, porque cada hora de atraso aumenta a mortalidade.",
  "pega": "Criança em <b>choque com púrpura</b>: <b>suporte + hemocultura + antibiótico imediato</b>; punção adiada. Tomografia de rotina antes da punção <b>só atrasa</b>.",
  "z": "Esperar tomografia pra dar ceftriaxona numa criança com púrpura e hipotensa é deixar o meningococo ganhar a corrida. Antibiótico primeiro, punção depois, porra.",
  "ills": ["m_puncao"]},
 {"id": "m_lcr", "t": "O líquor: viral × bacteriana × tuberculosa (slide 26)",
  "s": "<table class=t><tr><th></th><th>Bacteriana</th><th>Viral</th><th>Tuberculosa</th></tr>"
       "<tr><td>Células</td><td><b>&gt; 1.000</b></td><td>&lt; 1.000</td><td>20–500</td></tr>"
       "<tr><td>Predomínio</td><td><b>neutrófilos</b></td><td>linfócitos</td><td>linfócitos</td></tr>"
       "<tr><td>Proteína</td><td>100–200</td><td>normal/↑ leve</td><td><b>&gt; 100 (muito alta)</b></td></tr>"
       "<tr><td>Glicose</td><td><b>&lt; 30</b></td><td>normal</td><td>baixa</td></tr>"
       "<tr><td>Microbiologia</td><td>Gram + em ~85%</td><td>—</td><td>Ziehl-Neelsen + em 30%</td></tr></table>"
       "<br>Aspecto turvo na bacteriana. Antígenos 70–90%; hemocultura positiva em até 90%. Viral nas primeiras 48 h pode ter neutrófilos.",
  "fala": "A tabela do líquor é questão certa. Bacteriana: mais de mil células, com neutrófilos, proteína entre cem e duzentos e glicose abaixo de trinta, com Gram positivo em oitenta e cinco por cento. Viral: menos de mil células, linfócitos, proteína e glicose normais. Tuberculosa: poucas células, de vinte a quinhentas, linfócitos, mas proteína muito alta e glicose baixa, com Ziehl-Neelsen positivo em só trinta por cento.",
  "div": "lcr_viral",
  "pega": "Tuberculosa: <b>poucas células</b> mas a <b>maior proteína</b> + glicose baixa. Diplococo <b>Gram-negativo</b> = meningococo.",
  "z": "Líquor turvo, glicose vinte e mil células de neutrófilo: isso é pus, não é virose. Ceftriaxona, porra.",
  "ills": ["m_lcr"]},
 {"id": "m_trat", "t": "Tratamento empírico por idade, doses e duração",
  "s": "Suporte: <b>SF 20 mL/kg em 5–10 min</b> se choque, UTI conforme gravidade, controle de convulsão e HIC. "
       "<br><b>Até 2 meses (60 dias)</b>: <b>ampicilina + cefotaxima</b> (2ª opção: ampicilina + aminoglicosídeo/gentamicina). "
       "<br><b>&gt; 2 meses</b>: <b>ceftriaxona (ou cefotaxima) + vancomicina</b> — nunca vancomicina isolada (penetração ruim). "
       "<br>Doses (slide 33): <b>ceftriaxona 100 mg/kg/dia 12/12 h</b> · cefotaxima 200 mg/kg/dia 6/6 h · <b>ampicilina 200–300 mg/kg/dia 6/6 h</b> · <b>vancomicina 60 mg/kg/dia 6/6 h</b>. "
       "<br>Duração: meningococo <b>5–7 d</b> · Hib 7–10 · pneumococo <b>10–14</b> · Gram-negativo 21 dias.",
  "fala": "O esquema empírico depende da idade. Até dois meses, ampicilina para cobrir Listeria e enterococo, mais cefotaxima para enterobactérias; a segunda opção é ampicilina com gentamicina. Acima de dois meses, ceftriaxona ou cefotaxima mais vancomicina, para pneumococo resistente, e nunca vancomicina sozinha. A ceftriaxona é cem miligramas por quilo por dia de doze em doze horas. Meningococo trata de cinco a sete dias e pneumococo de dez a catorze.",
  "pega": "No RN a cefalosporina é <b>cefotaxima</b> (ceftriaxona desloca bilirrubina). &gt; 2 meses: <b>C3G + vancomicina</b>.",
  "z": "Menor de dois meses: ampicilina mais cefotaxima. Maior: ceftriaxona mais vanco. Trocou os dois, deixou a Listeria ou o pneumococo resistente de presente, caralho.",
  "ills": ["m_trat"]},
 {"id": "m_dexa", "t": "Dexametasona: dose, idade e momento",
  "s": "<b>Dexametasona 0,15 mg/kg/dose IV 6/6 h por 2 dias</b>, em crianças <b>&gt; 6 semanas</b>, na meningite <b>bacteriana</b>. "
       "<br>Reduz <b>perda auditiva grave</b> e sequelas neurológicas (sobretudo Hib). <b>Previne, mas não reverte</b> → dar <b>antes ou junto da 1ª dose</b> do antibiótico.",
  "fala": "A dexametasona na meningite bacteriana é zero vírgula quinze miligrama por quilo por dose, de seis em seis horas, por dois dias, acima de seis semanas de vida. Ela reduz a surdez grave e outras sequelas, mas só previne, não reverte a lesão já instalada, por isso entra antes ou junto da primeira dose do antibiótico, nunca no terceiro dia.",
  "div": "dexa",
  "pega": "Dexa: <b>&gt; 6 semanas</b>, <b>0,15 mg/kg 6/6 h × 2 dias</b>, <b>antes/junto</b> do antibiótico. Não é para meningite viral.",
  "z": "Dexametasona no terceiro dia é colocar cinto de segurança depois da batida. Antes ou junto da primeira dose, porra.",
  "ills": ["m_dexa"]},
 {"id": "m_profil", "t": "Quimioprofilaxia: meningococo × Hib",
  "s": "<b>Meningococo</b>: <b>todo contato íntimo</b> (domicílio, creche, quem dormiu junto) dos 7 dias prévios, <b>vacinado ou não</b>: "
       "<br>• <b>rifampicina 10 mg/kg (máx 600 mg) 12/12 h por 2 dias</b> (RN 5 mg/kg 12/12 h) · ceftriaxona IM dose única 125 mg (&lt; 15 a) / 250 mg (≥ 15 a) · ciprofloxacina 500 mg (≥ 18 a) · azitromicina 10 mg/kg. "
       "<br><b>Hib</b>: se na casa há <b>criança &lt; 4 anos não vacinada ou parcialmente vacinada</b> → <b>todos os contatos domiciliares</b>: <b>rifampicina 20 mg/kg (máx 600) 1×/dia por 4 dias</b>. "
       "<br>Paciente: precaução respiratória nas primeiras <b>24–48 h</b> de antibiótico. Notificar.",
  "fala": "Na doença meningocócica, todo contato íntimo dos últimos sete dias recebe quimioprofilaxia, tendo vacina ou não: rifampicina, dez miligramas por quilo, máximo seiscentos, de doze em doze horas, por dois dias; alternativas são ceftriaxona intramuscular em dose única ou ciprofloxacina no adulto. No hemófilo, se houver na casa uma criança abaixo de quatro anos com vacina incompleta, todos os contatos da casa recebem rifampicina, vinte miligramas por quilo, uma vez ao dia, por quatro dias.",
  "pega": "Meningo: <b>10 mg/kg 12/12 h × 2 d</b>, <b>independe da vacina</b>. Hib: <b>20 mg/kg 1×/dia × 4 d</b>, para <b>todos</b> da casa se há &lt; 4 anos mal vacinado.",
  "z": "Irmão vacinado com meningo C dormindo no mesmo quarto? Rifampicina igual: a vacina C não cobre o B, porra.",
  "ills": ["m_profil"]},
 {"id": "m_vac", "t": "Vacinas que previnem meningite",
  "s": "<b>Meningocócica C</b>: 3, 5 e 12 meses (ACWY no adolescente). <b>Pentavalente</b> (inclui Hib): 2, 4 e 6 meses. <b>Pneumocócica 10</b>: 2, 4 e reforço aos 12 meses. "
       "<br><b>BCG</b>: protege contra as formas graves da tuberculose — <b>miliar e meníngea</b>.",
  "fala": "As vacinas do calendário que previnem meningite são a meningocócica C aos três, cinco e doze meses, com a ACWY no adolescente; a pentavalente, que inclui o hemófilo, aos dois, quatro e seis meses; e a pneumocócica dez aos dois, quatro e doze meses. E a BCG, aplicada ao nascer, existe justamente para prevenir as formas graves da tuberculose: a miliar e a meníngea.",
  "div": "acwy",
  "pega": "BCG previne <b>meningite tuberculosa</b> e miliar (não a TB pulmonar do adulto).",
  "z": "BCG não é vacina de tuberculose de pulmão de adulto; é vacina pra criança não ter meningite tuberculosa. Erra isso e leva bronca da Patrícia, caralho.",
  "m": [["MEDCURSO · S27 P01 02:22–03:38", "A BCG protege contra as formas graves: miliar e meníngea."]],
  "ills": ["m_vac"]},
]

ILLS = {
 "m_epi": cards("Meningite no Brasil", [
     ("👶", "Quem", "< 5 anos, pico 3–12 meses", "p"),
     ("🦠", "Mais comum", "meningococo (C predomina; B cresce em 0–4 a)", "v"),
     ("☠️", "Maior letalidade", "pneumococo 26,9–31,1%", "r"),
     ("💉", "Hib", "↓ 95% após a vacina (1999)", "g")],
     foot="Bacteriana não tratada ≈ 100% de mortalidade"),
 "m_etio": table("Agente por idade e condição", [
     ("Até 2 meses", "enterobactérias (E. coli) · estrepto grupo B · Listeria"),
     ("> 2 meses", "meningococo · pneumococo · H. influenzae b"),
     ("6–21 anos", "meningococo e pneumococo"),
     ("Asplenia / falciforme", "encapsulados"),
     ("DVP / neurocirurgia", "estafilococos · Pseudomonas")], cor="p",
     foot="Via principal: hematogênica a partir da nasofaringe", fcor="t"),
 "m_clin": versus("Clínica por idade", ("🧒", "Criança maior", "p", [
     "• febre, cefaleia, vômitos", "• rigidez de nuca", "• Kernig, Brudzinski", "• convulsão precoce 20–30%", "• púrpura: meningococo (60%)"]),
     ("👶", "RN / lactente", "r", [
     "• irritabilidade, choro ao colo", "• recusa alimentar, gemência", "• hipotermia, icterícia", "• fontanela abaulada (1/3)", "✘ febre e rigidez podem faltar"])),
 "m_puncao": flow("Punção e antibiótico: a ordem certa", [
     ("💉", "Líquor imediatamente", "regra geral", "p"),
     ("⛔", "Exceto", "instabilidade · sinais focais / HIC · coagulopatia · infecção local", "a"),
     ("🩸", "Na exceção", "hemocultura + antibiótico já; punção depois", "r"),
     ("⏱️", "NUNCA POSTERGAR TRATAMENTO", "atraso de 3–6 h aumenta mortalidade", "r")]),
 "m_lcr": table("Líquor (slide 26)", [
     ("Bacteriana", "> 1.000 · neutrófilos · proteína 100–200 · glicose < 30 · Gram + 85%"),
     ("Viral", "< 1.000 · linfócitos · proteína e glicose normais"),
     ("Tuberculosa", "20–500 · linfócitos · proteína > 100 · glicose baixa · ZN + 30%"),
     ("Diplococo Gram −", "meningococo"),
     ("Pegadinha", "viral nas primeiras 48 h pode ter neutrófilos")], cor="p", kw=170),
 "m_trat": flow("Tratamento empírico", [
     ("💧", "Suporte", "SF 20 mL/kg em 5–10 min se choque · convulsão · HIC", "t"),
     ("🍼", "Até 2 meses", "ampicilina 200–300 mg/kg/dia + cefotaxima 200 mg/kg/dia (6/6 h)", "v"),
     ("🧒", "> 2 meses", "ceftriaxona 100 mg/kg/dia 12/12 h + vancomicina 60 mg/kg/dia 6/6 h", "p"),
     ("📆", "Duração", "meningo 5–7 · Hib 7–10 · pneumo 10–14 · Gram-negativo 21 dias", "a")],
     foot="2ª opção no RN: ampicilina + gentamicina · nunca vancomicina isolada"),
 "m_dexa": cards("Dexametasona na meningite bacteriana", [
     ("💊", "Dose", "0,15 mg/kg/dose IV 6/6 h", "p"),
     ("📆", "Duração", "2 dias", "a"),
     ("🎂", "Idade", "> 6 semanas de vida", "t"),
     ("⏰", "Momento", "antes ou junto da 1ª dose — previne, não reverte", "r")],
     foot="Reduz perda auditiva grave e sequelas", fcor="g"),
 "m_profil": versus("Quimioprofilaxia", ("🦠", "Meningococo", "v", [
     "• todo contato íntimo (7 dias)", "• vacinado ou não", "• rifampicina 10 mg/kg 12/12 h × 2 d", "• RN 5 mg/kg · máx 600 mg", "• alt.: ceftriaxona IM 125/250 mg"]),
     ("🧫", "Hib", "a", [
     "• casa com < 4 anos mal vacinado", "• → todos os contatos da casa", "• rifampicina 20 mg/kg 1×/dia × 4 d", "• máx 600 mg"]),
     foot="Paciente: precaução respiratória 24–48 h · notificar", fcor="p"),
 "m_vac": table("Vacinas contra meningite", [
     ("Meningocócica C", "3, 5 e 12 meses (ACWY no adolescente)"),
     ("Pentavalente (Hib)", "2, 4 e 6 meses"),
     ("Pneumocócica 10", "2, 4 e 12 meses"),
     ("BCG", "ao nascer — formas graves da TB: miliar e meníngea")], cor="g"),
}

QMAP = {0: ["m_puncao", "m_trat"], 1: ["m_lcr"], 2: ["m_lcr", "m_vac"], 3: ["m_trat", "m_clin"], 4: ["m_profil"], 5: ["m_profil"], 6: ["m_dexa"], 7: ["m_puncao"]}

Q = [
 {"id": "qn_lcr", "cap": 8, "src": "autoral", "orig": "Tour Provas · questão nova no estilo da professora", "tag": "líquor",
  "enun": "Lactente de 10 meses, febre há 2 dias e irritabilidade. Líquor: 600 células/mm³ com predomínio de linfócitos, proteína 40 mg/dL, glicose 58 mg/dL (glicemia 90), bacterioscopia negativa. A interpretação mais adequada pelo slide da professora é:",
  "alts": ["Meningite bacteriana parcialmente tratada", "Meningite viral", "Meningite tuberculosa", "Líquor normal para a idade"], "ok": 1,
  "coment": "<b>B — Meningite viral.</b> &lt; 1.000 células com linfócitos, proteína e glicose normais. <b>C</b>: tuberculosa exigiria glicose baixa e proteína muito elevada. <b>A</b>: bacteriana teria neutrófilos, glicose &lt; 30 e proteína 100–200. <b>D</b>: 600 células nunca é normal.",
  "blk": ["m_lcr"]},
]

DIV = {
 "letal": ["Letalidade das meningites no Brasil", "Slide 6: “5.581 mortes (taxa de letalidade <b>20%</b>)” sobre 265.644 casos",
           "5.581 / 265.644 ≈ <b>2,1%</b> — um dos dois números está errado", "Não use esse número na prova; use “pneumococo 26,9–31,1%”"],
 "lcr_viral": ["Celularidade da meningite viral", "Slide 26: <b>&lt; 1.000</b> células", "Apostila PED 5: em geral &lt; 500; neutrófilos nas primeiras 48 h",
               "Prova: corte da professora (<b>&lt; 1.000</b>). Residência: glicose &lt; 40 ou relação líquor/sangue &lt; 0,4"],
 "dexa": ["Idade da dexametasona × esquema neonatal", "Slide 35: dexametasona <b>&gt; 6 semanas</b>", "Esquema neonatal (ampicilina + cefotaxima) vai até <b>60 dias</b>",
          "Sobreposição de 6 a 8 semanas: escreva “&gt; 6 semanas, antes ou junto da 1ª dose”"],
 "acwy": ["ACWY no adolescente", "Slide 42: 11–12 anos incompletos", "Apostila PED 3: 11 a 14 anos desde 2022", "Faculdade: slide; residência: calendário vigente"],
}

FLASH = [
 [8, "Faixa de maior risco de meningite?", "< 5 anos, sobretudo 3–12 meses."],
 [8, "Agente bacteriano mais comum e o de maior letalidade?", "Meningococo; pneumococo."],
 [8, "Agentes até 2 meses?", "Enterobactérias, estrepto do grupo B, Listeria."],
 [8, "Empírico < 2 meses?", "Ampicilina + cefotaxima (2ª: ampicilina + gentamicina)."],
 [8, "Empírico > 2 meses?", "Ceftriaxona/cefotaxima + vancomicina."],
 [8, "Dose de ceftriaxona?", "100 mg/kg/dia 12/12 h."],
 [8, "Dose de vancomicina?", "60 mg/kg/dia 6/6 h."],
 [8, "Exceções à punção imediata?", "Instabilidade, sinais focais/HIC, coagulopatia."],
 [8, "Frase em vermelho do slide 22?", "Nunca postergar tratamento."],
 [8, "Líquor bacteriano?", "> 1.000, neutrófilos, proteína 100–200, glicose < 30."],
 [8, "Líquor tuberculoso?", "20–500, linfócitos, proteína > 100, glicose baixa; ZN + 30%."],
 [8, "Dexametasona?", "0,15 mg/kg 6/6 h × 2 dias, > 6 semanas, antes/junto do antibiótico."],
 [8, "Profilaxia meningococo?", "Rifampicina 10 mg/kg (máx 600) 12/12 h × 2 dias, vacinado ou não."],
 [8, "Profilaxia Hib?", "Rifampicina 20 mg/kg 1×/dia × 4 dias, todos da casa se < 4 anos mal vacinado."],
 [8, "Duração: meningo × pneumo?", "5–7 dias × 10–14 dias."],
 [8, "BCG previne?", "Formas graves da TB: miliar e meníngea."],
]

COLA = [["Cap. 8 · Meningites", [
 ["< 2 meses", "ampicilina + cefotaxima"], ["> 2 meses", "ceftriaxona + vancomicina"], ["Ceftriaxona", "100 mg/kg/dia 12/12 h"],
 ["Cefotaxima", "200 mg/kg/dia 6/6 h"], ["Ampicilina", "200–300 mg/kg/dia 6/6 h"], ["Vancomicina", "60 mg/kg/dia 6/6 h"],
 ["LCR bacteriana", "> 1.000 · PMN · ptn 100–200 · glic < 30"], ["LCR viral", "< 1.000 · linfo · normal"], ["LCR TB", "20–500 · linfo · ptn > 100 · glic ↓"],
 ["Dexa", "0,15 mg/kg 6/6 h × 2 d · > 6 sem"], ["Meningo profilaxia", "rifampicina 10 mg/kg 12/12 h × 2 d"],
 ["Hib profilaxia", "rifampicina 20 mg/kg/dia × 4 d"], ["Duração", "meningo 5–7 · Hib 7–10 · pneumo 10–14 · Gram − 21"]]]]

KS = [
 {"id": "k_m_rn", "cap": 8, "blk": ["m_trat", "m_etio"], "t": "Meningite em menor de 2 meses (caiu 2×)",
  "src": "Caiu em 2 provas antigas (0,5 pt) — Profa. Patrícia",
  "enun": "Lactente de 5 semanas, 4 kg, com hipotermia, recusa alimentar e gemência. Líquor com pleocitose neutrofílica.",
  "p": [{"p": "Cite o tratamento empírico da meningite em crianças menores de 2 meses.",
         "m": "<b>Ampicilina + cefalosporina de 3ª geração (cefotaxima)</b>. 2ª opção: <b>ampicilina + aminoglicosídeo</b> (gentamicina). A ampicilina cobre <i>Listeria</i> e enterococo. Doses (slide 33): ampicilina 200–300 mg/kg/dia 6/6 h · cefotaxima 200 mg/kg/dia 6/6 h.",
         "c": ["ampicilina", "cefotaxima", "gentamicina", "Listeria", "200 mg/kg/dia"]},
        {"p": "Quais os agentes prováveis nessa idade?",
         "m": "<b>Enterobactérias</b> (<i>E. coli</i>), <b>estreptococo do grupo B</b> e <b><i>Listeria monocytogenes</i></b>.",
         "c": ["enterobactérias", "E. coli", "estreptococo do grupo B", "Listeria"]}]},
 {"id": "k_m_bact", "cap": 8, "blk": ["m_lcr", "m_trat", "m_dexa", "m_clin"], "t": "Meningite bacteriana na criança maior (2025/2)",
  "src": "Prova 2025/2 · Q3 (1,5 pt) — gabarito mínimo oficial",
  "enun": "Menino de 5 anos, 18 kg, febre alta, cefaleia e vômitos há 12 h; teve uma convulsão em casa. Rigidez de nuca, Kernig e Brudzinski positivos. Líquor <b>turvo</b>: 2.800 leucócitos com 90% de neutrófilos, proteína 180 mg/dL, glicose 20 mg/dL, bacterioscopia com diplococos.",
  "p": [{"p": "Diagnóstico e justificativa. (0,6)",
         "m": "<b>Meningite bacteriana</b>: febre + cefaleia + vômitos, sinais de irritação meníngea, convulsão; líquor <b>turvo</b>, &gt; 1.000 células com <b>neutrófilos</b>, <b>glicose baixa</b> (&lt; 30), <b>proteína alta</b> (100–200), bacterioscopia positiva.",
         "c": ["meningite bacteriana", "rigidez de nuca", "turvo", "neutrófilos", "glicose baixa", "proteína alta"]},
        {"p": "Agentes prováveis. (0,3)",
         "m": "<b>Pneumococo</b> e <b>meningococo</b> (Hib raro após a vacina); diplococos sugerem pneumococo (Gram +) ou meningococo (Gram −).",
         "c": ["pneumococo", "meningococo", "Hib"]},
        {"p": "Tratamento. (0,6)",
         "m": "Suporte; <b>ceftriaxona 100 mg/kg/dia 12/12 h</b> (ou cefotaxima) <b>+ vancomicina 60 mg/kg/dia 6/6 h</b>; <b>dexametasona 0,15 mg/kg/dose 6/6 h por 2 dias</b>, antes ou junto da 1ª dose (&gt; 6 semanas); notificar e quimioprofilaxia dos contatos se meningococo.",
         "c": ["ceftriaxona", "100 mg/kg/dia", "vancomicina", "dexametasona", "0,15 mg/kg", "antes ou junto"]}]},
 {"id": "k_m_3lcr", "cap": 8, "blk": ["m_lcr", "m_profil"], "t": "Três líquores (treino no estilo da professora)",
  "src": "Tour Provas · questão nova no estilo da professora",
  "enun": "Três crianças com febre, cefaleia e vômitos fazem punção lombar:<br><b>A)</b> 2 anos: 3.200 células, 90% neutrófilos, proteína 180, glicose 18, Gram com diplococos Gram-negativos.<br><b>B)</b> 6 anos: 180 células, 85% linfócitos, proteína 45, glicose 60, Gram negativo.<br><b>C)</b> 4 anos, contato domiciliar com adulto tossidor, 3 semanas de febre e sonolência: 250 células, linfócitos, proteína 310, glicose 22.",
  "p": [{"p": "Qual o tipo de meningite em cada caso? Justifique pelo líquor.",
         "m": "<b>A = bacteriana</b> (&gt; 1.000, neutrófilos, proteína 100–200, glicose &lt; 30, Gram +). <b>B = viral</b> (&lt; 1.000, linfócitos, proteína e glicose normais). <b>C = tuberculosa</b> (20–500, linfócitos, <b>proteína muito alta</b>, <b>glicose baixa</b>, evolução arrastada, contato com TB).",
         "c": ["bacteriana", "viral", "tuberculosa", "neutrófilos", "linfócitos", "proteína muito alta", "glicose baixa"]},
        {"p": "Provável agente de A e conduta com o irmão de 5 anos que divide o quarto.",
         "m": "Diplococo Gram-negativo = <b>meningococo</b>. Irmão é contato íntimo → <b>quimioprofilaxia</b> independentemente da vacina: <b>rifampicina 10 mg/kg (máx. 600 mg) 12/12 h por 2 dias</b> (alternativa: ceftriaxona IM 125 mg dose única &lt; 15 anos). Paciente em precaução respiratória 24–48 h; notificar.",
         "c": ["meningococo", "rifampicina", "10 mg/kg", "12/12 h", "2 dias", "independente da vacina", "notificar"]},
        {"p": "Qual pesquisa no líquor de C tem baixa positividade?",
         "m": "<b>Ziehl-Neelsen</b>: positivo em só <b>30%</b> — a confirmação vem do isolamento do BK.",
         "c": ["Ziehl-Neelsen", "30%"]}]},
]
