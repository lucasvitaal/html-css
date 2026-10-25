CAP = {"n": 10, "t": "Choque na criança", "short": "Choque", "aula": "Aula 10 · slides da Patrícia",
       "icon": "🫀", "col": "#A8432A",
       "bul": ["PA normal não exclui choque: hipotensão é sinal tardio",
               "Hipotensão: RN &lt; 60 · 1–12 m &lt; 70 · 1–10 a &lt; 70 + 2 × idade · &gt; 10 a &lt; 90",
               "SF 20 mL/kg em 5–20 min, repetir; reavaliar após 40–60 mL/kg → amina",
               "Frio: adrenalina · quente: noradrenalina · IC: dobutamina · Holliday-Segar"],
       "medalha": ["🫀", "Primeira hora de ouro"]}

BLOCKS = [
 {"id": "s_conc", "t": "Choque: oferta × necessidade de oxigênio",
  "s": "Choque = <b>desequilíbrio entre oferta e necessidade de O₂</b> dos tecidos. Tripé: <b>volume – bomba – tônus</b>. "
       "<br>Oferta = conteúdo arterial de O₂ (Hb, SatO₂, pO₂) × <b>débito cardíaco</b> (FC × volume sistólico). PA = débito × resistência vascular. "
       "<br>A extração tecidual compensa até não conseguir → metabolismo anaeróbio → <b>lactato</b>.",
  "fala": "Choque é quando a oferta de oxigênio aos tecidos não dá conta da necessidade. A oferta depende do conteúdo de oxigênio no sangue, ou seja, hemoglobina e saturação, multiplicado pelo débito cardíaco. Por isso todo choque é falha de um dos três pés: volume, bomba ou tônus vascular. Enquanto os tecidos conseguem extrair mais oxigênio, a criança compensa; quando não conseguem, aparece o lactato.",
  "pega": "Choque é <b>perfusão</b>, não pressão: pode haver choque com <b>PA normal</b>.",
  "z": "Pressão normal não é salvo-conduto: o tecido pode estar se afogando em lactato com a pressão bonitinha no monitor, porra.",
  "ills": ["s_conc"]},
 {"id": "s_tipos", "t": "Os quatro tipos de choque",
  "s": "<b>Hipovolêmico</b>: desidratação (diarreia, vômitos), hemorragia, queimadura — <b>o mais comum</b>. "
       "<br><b>Distributivo</b>: <b>séptico</b>, anafilático, neurogênico (vasodilatação). "
       "<br><b>Cardiogênico</b>: cardiopatia, miocardite, arritmia, acidose. "
       "<br><b>Obstrutivo</b>: <b>pneumotórax hipertensivo</b>, <b>tamponamento</b>, TEP. "
       "<br>Mais comuns na criança: <b>hipovolemia e sepse</b>.",
  "fala": "São quatro tipos. O hipovolêmico, por diarreia, vômitos, sangramento ou queimadura, é o mais comum na criança. O distributivo é o choque da vasodilatação, como na sepse e na anafilaxia. O cardiogênico é a bomba que falha, como na miocardite. E o obstrutivo é o coração impedido de encher ou ejetar, no pneumotórax hipertensivo e no tamponamento. Na prática pediátrica, hipovolemia e sepse dominam.",
  "pega": "Mais comuns na criança: <b>hipovolêmico</b> e <b>séptico</b>.",
  "z": "Na pediatria o choque é quase sempre a diarreia que ninguém hidratou ou a sepse que ninguém viu. O resto é exceção, caralho.",
  "ills": ["s_tipos"]},
 {"id": "s_recon", "t": "Compensado × descompensado e a hipotensão por idade",
  "s": "<b>Compensado</b>: <b>taquicardia</b> (1º sinal), palidez, <b>extremidades frias</b>, <b>TEC &gt; 2 s</b>, <b>oligúria</b>, pulsos periféricos presentes (finos), <b>PA normal</b>. "
       "<br><b>Descompensado</b>: <b>hipotensão</b>, pulsos periféricos <b>ausentes</b>, <b>rebaixamento de consciência</b>. "
       "<br>TEC normal ≤ 2 s; diurese normal 1–2 mL/kg/h. "
       "<br><b>Hipotensão (PAS)</b> — único slide em quadro verde: <b>RN &lt; 60</b> · <b>1–12 meses &lt; 70</b> · <b>1–10 anos &lt; 70 + (2 × idade)</b> · <b>&gt; 10 anos &lt; 90</b> mmHg.",
  "fala": "Reconhecer o choque cedo é o objetivo da aula. No choque compensado a pressão ainda é normal, mas a criança tem taquicardia, palidez, extremidades frias, enchimento capilar lento e pouca urina. Descompensado é quando surge hipotensão, somem os pulsos periféricos ou a consciência cai. A hipotensão sistólica é abaixo de sessenta no recém-nascido, abaixo de setenta até um ano, setenta mais duas vezes a idade de um a dez anos, e abaixo de noventa acima de dez anos.",
  "div": "diurese",
  "pega": "Menino de <b>6 anos</b>: limite = 70 + 12 = <b>82</b>; PAS 80 = <b>hipotenso</b>. Hipotensão é sinal <b>tardio</b>.",
  "z": "Setenta mais duas vezes a idade. Seis anos, oitenta e dois. Abaixo disso a criança já gastou toda a compensação e está caindo do penhasco, porra.",
  "m": [["MEDCURSO · S30 P2 48:15–50:03", "Mesma fórmula da hipotensão: 70 + 2 × idade (1–10 anos)."]],
  "ills": ["s_recon"]},
 {"id": "s_hora1", "t": "A primeira hora: oxigênio, acesso e volume",
  "s": "Posição supina se hipotensa; <b>O₂ em alta concentração</b> (máscara não reinalante com reservatório; avaliar via aérea/VM). "
       "<br><b>Acesso venoso ou intraósseo</b> (se não conseguir veia rapidamente). "
       "<br><b>SF 0,9% ou RL 20 mL/kg em 5–20 min</b> (graves: até 10 min), <b>repetir</b> reavaliando; <b>hemorragia</b> (trauma): concentrado de hemácias 10 mL/kg; <b>cardiogênico</b>: <b>5–10 mL/kg em 10–20 min</b>. "
       "<br><b>Reavaliar após 40–60 mL/kg</b> (sinais de sobrecarga: estertores, hepatomegalia). Exames: hemograma, <b>glicemia</b>, gasometria, Ca, K, <b>lactato</b>. Antibiótico precoce na sepse (protocolo). <b>Nunca soro glicosado na expansão.</b>",
  "fala": "Na primeira hora: oxigênio em alta concentração com máscara e reservatório, acesso venoso e, se a veia não sai, intraósseo sem demora. A expansão é soro fisiológico ou Ringer, vinte mililitros por quilo em cinco a vinte minutos, repetida a cada reavaliação. No choque cardiogênico as alíquotas caem para cinco a dez mililitros por quilo. Depois de quarenta a sessenta mililitros por quilo, reavalie e pense em amina. Glicemia sempre, e nunca soro glicosado para expandir.",
  "div": "bolus",
  "pega": "16 kg → <b>320 mL</b> em 5–20 min. Duas veias falharam → <b>intraóssea</b>. Estertores + fígado crescendo após bolus = <b>cardiogênico</b>: 5–10 mL/kg + dobutamina.",
  "z": "Duas tentativas de veia e nada? Intraóssea, agora. Enquanto você caça veia, a criança perde a primeira hora, caralho.",
  "m": [["MEDCURSO · S30 P2 18:29–20:04", "Expansão é com cristaloide isotônico, nunca glicosado."]],
  "ills": ["s_hora1"]},
 {"id": "s_aminas", "t": "Aminas: frio, quente ou coração fraco",
  "s": "Choque que persiste após <b>40–60 mL/kg</b> → manter volume + <b>amina</b> (µg/kg/min): "
       "<br>• <b>Choque frio</b> (vasoconstrito, extremidades frias, pulsos finos): <b>adrenalina 0,05–1,5</b> (ou dopamina 2–20). "
       "<br>• <b>Choque quente</b> (vasodilatado, extremidades quentes, pulsos amplos, diastólica baixa): <b>noradrenalina 0,05–1,0</b>. "
       "<br>• <b>Insuficiência cardíaca</b>: <b>dobutamina 1–20</b> (inotrópico; pode baixar a PA). "
       "<br>Quente = queda da resistência vascular pelos mediadores da sepse, débito mantido ou alto.",
  "fala": "Se o choque persiste depois de quarenta a sessenta mililitros por quilo, mantém volume e começa amina, escolhida pelo tipo. Choque frio, com extremidades frias e pulsos finos, pede adrenalina. Choque quente, com extremidades quentes, pulsos amplos e diastólica baixa, é vasodilatação pelos mediadores da sepse e pede noradrenalina. E o coração que falha, na insuficiência cardíaca, pede dobutamina, que é inotrópico e pode baixar a pressão.",
  "div": "dopa",
  "pega": "Quente = <b>noradrenalina</b>; frio = <b>adrenalina</b>; IC = <b>dobutamina</b> (não usar dobutamina no quente hipotenso).",
  "z": "Extremidade quente e pressão no chão é vaso aberto demais: noradrenalina fecha a torneira. Dobutamina aí só abre mais, porra.",
  "ills": ["s_aminas"]},
 {"id": "s_obst", "t": "Choque obstrutivo e medidas finais",
  "s": "<b>Pneumotórax hipertensivo</b> (trauma, ventilação mecânica): ↓ murmúrio, <b>timpanismo</b>, desvio de traqueia, piora respiratória → <b>punção de tórax e drenagem</b>. "
       "<br><b>Tamponamento</b>: bulhas abafadas, turgência jugular, QRS de baixa voltagem → <b>punção pericárdica de alívio</b>. "
       "<br>Também: corrigir distúrbios metabólicos (glicose, cálcio, potássio, acidose), <b>UTI</b>; transporte só após estabilizar.",
  "fala": "Choque obstrutivo não melhora com volume nem com amina: precisa tirar a obstrução. No pneumotórax hipertensivo, típico do politrauma ou da ventilação mecânica, há murmúrio abolido e timpanismo de um lado, e a conduta é punção de tórax seguida de drenagem. No tamponamento, bulhas abafadas e jugulares túrgidas, a conduta é punção pericárdica de alívio. E sempre corrija glicose, cálcio e potássio, e leve para a terapia intensiva só depois de estabilizar.",
  "pega": "Intubado + timpanismo + murmúrio abolido + hipotensão = <b>punção de tórax</b> (não ecocardiograma, não mais volume).",
  "z": "Pneumotórax hipertensivo não se trata com o quarto bolus nem com noradrenalina: agulha no tórax, porra.",
  "ills": ["s_obst"]},
 {"id": "s_manut", "t": "Soro de manutenção: Holliday-Segar",
  "s": "<b>Volume/24 h</b>: <b>até 10 kg: 100 mL/kg</b> · <b>10–20 kg: 1000 + 50 mL/kg acima de 10</b> · <b>&gt; 20 kg: 1500 + 20 mL/kg acima de 20</b>. "
       "<br>Eletrólitos: <b>Na 3 mEq/kg/dia</b>, <b>K 2 mEq/kg/dia</b> (ou por 100 mL: Na 2–3, K 1–2). Ampolas: <b>NaCl 20% = 3,4 mEq/mL</b> · KCl 10% = 1,3 · <b>KCl 19,1% = 2,5 mEq/mL</b>. "
       "<br>Exemplo da aula: <b>30 kg</b> → 1500 + 200 = <b>1700 mL/dia</b> em 4 etapas de 425 mL (SG 5%) + eletrólitos → ~<b>72 mL/h</b>.",
  "fala": "Depois de estabilizar vem o soro de manutenção pela regra de Holliday-Segar. Até dez quilos, cem mililitros por quilo por dia. De dez a vinte quilos, mil mais cinquenta por cada quilo acima de dez. Acima de vinte, mil e quinhentos mais vinte por quilo acima de vinte. Some sódio três e potássio dois miliequivalentes por quilo por dia. O exemplo da aula é a criança de trinta quilos: mil e setecentos mililitros por dia, cerca de setenta e dois mililitros por hora.",
  "div": "eletro",
  "pega": "15 kg = 1000 + 50 × <b>5</b> = <b>1250 mL</b> (os 50 são só sobre os quilos <b>acima de 10</b>).",
  "z": "Quinze quilos não é mil setecentos e cinquenta: o cinquenta é só nos quilos acima de dez. Mil duzentos e cinquenta, caralho.",
  "ills": ["s_manut"]},
 {"id": "s_caso", "t": "O caso da aula: 10 anos, 30 kg",
  "s": "10 anos, 30 kg, febre há 5 dias e exantema, agora afebril e sonolenta: PA 80 (&lt; 90) = <b>choque descompensado</b> → <b>3 × 20 mL/kg</b> (600 mL cada) em 1 h. "
       "<br>Reavaliação: PA 90 × 60, mas <b>perfusão 4 s</b>, pulsos periféricos impalpáveis, sonolência = <b>ainda em choque</b>. "
       "<br>Após 60 mL/kg sem sobrecarga: <b>manter expansão + iniciar amina + exames</b> (slide 37–38: novo SF 20 mL/kg em 20 min). Só depois de estabilizar: <b>Holliday-Segar 1700 mL/dia</b>. "
       "<br>Confere com o grupo D da dengue (Cap. 6).",
  "fala": "O caso da aula junta tudo: uma criança de dez anos e trinta quilos, com febre de cinco dias e exantema, agora sem febre e sonolenta, com pressão de oitenta, abaixo de noventa, ou seja, choque descompensado. Recebe três bolus de vinte mililitros por quilo em uma hora. A pressão sobe para noventa, mas a perfusão segue em quatro segundos e os pulsos periféricos não voltam: ainda é choque. Então mantém volume, começa amina e pede exames; manutenção só depois.",
  "pega": "PA normalizou mas <b>TEC 4 s</b> e pulsos ausentes = <b>choque persistente</b> → amina; não é alta do choque.",
  "z": "Pressão de noventa com perfusão de quatro segundos é choque de maquiagem. Amina e reavaliação, porra.",
  "ills": ["s_caso"]},
]

