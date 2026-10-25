"""EXEMPLO REAL (Trilha de Obstetrícia, bloco "Os 4 períodos do parto").
Este arquivo NÃO entra no build (o nome começa com _exemplo). Use como régua de qualidade:
cada bloco novo deve ter este nível — slide, fala narrável, fala do professor com timestamp,
cursinho recolhido, pegadinha, divergência resolvida, zoeira amarrada a uma decisão e um esquema próprio."""

CAPS = [{'n': 5,
  't': 'Assistência ao parto',
  'short': 'Parto',
  'aula': 'Aulas 6 e 7 · slides Caliman',
  'grav': 7,
  'icon': '🤱',
  'col': '#A2452F',
  'bul': ['4 períodos: dilatação · expulsivo · dequitação · 4º (1ª hora)',
          'Fase ativa: 2–3 contrações/10 min + dilatação',
          'BCF 30/30 min; 5/5 min no expulsivo',
          'Manejo ativo: ocitocina IM + clampeamento + tração'],
  'medalha': ['🤱', 'Globo de Pinard']}]

BLOCKS = [{'id': 'e_def',
  'ord': 1,
  't': 'Parto: definição e os 4 períodos clínicos',
  'slides': ['E3', 'E4', 'F2'],
  'ill': 'periodos',
  's': 'Parto = expulsão dos produtos da concepção do útero e da vagina para o meio externo, <b>a partir de '
       '<span class=n>20 semanas</span></b> (anotação: “20–22, não é exato”). Antes disso é '
       '<b>abortamento</b>.\n'
       '<br>4 fases: <b>1º dilatação</b> (abertura do colo) · <b>2º expulsão</b> (do feto) · <b>3º '
       'secundamento</b> (saída da placenta) · <b>4º quarto período</b> (hemostasia): <b>a 1ª hora '
       'pós-parto</b> para o Túlio; o slide diz <b>até 2 h</b> (Greenberg).',
  'a': 'Anotação: aborto = interrupção da gravidez; abortamento = o processo de expulsão.',
  'm': [['OBS2 · Assistência 00:13:05',
         '4º período = do secundamento até <b>1 hora</b> (“período de ouro”) — no slide: <b>até 2 h</b>.']],
  'div': 'quarto',
  'fala': 'Parto é a expulsão do concepto a partir de vinte semanas; antes disso é abortamento. São quatro '
          'períodos: dilatação, expulsão, secundamento, que é a saída da placenta, e o quarto período, a '
          'hemostasia, que o Túlio define como a primeira hora após o parto; o slide estende até duas horas.',
  'pega': 'Viabilidade: <b>20 sem</b> (slide). 4º período: <b>1ª hora</b> (Túlio e MEDCURSO); o slide diz '
          'até 2 h. Na prova, escreva 1ª hora e cite o slide.',
  'cap': 5,
  'hot': ['q_a2'],
  'g': [{'a': 7,
         'an': 'Assistência ao parto',
         'ts': '00:00:00',
         't': 'Parto = expulsão do concepto <b>após 20 sem</b>; antes = abortamento. Ideal ≥ 37 sem.',
         'e': False}],
  'z': 'Antes de vinte semanas é abortamento; depois é parto. E o quarto período, pro Túlio, é a primeira '
       'hora: a hora de ouro em que a mulher pode sangrar até morrer se ninguém olhar o útero.',
  'ills': ['periodos']}]

Q = [{'id': 'q_a2',
  'cap': 5,
  'src': 'prof',
  'orig': 'Questão comentada na aula · grav. 7 (39:32)',
  'tag': ' · 39:32',
  'enun': '38 sem, sem complicações, em TP sem analgesia, com puxos. AU 34, dilatação total, bolsa rota, OP, '
          'plano +4 de DeLee. Em que período ela está?',
  'alts': ['Primeiro', 'Segundo (expulsivo)', 'Terceiro', 'Quarto'],
  'ok': 1,
  'coment': 'Dilatação total (10 cm) até a saída do bebê = <b>2º período</b>. “Tenho que saber primeiro, '
            'segundo, terceiro, quarto e qual é cada um.”',
  'blk': ['e_expul', 'e_def'],
  'slides': ['F3', 'E4'],
  'pct': None}]

