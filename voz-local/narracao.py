"""Prepara textos para o app de voz: frases curtas e tudo escrito como deve ser falado.

    python narracao.py entrada.json lote.txt

entrada.json é {"nome": "texto", ...}. Cada nome vira um arquivo nome.mp3 no modo Lote do app.
O lote sai assim (é o que se cola no app):

    ## 01
    Bom dia a todos.
    Nosso tema é o sangramento uterino anormal.
"""
import json
import re
import sys

UN = "zero um dois três quatro cinco seis sete oito nove dez onze doze treze catorze quinze dezesseis dezessete dezoito dezenove".split()
DEZ = "_ _ vinte trinta quarenta cinquenta sessenta setenta oitenta noventa".split()
CEM = "_ cento duzentos trezentos quatrocentos quinhentos seiscentos setecentos oitocentos novecentos".split()
ORD = {1: "primeir", 2: "segund", 3: "terceir", 4: "quart", 5: "quint", 6: "sext", 7: "sétim", 8: "oitav", 9: "non", 10: "décim"}
# palavras femininas que costumam vir depois de número ("duas semanas", "uma vez")
FEM = set("semana semanas hora horas vez vezes dose doses unidade unidades criança crianças gestação gestações "
          "mulher mulheres causa causas pergunta perguntas consulta consultas classe classes".split())