ILLS = {
 "s_conc": flow("Choque: da oferta de O₂ ao lactato", [
     ("🩸", "Conteúdo de O₂", "hemoglobina × saturação (+ pO₂)", "v"),
     ("🫀", "Débito cardíaco", "frequência × volume sistólico", "r"),
     ("⚖️", "Oferta < necessidade", "falha de volume, bomba ou tônus", "a"),
     ("🧪", "Lactato", "extração esgotada → metabolismo anaeróbio", "p")],
     foot="PA = débito × resistência — pode estar normal no choque"),
 "s_tipos": cards("Os quatro tipos de choque", [
     ("💧", "Hipovolêmico", "desidratação, hemorragia, queimadura — o mais comum", "t"),
     ("🌡️", "Distributivo", "séptico, anafilático, neurogênico", "a"),
     ("🫀", "Cardiogênico", "miocardite, cardiopatia, arritmia", "r"),
     ("🚧", "Obstrutivo", "pneumotórax hipertensivo, tamponamento", "p")]),
 "s_recon": table("Reconhecer e classificar", [
     ("Compensado", "taquicardia · palidez · extremidades frias · TEC > 2 s · oligúria · PA normal"),
     ("Descompensado", "hipotensão · pulsos periféricos ausentes · consciência rebaixada"),
     ("PAS RN", "< 60 mmHg"), ("PAS 1–12 meses", "< 70 mmHg"),
     ("PAS 1–10 anos", "< 70 + (2 × idade)"), ("PAS > 10 anos", "< 90 mmHg"),
     ("Normal", "TEC ≤ 2 s · diurese 1–2 mL/kg/h")], cor="r", kw=180),
 "s_hora1": flow("A primeira hora", [
     ("😷", "O₂ alta concentração", "máscara não reinalante com reservatório · via aérea", "t"),
     ("💉", "Acesso venoso ou intraósseo", "IO se a veia não sai rápido", "p"),
     ("💧", "SF/RL 20 mL/kg em 5–20 min", "repetir reavaliando · cardiogênico 5–10 mL/kg · trauma: hemácias 10 mL/kg", "g"),
     ("🔁", "Reavaliar após 40–60 mL/kg", "sobrecarga? choque persiste → amina", "a"),
     ("🧪", "Exames", "hemograma, glicemia, gasometria, Ca, K, lactato", "v")],
     foot="Nunca soro glicosado na expansão"),
 "s_aminas": table("Amina pelo tipo de choque (µg/kg/min)", [
     ("Frio", "adrenalina 0,05–1,5 (ou dopamina 2–20)"),
     ("Quente", "noradrenalina 0,05–1,0"),
     ("Insuficiência cardíaca", "dobutamina 1–20 (pode baixar a PA)"),
     ("Quente, por quê", "vasodilatação por mediadores da sepse · pulsos amplos · diastólica baixa")], cor="r", kw=190),
 "s_obst": versus("Choque obstrutivo", ("🫁", "Pneumotórax hipertensivo", "t", [
     "• trauma / ventilação mecânica", "• murmúrio abolido, timpanismo", "• desvio de traqueia", "✔ punção de tórax + drenagem"]),
     ("🫀", "Tamponamento", "v", [
     "• bulhas abafadas", "• turgência jugular", "• QRS de baixa voltagem", "✔ punção pericárdica de alívio"]),
     foot="Volume e amina não resolvem obstrução"),
 "s_manut": table("Holliday-Segar (24 h)", [
     ("Até 10 kg", "100 mL/kg"), ("10–20 kg", "1000 + 50 mL/kg acima de 10 (15 kg = 1250)"),
     ("> 20 kg", "1500 + 20 mL/kg acima de 20 (30 kg = 1700)"),
     ("Eletrólitos", "Na 3 · K 2 mEq/kg/dia"),
     ("Ampolas", "NaCl 20% 3,4 · KCl 10% 1,3 · KCl 19,1% 2,5 mEq/mL"),
     ("30 kg", "4 etapas de 425 mL · ~72 mL/h")], cor="g", kw=150),
 "s_caso": flow("O caso da aula (30 kg)", [
     ("😴", "PA 80 < 90, sonolenta", "choque descompensado", "r"),
     ("💧", "3 × 20 mL/kg em 1 h", "600 mL cada bolus", "g"),
     ("🔍", "PA 90, TEC 4 s, sem pulso periférico", "ainda em choque", "a"),
     ("💊", "Manter volume + amina + exames", "novo SF 20 mL/kg em 20 min", "p"),
     ("🧴", "Depois de estável", "Holliday-Segar 1700 mL/dia", "t")]),
}