KS = [{'id': 'k_diag1',
  'cap': 1,
  'blk': ['d_presuncao', 'd_prob', 'p_ig'],
  't': 'O caso da SMF (o caso da própria aula)',
  'enun': 'SMF, 32 anos, G3, procura a UBS em <b>12/02</b> por atraso menstrual. <b>DUM 04/12</b>, ciclos '
          'sempre regulares. Refere mamas doloridas e aumentadas, enjoo, constipação e polaciúria. Ao exame: '
          'hipertrofia das glândulas sebáceas da aréola, aréola secundária bem desenvolvida, arroxeamento da '
          'mucosa vulvar e vaginal, amolecimento do istmo e útero aumentado e abaulado à esquerda. O BCF não '
          'foi audível ao sonar.',
  'p': [{'p': 'Calcule a idade gestacional e a data provável do parto, mostrando a conta.',
         'm': 'Calendário: 04/12→31/12 = 27 dias + janeiro 31 + fevereiro 12 = <b>70 dias ÷ 7 = 10 '
              'semanas</b>. Näegele: dia + 7 = 11; mês − 3 (ou + 9) = setembro → <b>DPP 11/09</b> do ano '
              'seguinte.',
         'c': ['70 dias',
               'dividir por 7',
               '10 semanas',
               'Näegele',
               '+7 dias',
               '−3 meses ou +9 meses',
               'DPP 11/09']},
        {'p': 'Liste os sinais e sintomas de presunção e os de probabilidade presentes, com os epônimos.',
         'm': '<b>Presunção</b> (o que ela sente / alterações gerais): atraso menstrual, náusea, mastalgia e '
              'mamas congestas, polaciúria, constipação; nas mamas, <b>tubérculos de Montgomery</b> e '
              '<b>sinal de Hunter</b> (aréola secundária) — o Túlio ensinou as mamárias como presunção. '
              '<b>Probabilidade</b> (perto do bebê): <b>Hegar</b> (amolecimento do istmo), <b>Piskacek</b> '
              '(útero assimétrico, abaulado à esquerda), <b>Jacquemier</b> (vulva arroxeada), <b>Kluge</b> '
              '(vagina arroxeada), útero aumentado.',
         'c': ['atraso menstrual',
               'náusea',
               'mastalgia',
               'Montgomery',
               'Hunter',
               'Hegar = istmo',
               'Piskacek = assimetria',
               'Jacquemier = vulva',
               'Kluge = vagina']},
        {'p': 'Por que o BCF não foi ouvido? Como você confirma a gravidez agora?',
         'm': 'Com 10 semanas ainda não se ouve com o sonar — o <b>sonar detecta a partir de 12 semanas</b> '
              '(Pinard 18). Confirmar com <b>β-hCG quantitativo</b> e <b>USG transvaginal</b> (saco 4 · '
              'vesícula 5 · embrião 6 · BCF 6–7 sem), que também data a gestação (CCN; regra dos 7 dias).',
         'c': ['sonar a partir de 12 semanas',
               'β-hCG quantitativo',
               'USG transvaginal',
               'embrião/BCF visível ao USG',
               'regra dos 7 dias ou CCN']}],
  'src': 'Caso apresentado pelo Túlio no início da aula de diagnóstico (grav. 2, 02:23)'}]

DIV = {'quarto': ['Duração do 4º período',
            'Slide F24–F25 (Caliman): <b>até 2 h após o parto</b> (Greenberg)',
            '<b>Túlio na aula (grav. 7, 26:55)</b> e MEDCURSO: <b>a primeira hora pós-parto</b>',
            'Responda <b>1ª hora</b> (fala do Túlio); se a alternativa for “até 2 h”, ela também tem '
            'respaldo no slide']}