def _ate999(n, fem):
    if n < 20:
        s = UN[n]
    elif n < 100:
        s = DEZ[n // 10] + ("" if n % 10 == 0 else " e " + UN[n % 10])
    elif n == 100:
        return "cem"
    else:
        s = CEM[n // 100] + ("" if n % 100 == 0 else " e " + _ate999(n % 100, fem))
    if fem:
        s = re.sub(r"\bum$", "uma", re.sub(r"\bdois$", "duas", s))
        s = s.replace("entos", "entas")
    return s


def extenso(n, fem=False):
    """Inteiro por extenso em pt-BR (até 999 milhões)."""
    if n < 1000:
        return _ate999(n, fem)
    partes = []
    mi, n = divmod(n, 1_000_000)
    mil, r = divmod(n, 1000)
    if mi:
        partes.append("um milhão" if mi == 1 else _ate999(mi, False) + " milhões")
    if mil:
        partes.append("mil" if mil == 1 else _ate999(mil, fem) + " mil")
    if r:
        partes.append(("e " if r < 100 or r % 100 == 0 else "") + _ate999(r, fem))
    return " ".join(partes)


SIMBOLOS = [
    (r"β-?hCG", "beta agá cê gê"), (r"\bPALM-COEIN\b", "Pálm Coêin"), (r"\bPALM\b", "Pálm"), (r"\bCOEIN\b", "Coêin"),
    (r"\bFIGO\b", "Fígo"), (r"\bvon Willebrand\b", "fon Vílebrand"), (r"\bkg/m²", "quilos por metro quadrado"),
    (r"(\d)\s*×\s*/\s*dia", r"\1 vezes ao dia"), (r"(\d)\s*×", r"\1 vezes"), (r"\s*/\s*dia\b", " por dia"),
    (r"/kg\b", " por quilo"), (r"/m[lL]\b", " por mililitro"), (r"/h\b", " por hora"), (r"/min\b", " por minuto"), (r"≥", " maior ou igual a "), (r"≤", " menor ou igual a "), (r"≈", " cerca de "),
    (r"±", " mais ou menos "), (r"(?<=\s)>(?=\s*\d)", " maior que "), (r"(?<=\s)<(?=\s*\d)", " menor que "),
    (r"^>(?=\s*\d)", "maior que "), (r"^<(?=\s*\d)", "menor que "), (r"\s*→\s*", ", "), (r"\s*[·—–]\s+", ", "),
    (r"(\d)\s*[–-]\s*(\d)", r"\1 a \2"), (r"\s/\s", " sobre "), (r"%", " por cento"), (r"(\d)\s*°C", r"\1 graus"),
    (r"\b(\d+)/\1\s*(?:h|horas)\b", r"de \1 em \1 horas"), (r"(\d)/(\d)", r"\1 barra \2"),
    (r"(\d+):(\d\d)\b", r"\1 e \2"), (r"(\w)\+(?=[\s,.;)]|$)", r"\1 positivo"), (r"(\w)[−-](?=[\s,.;)]|$)", r"\1 negativo"),
    (r"([A-Za-zÀ-ú])/(?=[A-Za-zÀ-ú])", r"\1 ou "), (r"/(?=\s*\d)", " por "),
]
UNIDADES = {"mm": "milímetros", "cm": "centímetros", "mg": "miligramas", "mcg": "microgramas", "kg": "quilos",
            "g": "gramas", "mL": "mililitros", "ml": "mililitros", "h": "horas", "min": "minutos", "mEq": "miliequivalentes",
            "mmHg": "milímetros de mercúrio", "bpm": "batimentos por minuto", "UI": "unidades internacionais"}
SIGLAS = {"FSH": "éfe ésse agá", "TSH": "tê ésse agá", "DIU": "diu", "SOP": "síndrome dos ovários policísticos",
          "IMC": "índice de massa corporal", "IBP": "i bê pê", "RGE": "refluxo gastroesofágico", "APLV": "a pê éle vê",
          "ITU": "infecção urinária", "LCR": "líquor", "AINE": "anti-inflamatório", "ACO": "anticoncepcional oral",
          "USG": "ultrassom", "MAV": "malformação arteriovenosa", "EV": "endovenoso", "IST": "i ésse tê",
          "PA": "pressão arterial", "FC": "frequência cardíaca", "Hb": "hemoglobina", "HPV": "agá pê vê",
          "SUA": "sangramento uterino anormal", "RR": "risco relativo", "UFC": "unidades formadoras de colônia", "VO": "via oral", "IM": "intramuscular", "SC": "subcutâneo", "RN": "recém-nascido", "UBS": "u bê ésse", "SUS": "sus"}


def falar(t):
    """Texto como deve ser falado: siglas, símbolos, unidades e números por extenso."""
    t = " ".join(t.split())
    for a, b in SIMBOLOS:
        t = re.sub(a, b, t)
    t = re.sub(r"\b(\d+)\s*(" + "|".join(sorted(UNIDADES, key=len, reverse=True)) + r")\b",
               lambda m: m.group(1) + " " + UNIDADES[m.group(2)], t)
    t = re.sub(r"\b(" + "|".join(SIGLAS) + r")\b", lambda m: SIGLAS[m.group(1)], t)
    t = re.sub(r"\b(\d{1,3}(?:\.\d{3})+)\b", lambda m: m.group(1).replace(".", ""), t)  # 40.000 -> 40000
    t = re.sub(r"\b(\d+)\s*([ºª])", lambda m: ORD.get(int(m.group(1)), m.group(1)) + ("o" if m.group(2) == "º" else "a")
               if int(m.group(1)) in ORD else m.group(0), t)

    def num(m):
        inteiro, dec, prox = m.group(1), m.group(2), m.group(3) or ""
        faixa = re.match(r"\s*a\s+\d+\s+(\w+)", m.string[m.end(2) if dec else m.end(1):])  # "2 a 4 semanas"
        fem = prox.lower() in FEM or bool(faixa and faixa.group(1).lower() in FEM)
        s = extenso(int(inteiro), fem)
        if dec:  # 2,05 -> dois vírgula zero cinco
            resto = dec.lstrip("0")
            s += " vírgula " + " ".join(["zero"] * (len(dec) - len(resto)) + ([extenso(int(resto))] if resto else []))
        return s + (" " + prox if prox else "")

    t = re.sub(r"\b(\d+)(?:,(\d+))?\b(?:\s+([A-Za-zÀ-ú]+))?", num, t)
    t = re.sub(r"\s+([,.;:!?])", r"\1", re.sub(r"[()\[\]]", ", ", t))
    t = re.sub(r",\s*,+", ",", re.sub(r"\s{2,}", " ", t)).strip(" ,")
    t = re.sub(r"[,;:]+\s*([.!?])", r"\1", t)
    return t


def frases(t, maximo=160):
    """Frases curtas: quebra no ponto final e, se ainda ficar longa, no ponto e vírgula ou na vírgula do meio."""
    out = []
    for f in re.split(r"(?<=[.!?])\s+", t):
        while len(f) > maximo:
            cortes = [m.end() for m in re.finditer(r"[;:,]\s", f) if 40 < m.end() < len(f) - 30]
            if not cortes:
                break
            c = min(cortes, key=lambda x: abs(x - len(f) / 2))
            out.append(f[:c].strip().rstrip(",;:") + ".")
            f = f[c:].strip()
            f = f[:1].upper() + f[1:]
        if f.strip():
            out.append(f.strip())
    return [f[:1].upper() + f[1:] for f in out]


def lote(itens):
    """{"nome": "texto"} -> texto do lote para colar no app."""
    blocos = []
    for nome, texto in itens.items():
        blocos.append("## " + nome + "\n" + "\n".join(frases(falar(texto))))
    return "\n\n".join(blocos) + "\n"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as f:
        itens = json.load(f)
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        f.write(lote(itens))
    print(len(itens), "falas ->", sys.argv[2])