QMAP = {0: ["s_recon"], 1: ["s_recon"], 2: ["s_hora1"], 3: ["s_hora1", "s_aminas"], 4: ["s_aminas"], 5: ["s_obst"], 6: ["s_manut"], 7: ["s_caso"]}

DIV = {
 "diurese": ["Débito urinário normal e TEC", "Slide 13: diurese <b>1–2 mL/kg/h</b>; TEC “até 2 s”", "Slide 14: <b>1,5–2 mL/kg/h</b>; TEC “menor que 2 s”",
             "Divergência interna: escreva “diurese ≥ 1 mL/kg/h e TEC ≤ 2 s”"],
 "bolus": ["Tempo do bolus nos graves", "Slide 21: graves em <b>até 10 min</b>", "Caso dos slides 34/38: 20 mL/kg em <b>20 minutos</b>",
           "Escreva “20 mL/kg em 5–20 min (graves: até 10 min)”"],
 "dopa": ["Dopamina no choque frio", "Slides 25/38: dopamina como opção no choque frio",
          "Surviving Sepsis pediátrica 2020: <b>adrenalina ou noradrenalina</b> preferidas; dopamina perdeu espaço", "Faculdade: o slide; residência: adrenalina"],
 "eletro": ["Cálculo dos eletrólitos da manutenção", "Slide 27: por kg (Na 3, K 2 mEq/kg/dia) → 30 kg: Na 60 / K 35",
            "Slides 28–29/40: por 100 mL (modificado) → 30 kg: Na 51 / K 34", "Dois métodos válidos: diga qual usou"],
}

