"""Gerador dos esquemas (ILLS) da trilha — paleta e regras de references/esquemas.md.

Quatro formatos: cards (grade de cartões), flow (sequência numerada / fluxo de conduta),
versus (A × B lado a lado) e table (tabela-desenho de números). Texto ≥ 13 px na escala 640.
"""
import html

COR = {  # traço, fundo claro
    't': ('#1E5E6E', '#E5F0F3'), 'v': ('#7A2E4A', '#F6EAF0'), 'g': ('#2E6B4F', '#E7F2EC'),
    'a': ('#B07D3A', '#FBF2E2'), 'r': ('#B5402F', '#FBEDE8'), 'p': ('#5B3F8C', '#EFEAF7'),
}
INK, INK2, BG = '#262223', '#5A5250', '#FBF9F6'
FONT = 'Carlito,Segoe UI,Arial,sans-serif'


def e(s):
    return html.escape(str(s), quote=True)


def wrap(text, n):
    out, cur = [], ''
    for w in str(text).split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur); cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur: out.append(cur)
    return out or ['']


def _open(title, h):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 {h}" font-family="{FONT}" role="img" '
            f'aria-label="{e(title)}"><rect width="640" height="{h}" rx="14" fill="{BG}"/>'
            f'<text x="320" y="32" text-anchor="middle" font-size="19" font-weight="700" fill="{INK}">{e(title)}</text>')


def _foot(text, y, cor='r'):
    st, bg = COR[cor]
    ls = wrap(text, 78)
    h = 14 + 19 * len(ls)
    s = f'<rect x="24" y="{y}" width="592" height="{h}" rx="10" fill="{bg}" stroke="{st}" stroke-opacity=".35"/>'
    for i, l in enumerate(ls):
        s += f'<text x="320" y="{y + 22 + 19 * i}" text-anchor="middle" font-size="14" font-weight="700" fill="{st}">{e(l)}</text>'
    return s, h


def cards(title, items, cols=2, foot=None, fcor='r'):
    """items: [(emoji, título, texto, cor)]"""
    gap, x0 = 12, 24
    w = (592 - gap * (cols - 1)) / cols
    nch = int((w - 24) / 7.0)
    rows = [items[i:i + cols] for i in range(0, len(items), cols)]
    y = 52; body = ''
    for row in rows:
        hs = []
        for em, hd, tx, c in row:
            hl = wrap(hd, int((w - 70) / 8.2)); tl = wrap(tx, nch)
            hs.append(max(27 + 18 * len(hl) + 12, 68) + 18 * (len(tl) - 1) + 16)
        rh = max(hs)
        for j, (em, hd, tx, c) in enumerate(row):
            st, bg = COR[c]; x = x0 + j * (w + gap)
            body += f'<rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="{rh}" rx="12" fill="#fff" stroke="{st}" stroke-width="1.8"/>'
            body += f'<circle cx="{x + 30:.0f}" cy="{y + 30}" r="20" fill="{bg}" stroke="{st}" stroke-width="1.5"/>'
            body += f'<text x="{x + 30:.0f}" y="{y + 37}" text-anchor="middle" font-size="19">{e(em)}</text>'
            hl = wrap(hd, int((w - 70) / 8.2))
            for k, l in enumerate(hl):
                body += f'<text x="{x + 58:.0f}" y="{y + 27 + 18 * k}" font-size="15.5" font-weight="700" fill="{st}">{e(l)}</text>'
            ty = y + max(27 + 18 * len(hl) + 12, 68)
            for k, l in enumerate(wrap(tx, nch)):
                body += f'<text x="{x + 14:.0f}" y="{ty + 18 * k}" font-size="13.5" fill="{INK2}">{e(l)}</text>'
        y += rh + gap
    if foot:
        f, fh = _foot(foot, y, fcor); body += f; y += fh + gap
    h = y + 8
    return _open(title, h) + body + '</svg>'