SAY = [['Os 4 períodos do parto',
  'tenho que saber primeiro, segundo, terceiro, quarto e qual é cada um',
  7,
  '00:39:32',
  'e_def']]

NOSAY = [['Distócias do partograma',
  'fase ativa prolongada, paradas secundárias… “podem deixar para o próximo semestre”',
  7,
  '00:37:24']]

FLASH = [[5, 'Parto a partir de quantas semanas (slide)?', '20 semanas (antes = abortamento).'],
 [5, 'Diagnóstico de TP?', '2 contrações dolorosas/10 min, 30–35 s, + dilatação progressiva.']]

COLA = [['Modificações maternas',
  [['Volume sanguíneo', '↑ 50% (plasma 40–50%, hemácias 20–30%)'],
   ['Débito cardíaco', '↑ 40–50% · FC ↑ 10 bpm'],
   ['RVP / PA', '↓ / ↓ (mínimo no 2º tri)'],
   ['Hb normal', '≥ 11 g/dL'],
   ['Leucócitos', 'até 15.000/mm³'],
   ['TEV', '4–5× gestação · 20× puerpério'],
   ['HCO₃', '26 → 22 mmol/L'],
   ['Diafragma', 'sobe 4 cm'],
   ['TFG', '↑ 50% · Cr 0,5–0,9'],
   ['Glicemia de jejum', '< 92 normal'],
   ['Útero', '70 g → 1.100 g · 10 mL → 5 L'],
   ['Sínfise', 'mobilidade até 1,2 cm'],
   ['pH vaginal', '3,5–6']]]]

MISSIONS = [{'id': 'm1', 'nm': '🔍 Diagnóstico completo', 'dl': '2026-10-01T23:35:00-03:00', 'tipo': 'cap', 'cap': 1},
 {'id': 'm3',
  'nm': '🩺 Pré-natal · blocos 1–10',
  'dl': '2026-10-02T00:50:00-03:00',
  'tipo': 'faixa',
  'cap': 3,
  'de': 1,
  'ate': 10},
 {'id': 'm7', 'nm': '📝 Todas as questões', 'dl': '2026-10-02T02:45:00-03:00', 'tipo': 'questoes'},
 {'id': 'mk', 'nm': '✍️ 1 caso por capítulo', 'dl': '2026-10-02T02:45:00-03:00', 'tipo': 'casos'},
 {'id': 'ms', 'nm': '⏱️ Um simulado', 'dl': '2026-10-02T03:00:00-03:00', 'tipo': 'prova'},
 {'id': 'm8', 'nm': '⚡ Pegadinhas + ≠', 'dl': '2026-10-02T03:00:00-03:00', 'tipo': 'vesp'}]

MEDALS_EXTRA = [{'id': 'toxo',
  'ic': '🐈',
  'nm': 'Gato escaldado',
  'ds': 'Acertar todas de toxoplasmose',
  'qs': ['q_p76', 'q_p78', 'q_p79', 'q_p80', 'q_e9']}]

GORILA_FALAS = ['Mamas são presunção. Já falei. Vou falar de novo.', 'Primeira hora pós-parto. Quarto período. Grava.']