FLASH = [
 [10, "Choque é definido por?", "Oferta de O₂ < necessidade (não por PA)."],
 [10, "Tipos de choque mais comuns na criança?", "Hipovolêmico e séptico."],
 [10, "Primeiro sinal de choque compensado?", "Taquicardia."],
 [10, "Compensado × descompensado?", "Descompensado: hipotensão, pulsos periféricos ausentes, consciência rebaixada."],
 [10, "Hipotensão RN / 1–12 m / 1–10 a / > 10 a?", "< 60 / < 70 / < 70 + 2 × idade / < 90."],
 [10, "Limite de PAS aos 6 anos?", "82 mmHg."],
 [10, "Bolus de expansão?", "SF/RL 20 mL/kg em 5–20 min, repetir."],
 [10, "Bolus no cardiogênico?", "5–10 mL/kg em 10–20 min."],
 [10, "Sem veia?", "Intraóssea."],
 [10, "Quando pensar em amina?", "Choque persistente após 40–60 mL/kg."],
 [10, "Choque quente: amina?", "Noradrenalina 0,05–1,0 µg/kg/min."],
 [10, "Choque frio: amina?", "Adrenalina 0,05–1,5 (ou dopamina)."],
 [10, "Insuficiência cardíaca: amina?", "Dobutamina 1–20."],
 [10, "Pneumotórax hipertensivo?", "Punção de tórax + drenagem."],
 [10, "Holliday-Segar 15 kg?", "1250 mL/dia."],
 [10, "Holliday-Segar 30 kg?", "1700 mL/dia (~72 mL/h)."],
 [10, "Eletrólitos da manutenção?", "Na 3, K 2 mEq/kg/dia."],
]