def flow(title, steps, foot=None, fcor='r'):
    """steps: [(emoji, título, texto, cor)] — sequência numerada com setas."""
    y = 50; body = ''
    for i, (em, hd, tx, c) in enumerate(steps):
        st, bg = COR[c]
        tl = wrap(tx, 70)
        h = 34 + 18 * len(tl)
        body += f'<rect x="24" y="{y}" width="592" height="{h}" rx="10" fill="#fff" stroke="{st}" stroke-width="1.8"/>'
        cy = y + h / 2
        body += f'<circle cx="56" cy="{cy:.0f}" r="19" fill="{bg}" stroke="{st}" stroke-width="1.5"/>'
        body += f'<text x="56" y="{cy + 7:.0f}" text-anchor="middle" font-size="19">{e(em)}</text>'
        body += f'<circle cx="40" cy="{y + 9}" r="9" fill="{st}"/><text x="40" y="{y + 13.5}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{i + 1}</text>'
        body += f'<text x="88" y="{y + 23}" font-size="15.5" font-weight="700" fill="{INK}">{e(hd)}</text>'
        for k, l in enumerate(tl):
            body += f'<text x="88" y="{y + 42 + 18 * k}" font-size="13.5" fill="{INK2}">{e(l)}</text>'
        y += h
        if i < len(steps) - 1:
            body += f'<path d="M56 {y} V{y + 12}" stroke="{st}" stroke-width="2.2"/><path d="M50 {y + 6} L56 {y + 13} L62 {y + 6}" fill="none" stroke="{st}" stroke-width="2.2"/>'
            y += 14
    y += 12
    if foot:
        f, fh = _foot(foot, y, fcor); body += f; y += fh + 12
    return _open(title, y + 4) + body + '</svg>'


def versus(title, left, right, foot=None, fcor='r'):
    """left/right: (emoji, título, cor, [linhas]) — linhas começando com '✔'/'✘'/'•' ou livres."""
    body = ''; y0 = 52; w = 290
    hs = []
    for side in (left, right):
        n = sum(len(wrap(l, 36)) for l in side[3])
        hs.append(64 + 19 * n + 10)
    h = max(hs)
    for j, (em, hd, c, ls) in enumerate((left, right)):
        st, bg = COR[c]; x = 24 + j * (w + 12)
        body += f'<rect x="{x}" y="{y0}" width="{w}" height="{h}" rx="12" fill="#fff" stroke="{st}" stroke-width="1.8"/>'
        body += f'<rect x="{x}" y="{y0}" width="{w}" height="44" rx="12" fill="{bg}"/><rect x="{x}" y="{y0 + 30}" width="{w}" height="14" fill="{bg}"/>'
        body += f'<text x="{x + 26}" y="{y0 + 29}" text-anchor="middle" font-size="19">{e(em)}</text>'
        body += f'<text x="{x + 48}" y="{y0 + 28}" font-size="16" font-weight="700" fill="{st}">{e(hd)}</text>'
        yy = y0 + 66
        for l in ls:
            for k, part in enumerate(wrap(l, 36)):
                body += f'<text x="{x + 14 + (12 if k else 0)}" y="{yy}" font-size="13.5" fill="{INK if k == 0 else INK2}">{e(part)}</text>'
                yy += 19
    y = y0 + h + 12
    body += f'<circle cx="320" cy="{y0 + h / 2:.0f}" r="15" fill="{BG}" stroke="#d9d2c7"/><text x="320" y="{y0 + h / 2 + 5:.0f}" text-anchor="middle" font-size="14" font-weight="700" fill="{INK2}">×</text>'
    if foot:
        f, fh = _foot(foot, y, fcor); body += f; y += fh + 12
    return _open(title, y + 4) + body + '</svg>'


def table(title, rows, cor='t', foot=None, fcor='r', kw=230):
    """rows: [(chave, valor)] — tabela-desenho de números e condutas."""
    st, bg = COR[cor]; y = 52; body = ''
    vw = int((592 - kw - 24) / 7.1)
    for i, (k, v) in enumerate(rows):
        kl = wrap(k, int((kw - 20) / 7.6)); vl = wrap(v, vw)
        h = 16 + 18 * max(len(kl), len(vl))
        body += f'<rect x="24" y="{y}" width="592" height="{h}" rx="8" fill="{bg if i % 2 == 0 else "#fff"}" stroke="{st}" stroke-opacity=".35"/>'
        for n, l in enumerate(kl):
            body += f'<text x="36" y="{y + 22 + 18 * n}" font-size="14" font-weight="700" fill="{st}">{e(l)}</text>'
        for n, l in enumerate(vl):
            body += f'<text x="{24 + kw + 12}" y="{y + 22 + 18 * n}" font-size="14" fill="{INK}">{e(l)}</text>'
        y += h + 4
    y += 8
    if foot:
        f, fh = _foot(foot, y, fcor); body += f; y += fh + 12
    return _open(title, y + 4) + body + '</svg>'