ILLS = {'periodos': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 334" font-family="Carlito,Segoe '
             'UI,Arial,sans-serif" role="img" aria-label="Os 4 períodos clínicos do parto"><rect width="640" '
             'height="334" rx="14" fill="#FBF9F6"/><text x="320" y="30" text-anchor="middle" font-size="18" '
             'font-weight="700" fill="#262223">Os 4 períodos clínicos do parto</text><rect x="30" y="48" '
             'width="580" height="48" rx="10" fill="#fff" stroke="#1E5E6E" stroke-width="1.8"/><circle '
             'cx="58" cy="72" r="18" fill="#E5F0F3" stroke="#1E5E6E" stroke-width="1.6"/><text x="58" y="79" '
             'font-size="19" text-anchor="middle">⭕</text><circle cx="42" cy="57" r="7.5" '
             'fill="#1E5E6E"/><text x="42" y="60.5" font-size="9.5" fill="#fff" text-anchor="middle" '
             'font-weight="700">1</text><text x="86" y="68" font-size="13.5" font-weight="700" '
             'fill="#262223">1º Dilatação</text><text x="86" y="86" font-size="11.5" fill="#5A5250">TP (2 '
             'contr/10 min + dilatação) → 10 cm · ativa &gt; 5 cm · BCF 30/30 · toque 2/2 h</text><path '
             'd="M56 96V106" stroke="#1E5E6E" stroke-width="2"/><rect x="30" y="106" width="580" height="48" '
             'rx="10" fill="#fff" stroke="#7A2E4A" stroke-width="1.8"/><circle cx="58" cy="130" r="18" '
             'fill="#F6EAF0" stroke="#7A2E4A" stroke-width="1.6"/><text x="58" y="137" font-size="19" '
             'text-anchor="middle">👶</text><circle cx="42" cy="115" r="7.5" fill="#7A2E4A"/><text x="42" '
             'y="118.5" font-size="9.5" fill="#fff" text-anchor="middle" font-weight="700">2</text><text '
             'x="86" y="126" font-size="13.5" font-weight="700" fill="#262223">2º Expulsão</text><text '
             'x="86" y="144" font-size="11.5" fill="#5A5250">10 cm → saída do feto · puxos (Ferguson) · 5 '
             'contr/10 min · BCF 5/5 · até 2 h (primi)</text><path d="M56 154V164" stroke="#7A2E4A" '
             'stroke-width="2"/><rect x="30" y="164" width="580" height="48" rx="10" fill="#fff" '
             'stroke="#B07D3A" stroke-width="1.8"/><circle cx="58" cy="188" r="18" fill="#FBF2E2" '
             'stroke="#B07D3A" stroke-width="1.6"/><text x="58" y="195" font-size="19" '
             'text-anchor="middle">🥩</text><circle cx="42" cy="173" r="7.5" fill="#B07D3A"/><text x="42" '
             'y="176.5" font-size="9.5" fill="#fff" text-anchor="middle" font-weight="700">3</text><text '
             'x="86" y="184" font-size="13.5" font-weight="700" fill="#262223">3º Secundamento</text><text '
             'x="86" y="202" font-size="11.5" fill="#5A5250">descolamento → descida → expulsão da placenta · '
             'Jacob-Dublin · ocitocina 10 UI IM</text><path d="M56 212V222" stroke="#B07D3A" '
             'stroke-width="2"/><rect x="30" y="222" width="580" height="48" rx="10" fill="#fff" '
             'stroke="#2E6B4F" stroke-width="1.8"/><circle cx="58" cy="246" r="18" fill="#E7F2EC" '
             'stroke="#2E6B4F" stroke-width="1.6"/><text x="58" y="253" font-size="19" '
             'text-anchor="middle">🛡️</text><circle cx="42" cy="231" r="7.5" fill="#2E6B4F"/><text x="42" '
             'y="234.5" font-size="9.5" fill="#fff" text-anchor="middle" font-weight="700">4</text><text '
             'x="86" y="242" font-size="13.5" font-weight="700" fill="#262223">4º Quarto período</text><text '
             'x="86" y="260" font-size="11.5" fill="#5A5250">1ª hora pós-parto (Túlio; slide: até 2 h) · '
             'miotamponagem · globo de Pinard</text><rect x="30" y="284" width="580" height="36" rx="10" '
             'fill="#FBEDE8" stroke="#e8c9bd"/><text x="320" y="307" font-size="12.5" fill="#B5402F" '
             'text-anchor="middle" font-weight="700">risco do 4º período: atonia e hemorragia</text></svg>'}