COLA = [["Cap. 10 · Choque", [
 ["Hipotensão", "RN < 60 · 1–12 m < 70 · 1–10 a < 70 + 2×id · > 10 a < 90"], ["Normal", "TEC ≤ 2 s · diurese 1–2 mL/kg/h"],
 ["Bolus", "20 mL/kg em 5–20 min · repetir"], ["Cardiogênico", "5–10 mL/kg em 10–20 min"], ["Trauma", "hemácias 10 mL/kg"],
 ["Reavaliar", "40–60 mL/kg → amina"], ["Frio", "adrenalina 0,05–1,5"], ["Quente", "noradrenalina 0,05–1,0"], ["IC", "dobutamina 1–20"],
 ["Pneumotórax", "punção + drenagem"], ["Holliday", "100 · 1000+50 · 1500+20"], ["Eletrólitos", "Na 3 · K 2 mEq/kg/dia"],
 ["Ampolas", "NaCl 20% 3,4 · KCl 19,1% 2,5 mEq/mL"]]]]

KS = [
 {"id": "k_s_sep", "cap": 10, "blk": ["s_recon", "s_hora1", "s_aminas"], "t": "Lactente toxemiado com impetigo (prova antiga, 1,3 pt)",
  "src": "Prova A1 (3 pts) · Q2 média taxonomia — Profa. Patrícia",
  "enun": "Lactente de 1 ano, <b>10 kg</b>, tosse e febre há 1 semana com piora e dificuldade respiratória. Prostrado, sonolento, toxemiado, febre 39,5 °C. <b>Extremidades quentes</b>, FC 154, <b>pulsos periféricos não palpáveis</b>, centrais diminuídos, <b>PA 60 × 40</b>, perfusão 4 s. MV diminuído com estertores bilaterais, FR 60, tiragem. <b>Impetigo em membros inferiores.</b>",
  "p": [{"p": "Classifique o choque, a origem e o provável agente.",
         "m": "<b>Choque séptico (distributivo), descompensado</b> — hipotensão (PA 60 &lt; 70 + 2 × 1 = 72), pulsos periféricos ausentes, rebaixamento de consciência. Origem: <b>pneumonia</b> a partir de <b>impetigo</b> → <b><i>Staphylococcus aureus</i></b>.",
         "c": ["séptico", "distributivo", "descompensado", "72", "pneumonia", "impetigo", "Staphylococcus aureus"]},
        {"p": "Descreva o atendimento na primeira hora (10 kg).",
         "m": "O₂ em alta concentração (máscara não reinalante com reservatório; avaliar VM) · acesso venoso ou <b>intraósseo</b> · <b>SF/Ringer 20 mL/kg = 200 mL em 5–20 min</b> (grave: até 10 min), repetir reavaliando · após <b>40–60 mL/kg</b> sem resposta → <b>amina</b>: choque quente = <b>noradrenalina 0,05–1,0 µg/kg/min</b> · exames: hemograma, glicemia, gasometria, Ca, K, lactato · antibiótico precoce · UTI.",
         "c": ["oxigênio", "intraósseo", "20 mL/kg", "200 mL", "40 a 60 mL/kg", "noradrenalina", "lactato", "antibiótico"]},
        {"p": "Explique as extremidades quentes.",
         "m": "<b>Choque quente</b>: predomina a <b>vasodilatação</b> (queda da resistência vascular pelos mediadores da sepse), com débito mantido ou alto — pele quente, pulsos amplos no início. O problema é o tônus, por isso a droga é a noradrenalina.",
         "c": ["choque quente", "vasodilatação", "resistência vascular", "mediadores da sepse", "noradrenalina"]}]},
 {"id": "k_s_caso", "cap": 10, "blk": ["s_caso", "s_manut", "s_recon"], "t": "O caso da aula: 30 kg, febre e exantema",
  "src": "Caso dos slides 32–40 da professora",
  "enun": "Criança de 10 anos, 30 kg, febre há 5 dias e exantema, agora afebril e sonolenta. FC 140, PA 80 × 50, pulsos periféricos finos, perfusão 5 s.",
  "p": [{"p": "Classifique e diga a conduta inicial com volumes.",
         "m": "&gt; 10 anos: hipotensão = PAS &lt; 90 → <b>choque descompensado</b>. O₂, acesso, <b>SF 20 mL/kg = 600 mL</b> em 5–20 min, repetir até <b>3 vezes</b> (60 mL/kg) reavaliando.",
         "c": ["descompensado", "90", "20 mL/kg", "600 mL", "3 vezes", "reavaliar"]},
        {"p": "Após 3 bolus: PA 90 × 60, perfusão 4 s, pulsos periféricos impalpáveis, pulmões limpos. Conduta?",
         "m": "<b>Choque persistente</b> (perfusão e pulsos): <b>manter expansão</b> (novo 20 mL/kg em 20 min), <b>iniciar amina</b> conforme o perfil (frio → adrenalina) e <b>solicitar exames</b>; UTI.",
         "c": ["choque persistente", "manter expansão", "amina", "exames", "UTI"]},
        {"p": "Estabilizada, prescreva a manutenção de 24 h.",
         "m": "<b>Holliday-Segar</b>: 1500 + 20 × 10 = <b>1700 mL/dia</b> de SG 5% em 4 etapas de 425 mL, com <b>Na 3</b> e <b>K 2 mEq/kg/dia</b> (NaCl 20% 3,4 mEq/mL; KCl 19,1% 2,5 mEq/mL) → ~<b>72 mL/h</b>.",
         "c": ["Holliday-Segar", "1700 mL", "4 etapas", "sódio", "potássio", "72 mL/h"]}]},
]
