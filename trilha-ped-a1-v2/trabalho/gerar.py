#!/usr/bin/env python3
"""Monta dados/conteudo.json a partir de trabalho/capNN.py + extras.py.

Cada capNN.py define CAP, BLOCKS, ILLS, QMAP (índice da questão da Trilha 1.0 → blocos),
e opcionalmente DIV, FLASH, COLA, KS, Q. As questões da 1.0 vêm de fontes/outros/trilha_ped_a1_v1.json.
Uso: python3 trabalho/gerar.py   (depois: build.py da skill)
"""
import glob, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'trabalho'))
import svg

V1 = {c['n']: c for c in json.load(open(os.path.join(ROOT, 'fontes/outros/trilha_ped_a1_v1.json'), encoding='utf-8'))}
OUT = {k: [] for k in ('CAPS', 'BLOCKS', 'Q', 'KS', 'FLASH', 'COLA', 'SAY', 'NOSAY', 'MISSIONS', 'MEDALS_EXTRA', 'GORILA_FALAS')}
OUT.update(DIV={}, ILLS={})

def slides_of(html):
    return []  # sem PDFs nesta versão: as referências "Sl. N" ficam no texto

def v1_questions(n, qmap):
    qs = []
    for i, q in enumerate(V1[n]['qs']):
        if i not in qmap: sys.exit(f'cap {n}: questão {i} da 1.0 sem bloco em QMAP')
        enun = q['stem']
        coment = re.sub(r'<span class="ct">(.*?)</span>', r' <i>(\1)</i>', q['why'])
        qs.append({'id': f'q{n:02d}_{i + 1}', 'cap': n, 'src': 'autoral', 'orig': 'Trilha 1.0 · ' + q['h'],
                   'tag': q['h'].split('·')[-1].strip(), 'enun': enun, 'alts': q['alts'], 'ok': q['ok'],
                   'coment': coment, 'blk': qmap[i]})
    return qs

for f in sorted(glob.glob(os.path.join(ROOT, 'trabalho', 'cap*.py'))) + [os.path.join(ROOT, 'trabalho', 'extras.py')]:
    if not os.path.exists(f): continue
    ns = {k: getattr(svg, k) for k in ('cards', 'flow', 'versus', 'table')}
    exec(compile(open(f, encoding='utf-8').read(), f, 'exec'), ns)
    if 'CAP' in ns:
        n = ns['CAP']['n']; OUT['CAPS'].append(ns['CAP'])
        for i, b in enumerate(ns['BLOCKS']):
            b['cap'] = n; b.setdefault('ord', i + 1)
        OUT['BLOCKS'] += ns['BLOCKS']
        OUT['Q'] += v1_questions(n, ns['QMAP'])
    for k in ('Q', 'KS', 'FLASH', 'COLA', 'SAY', 'NOSAY', 'MISSIONS', 'MEDALS_EXTRA', 'GORILA_FALAS'):
        if k in ns: OUT[k] += ns[k]
    for k in ('DIV', 'ILLS'):
        if k in ns:
            dup = set(OUT[k]) & set(ns[k])
            if dup: sys.exit(f'{os.path.basename(f)}: chave repetida em {k}: {dup}')
            OUT[k].update(ns[k])

OUT['CAPS'].sort(key=lambda c: c['n'])
json.dump(OUT, open(os.path.join(ROOT, 'dados', 'conteudo.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('✔ dados/conteudo.json:', {k: len(v) for k, v in OUT.items()})
