#!/usr/bin/env python3
"""Gera o vídeo "SUA em 5 minutos": narração (ElevenLabs ou Kokoro, pt-BR), legendas e cenas.

Edite o roteiro em CENAS e rode:  python3 build.py
Depois: npx hyperframes check  e  npx hyperframes render -o renders/sua-5min.mp4

Cada cena tem falas (segs). Na marcação, um elemento com class="rv" e
data-seg="n" aparece quando a fala n começa; data-f="0.5" atrasa até a metade
dessa fala e data-fx escolhe a entrada (up, pop, wipe, fade).
"""
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys

import numpy as np
import soundfile as sf

ROOT = os.path.dirname(os.path.abspath(__file__))
# FONTE=eleven usa as falas do ElevenLabs em assets/eleven/<cena>-<fala>.mp3 (voz Henrique);
# FONTE=kokoro gera a voz local, frase a frase.
FONTE = os.environ.get("FONTE", "eleven")
VOZ = os.environ.get("VOZ", "pf_dora")
VELOCIDADE = os.environ.get("VELOCIDADE", "1.05")
HF = os.environ.get("HYPERFRAMES_BIN") or shutil.which("hyperframes") or "hyperframes"

PAUSA_FRASE = 0.55  # depois de ponto final, interrogação ou exclamação
PAUSA_CURTA = 0.3   # depois de dois-pontos ou ponto e vírgula
PAUSA_FALA = 0.7    # entre falas da mesma cena
PAUSA_CENA = 1.3    # entre cenas
INICIO = 0.5
FIM = 2.5

# Como a voz deve ler o que a legenda escreve.
PRONUNCIA = [
    ("β-hCG", "beta agá cê gê"),
    ("PALM-COEIN", "Pálm Coêin"),
    ("PALM", "Pálm"),
    ("COEIN", "Coêin"),
    ("FIGO", "Fígo"),
    ("FSH", "éfe ésse agá"),
    ("TSH", "tê ésse agá"),
    ("DIU", "Diu"),
    ("von Willebrand", "fon Vílebrand"),
    ("IMC", "índice de massa corporal"),
    ("SOP", "síndrome dos ovários policísticos"),
    ("%", " por cento"),
    (" mm", " milímetros"),
    (" mg", " miligramas"),
    (" mcg", " microgramas"),
]


def fala(texto):
    for a, b in PRONUNCIA:
        texto = texto.replace(a, b)
    return texto


CENAS = [
    {
        "id": "abertura",
        "segs": [
            "Sangramento uterino anormal. Em cinco minutos, você vai aprender a reconhecer, investigar e tratar.",
            "E tudo cabe em quatro perguntas: está estável? Está grávida? De onde vem? E por quê?",
        ],
        "html": """
<div class="stage center">
  <div class="chap">Ginecologia · revisão do ensaio</div>
  <h1 class="hero">Sangramento uterino <em>anormal</em></h1>
  <div class="sub rv" data-seg="0" data-f="0.55">reconhecer · investigar · tratar</div>
  <div class="row qs">
    <div class="pill rv" data-seg="1" data-f="0.4" data-fx="pop">Estável?</div>
    <div class="pill rv" data-seg="1" data-f="0.55" data-fx="pop">Grávida?</div>
    <div class="pill rv" data-seg="1" data-f="0.7" data-fx="pop">De onde vem?</div>
    <div class="pill rv" data-seg="1" data-f="0.85" data-fx="pop">Por quê?</div>
  </div>
</div>""",
    },
    {
        "id": "definicao",
        "segs": [
            "Sangramento uterino anormal é qualquer alteração do padrão menstrual, fora da gestação, na mulher em idade fértil.",
            "São quatro eixos: frequência, duração, regularidade e volume.",
            "Pela FIGO, o normal é: ciclo de 24 a 38 dias, menstruação de até 8 dias, variação de até 7 a 9 dias entre os ciclos, e um volume que não atrapalha a vida.",
            "O quadro pode ser agudo, intenso a ponto de exigir intervenção imediata, ou crônico, quando a alteração aparece na maioria dos ciclos dos últimos seis meses.",
        ],
        "html": """
<div class="stage">
  <div class="chap"><b>01</b> Definição</div>
  <h2 class="h rv" data-seg="0">Alteração do <em>padrão menstrual</em>, fora da gestação</h2>
  <div class="grid g4">
    <div class="card axis rv" data-seg="1" data-f="0.25"><div class="lbl">Frequência</div><div class="val rv" data-seg="2" data-f="0.12">24 a 38 dias</div></div>
    <div class="card axis rv" data-seg="1" data-f="0.42"><div class="lbl">Duração</div><div class="val rv" data-seg="2" data-f="0.33">até 8 dias</div></div>
    <div class="card axis rv" data-seg="1" data-f="0.6"><div class="lbl">Regularidade</div><div class="val rv" data-seg="2" data-f="0.52">variação ≤ 7 a 9 dias</div></div>
    <div class="card axis rv" data-seg="1" data-f="0.8"><div class="lbl">Volume</div><div class="val rv" data-seg="2" data-f="0.8">não atrapalha a vida</div></div>
  </div>
  <div class="grid g2">
    <div class="card bw rv" data-seg="3" data-f="0.02"><div class="lbl w">Agudo</div><div class="txt">intenso, exige intervenção imediata</div></div>
    <div class="card bn rv" data-seg="3" data-f="0.45"><div class="lbl n">Crônico</div><div class="txt">na maioria dos ciclos dos últimos 6 meses</div></div>
  </div>
</div>""",
    },
    {
        "id": "atendimento",
        "segs": [
            "Imagine uma paciente de 26 anos, sangrando muito há três dias. Por onde começar?",
            "Primeiro, a hemodinâmica: frequência cardíaca, pressão, pulsos, consciência e diurese.",
            "Atenção: a pressão só cai na hipovolemia classe três, com perda de 30 a 40% e frequência acima de 120. A taquicardia vem antes.",
            "Segundo: β-hCG em toda mulher em idade fértil que sangra. Gestação se exclui antes de qualquer conduta.",
            "Só com a paciente estável e o teste negativo, vamos atrás da causa.",
        ],
        "html": """
<div class="stage">
  <div class="chap"><b>02</b> Primeiro atendimento</div>
  <div class="card case rv" data-seg="0"><span class="lbl">Caso 1</span><span class="big">26 anos · sangramento intenso há 3 dias</span></div>
  <div class="grid g2 tall">
    <div class="card rv" data-seg="1">
      <div class="lbl g">1 · Hemodinâmica</div>
      <div class="row chips">
        <span class="chip rv" data-seg="1" data-f="0.3">FC</span><span class="chip rv" data-seg="1" data-f="0.45">PA</span><span class="chip rv" data-seg="1" data-f="0.6">pulsos</span><span class="chip rv" data-seg="1" data-f="0.72">consciência</span><span class="chip rv" data-seg="1" data-f="0.85">diurese</span>
      </div>
      <div class="hypo">
        <div class="hr rv" data-seg="2" data-f="0.05"><b>Classe I</b><span>&lt; 15%</span><span>FC normal</span></div>
        <div class="hr rv" data-seg="2" data-f="0.1"><b>Classe II</b><span>15–30%</span><span>FC &gt; 100</span></div>
        <div class="hr hot rv" data-seg="2" data-f="0.2" data-fx="pop"><b>Classe III</b><span>30–40%</span><span>FC &gt; 120 · PA cai</span></div>
        <div class="hr rv" data-seg="2" data-f="0.3"><b>Classe IV</b><span>&gt; 40%</span><span>FC &gt; 140</span></div>
      </div>
    </div>
    <div class="card rv" data-seg="3">
      <div class="lbl a">2 · Excluir gravidez</div>
      <div class="mega a">β-hCG</div>
      <div class="txt">em toda mulher em idade fértil que sangra, antes de qualquer conduta</div>
    </div>
  </div>
  <div class="strip rv" data-seg="4">Estável ✓ &nbsp; β-hCG negativo ✓ &nbsp;→&nbsp; procurar a causa</div>
</div>""",
    },
    {
        "id": "anamnese",
        "segs": [
            "A idade orienta. Na adolescência, pense em imaturidade do eixo, gestação, infecção e coagulopatia.",
            "Na adulta, disfunção ovulatória e gestação anormal. Na pós-menopausa, atrofia e terapia hormonal, mas câncer de endométrio até prova em contrário.",
            "No exame especular, confirme que o sangue vem do colo e procure pólipo, mioma parido ou cervicite.",
            "No toque, o útero dá a pista: aumentado, nodular e indolor sugere mioma; amolecido e doloroso, adenomiose.",
        ],
        "html": """
<div class="stage">
  <div class="chap"><b>03</b> Anamnese e exame físico</div>
  <h2 class="h rv" data-seg="0">A <em>idade</em> orienta a suspeita</h2>
  <div class="grid g3">
    <div class="card rv" data-seg="0" data-f="0.2"><div class="lbl n">Adolescência</div><div class="txt">imaturidade do eixo · gestação · IST · coagulopatia</div></div>
    <div class="card rv" data-seg="1"><div class="lbl n">Adulta</div><div class="txt">disfunção ovulatória · gestação anormal</div></div>
    <div class="card rv" data-seg="1" data-f="0.4"><div class="lbl n">Pós-menopausa</div><div class="txt">atrofia · terapia hormonal</div><div class="txt w b rv" data-seg="1" data-f="0.68">câncer de endométrio até prova em contrário</div></div>
  </div>
  <div class="grid g2">
    <div class="card rv" data-seg="2"><div class="lbl g">Especular</div><div class="txt">vem do colo? pólipo · mioma parido · cervicite</div></div>
    <div class="card rv" data-seg="3">
      <div class="lbl g">Toque bimanual</div>
      <div class="txt rv" data-seg="3" data-f="0.25"><b>Mioma:</b> aumentado, nodular, indolor</div>
      <div class="txt rv" data-seg="3" data-f="0.7"><b>Adenomiose:</b> amolecido, doloroso</div>
    </div>
  </div>
</div>""",
    },
    {
        "id": "palm",
        "segs": [
            "Para as causas, a FIGO criou o PALM-COEIN. PALM são as causas estruturais, que a imagem ou a histologia mostram.",
            "Pólipo: 20 a 30% dos casos, perto da menopausa.",
            "Adenomiose: endométrio dentro do miométrio, com fluxo aumentado e cólica forte.",
            "Leiomioma: o submucoso dá metrorragia, sangramento fora de hora; o intramural dá menorragia, fluxo aumentado. O subseroso costuma não sangrar.",
            "Malignidade e hiperplasia: na pós-menopausa, endométrio acima de 4 mm pede biópsia.",
        ],
        "html": """
<div class="stage">
  <div class="chap"><b>04</b> Etiologias · PALM-COEIN</div>
  <h2 class="h rv" data-seg="0" data-f="0.35"><em>PALM</em> = estrutural: aparece na imagem ou na histologia</h2>
  <div class="grid g4 letters">
    <div class="card"><div class="L rv" data-seg="0" data-f="0.55" data-fx="pop">P</div><div class="lbl">Pólipo</div><div class="txt rv" data-seg="1">20–30% dos casos · perto da menopausa</div></div>
    <div class="card"><div class="L rv" data-seg="0" data-f="0.62" data-fx="pop">A</div><div class="lbl">Adenomiose</div><div class="txt rv" data-seg="2">endométrio no miométrio · fluxo ↑ + cólica</div></div>
    <div class="card"><div class="L rv" data-seg="0" data-f="0.69" data-fx="pop">L</div><div class="lbl">Leiomioma</div><div class="txt rv" data-seg="3">submucoso → metrorragia</div><div class="txt rv" data-seg="3" data-f="0.45">intramural → menorragia</div><div class="txt m rv" data-seg="3" data-f="0.8">subseroso: raramente sangra</div></div>
    <div class="card"><div class="L rv" data-seg="0" data-f="0.76" data-fx="pop">M</div><div class="lbl">Malignidade e hiperplasia</div><div class="txt rv" data-seg="4">pós-menopausa + endométrio &gt; 4 mm → <b class="w">biópsia</b></div></div>
  </div>
</div>""",
    },
    {
        "id": "coein",
        "segs": [
            "COEIN são as causas não estruturais.",
            "Coagulopatia: a mais comum é a doença de von Willebrand. Desconfie de quem sangra muito desde a menarca.",
            "Ovulatória, a causa mais comum de todas. Na SOP, a mulher não ovula, não forma corpo lúteo e fica sem progesterona. O estrogênio age sem oposição, e o endométrio descama de forma irregular.",
            "Endometrial: falha da hemostasia local, com ciclos regulares e fluxo intenso.",
            "Iatrogênica: DIU de cobre, hormônios e anticoagulantes. E as não classificadas, como a malformação arteriovenosa e a istmocele.",
        ],
        "html": """
<div class="stage">
  <div class="chap"><b>04</b> Etiologias · PALM-COEIN</div>
  <h2 class="h rv" data-seg="0"><em>COEIN</em> = não estrutural</h2>
  <div class="grid g5 letters">
    <div class="card"><div class="L n rv" data-seg="0" data-f="0.3" data-fx="pop">C</div><div class="lbl">Coagulopatia</div><div class="txt rv" data-seg="1">von Willebrand · sangra desde a menarca</div></div>
    <div class="card hot"><div class="L n rv" data-seg="0" data-f="0.4" data-fx="pop">O</div><div class="lbl">Ovulatória</div><div class="tag rv" data-seg="2" data-f="0.05">a mais comum</div></div>
    <div class="card"><div class="L n rv" data-seg="0" data-f="0.5" data-fx="pop">E</div><div class="lbl">Endometrial</div><div class="txt rv" data-seg="3">hemostasia local · ciclos regulares</div></div>
    <div class="card"><div class="L n rv" data-seg="0" data-f="0.6" data-fx="pop">I</div><div class="lbl">Iatrogênica</div><div class="txt rv" data-seg="4">DIU de cobre · hormônios · anticoagulantes</div></div>
    <div class="card"><div class="L n rv" data-seg="0" data-f="0.7" data-fx="pop">N</div><div class="lbl">Não classificada</div><div class="txt rv" data-seg="4" data-f="0.6">MAV · istmocele</div></div>
  </div>
  <div class="chain">
    <span class="rv" data-seg="2" data-f="0.25">SOP: não ovula</span><i class="rv" data-seg="2" data-f="0.32">→</i>
    <span class="rv" data-seg="2" data-f="0.38">sem corpo lúteo</span><i class="rv" data-seg="2" data-f="0.44">→</i>
    <span class="rv" data-seg="2" data-f="0.48">sem progesterona</span><i class="rv" data-seg="2" data-f="0.58">→</i>
    <span class="hot rv" data-seg="2" data-f="0.62">estrogênio sem oposição</span><i class="rv" data-seg="2" data-f="0.75">→</i>
    <span class="rv" data-seg="2" data-f="0.8">descamação irregular</span>
  </div>
</div>""",
    },
    {
        "id": "exames",
        "segs": [
            "Para todas: β-hCG, hemograma com plaquetas e coagulograma.",
            "Se a suspeita é ovulatória: FSH, prolactina e TSH. Fogachos antes dos 40 anos? Pense em insuficiência ovariana precoce e dose o FSH.",
            "Na imagem, a primeira linha é o ultrassom transvaginal. A histerossonografia avalia melhor as lesões focais; a histeroscopia vê e já trata.",
            "Biópsia de endométrio: a partir dos 45 anos, com fatores de risco como obesidade e anovulação crônica, ou na pós-menopausa com endométrio acima de 4 mm.",
        ],
        "html": """
<div class="stage">
  <div class="chap"><b>05</b> Investigação</div>
  <div class="rows">
    <div class="card line rv" data-seg="0"><div class="lbl g">Para todas</div><div class="row chips"><span class="chip rv" data-seg="0" data-f="0.25">β-hCG</span><span class="chip rv" data-seg="0" data-f="0.5">hemograma + plaquetas</span><span class="chip rv" data-seg="0" data-f="0.78">coagulograma</span></div></div>
    <div class="card line rv" data-seg="1"><div class="lbl g">Ovulatória</div><div class="row chips"><span class="chip rv" data-seg="1" data-f="0.12">FSH</span><span class="chip rv" data-seg="1" data-f="0.2">prolactina</span><span class="chip rv" data-seg="1" data-f="0.3">TSH</span><span class="note rv" data-seg="1" data-f="0.5">fogacho &lt; 40 anos → FSH (insuficiência ovariana)</span></div></div>
    <div class="card line rv" data-seg="2"><div class="lbl g">Imagem</div><div class="row chips"><span class="chip hot rv" data-seg="2" data-f="0.1">USG transvaginal: 1ª linha</span><span class="note rv" data-seg="2" data-f="0.45">histerossonografia: lesão focal</span><span class="note rv" data-seg="2" data-f="0.75">histeroscopia: vê e trata</span></div></div>
    <div class="card line rv" data-seg="3"><div class="lbl w">Biópsia</div><div class="row chips"><span class="chip rv" data-seg="3" data-f="0.2">≥ 45 anos</span><span class="chip rv" data-seg="3" data-f="0.4">obesidade · anovulação crônica</span><span class="chip rv" data-seg="3" data-f="0.75">pós-menopausa + endométrio &gt; 4 mm</span></div></div>
  </div>
</div>""",
    },
    {
        "id": "agudo",
        "segs": [
            "De volta à paciente de 26 anos. A conduta tem cinco passos: estabilizar, excluir gravidez, parar o sangramento, tratar a anemia e prevenir, investigando a causa.",
            "Instável: volume, transfusão, estrogênio conjugado endovenoso e tamponamento com balão.",
            "Estável: anticoncepcional combinado de 35 mcg, três vezes ao dia. Se o estrogênio for contraindicado, medroxiprogesterona 20 mg, três vezes ao dia, por sete dias.",
            "Depois: ferro, hormônio por três meses e investigação da causa.",
        ],
        "html": """
<div class="stage">
  <div class="chap"><b>06</b> Tratamento do SUA agudo</div>
  <div class="grid g5 steps">
    <div class="card rv" data-seg="0" data-f="0.25"><div class="num">1</div><div class="txt b">Estabilizar</div></div>
    <div class="card rv" data-seg="0" data-f="0.37"><div class="num">2</div><div class="txt b">Excluir gravidez</div></div>
    <div class="card rv" data-seg="0" data-f="0.5"><div class="num">3</div><div class="txt b">Parar o sangramento</div></div>
    <div class="card rv" data-seg="0" data-f="0.65"><div class="num">4</div><div class="txt b">Tratar a anemia</div></div>
    <div class="card rv" data-seg="0" data-f="0.8"><div class="num">5</div><div class="txt b">Prevenir: investigar a causa</div></div>
  </div>
  <div class="grid g2">
    <div class="card bw rv" data-seg="1"><div class="lbl w">Instável</div><div class="txt">volume · transfusão · estrogênio conjugado EV · balão</div></div>
    <div class="card bg rv" data-seg="2"><div class="lbl g">Estável</div><div class="txt"><b>ACO 35 mcg</b>, 3×/dia</div><div class="txt rv" data-seg="2" data-f="0.42">contraindicação a estrogênio: <b>medroxiprogesterona 20 mg</b>, 3×/dia, 7 dias</div></div>
  </div>
  <div class="strip rv" data-seg="3">Depois: ferro + hormônio por 3 meses + investigar a causa</div>
</div>""",
    },
    {
        "id": "cronico",
        "segs": [
            "No crônico, as opções hormonais são o anticoncepcional combinado, o progestagênio e o DIU de levonorgestrel.",
            "Sem hormônio: ácido tranexâmico, anti-inflamatório e ferro.",
            "Mas lembre: o remédio controla o sintoma, não remove a causa estrutural. Pólipo se resolve com polipectomia.",
            "Na cirurgia, prefira a histeroscopia à curetagem, que é às cegas. Embolização, principalmente na malformação arteriovenosa. E a histerectomia fica como última opção.",
        ],
        "html": """
<div class="stage">
  <div class="chap"><b>07</b> Tratamento do SUA crônico</div>
  <div class="grid g2">
    <div class="card rv" data-seg="0"><div class="lbl n">Hormonal</div><div class="row chips"><span class="chip rv" data-seg="0" data-f="0.4">ACO</span><span class="chip rv" data-seg="0" data-f="0.6">progestagênio</span><span class="chip rv" data-seg="0" data-f="0.8">DIU de levonorgestrel</span></div></div>
    <div class="card rv" data-seg="1"><div class="lbl n">Não hormonal</div><div class="row chips"><span class="chip rv" data-seg="1" data-f="0.25">ácido tranexâmico</span><span class="chip rv" data-seg="1" data-f="0.55">AINE</span><span class="chip rv" data-seg="1" data-f="0.8">ferro</span></div></div>
  </div>
  <div class="quote rv" data-seg="2"><div>O remédio controla o <em>sintoma</em>, não remove a <em>causa estrutural</em>.</div><span class="rv" data-seg="2" data-f="0.7">pólipo → polipectomia</span></div>
  <div class="grid g3">
    <div class="card rv" data-seg="3"><div class="lbl g">Histeroscopia</div><div class="txt">melhor que curetagem às cegas</div></div>
    <div class="card rv" data-seg="3" data-f="0.45"><div class="lbl g">Embolização</div><div class="txt">principalmente na MAV</div></div>
    <div class="card rv" data-seg="3" data-f="0.75"><div class="lbl w">Histerectomia</div><div class="txt">última opção</div></div>
  </div>
</div>""",
    },
    {
        "id": "obesidade",
        "segs": [
            "Um capítulo à parte: a obesidade. A gordura converte androgênio em estrona, a mulher deixa de ovular, e o estrogênio fica sem oposição, levando à hiperplasia.",
            "A cada 5 pontos a mais de IMC, o risco de câncer de endométrio sobe cerca de 60%.",
            "E perder de 5 a 10% do peso pode devolver a ovulação.",
        ],
        "html": """
<div class="stage">
  <div class="chap"><b>08</b> Obesidade e SOP</div>
  <div class="chain big">
    <span class="rv" data-seg="0" data-f="0.3">gordura</span><i class="rv" data-seg="0" data-f="0.35">→</i>
    <span class="rv" data-seg="0" data-f="0.4">estrona</span><i class="rv" data-seg="0" data-f="0.5">→</i>
    <span class="rv" data-seg="0" data-f="0.55">anovulação</span><i class="rv" data-seg="0" data-f="0.65">→</i>
    <span class="hot rv" data-seg="0" data-f="0.7">estrogênio sem oposição</span><i class="rv" data-seg="0" data-f="0.85">→</i>
    <span class="rv" data-seg="0" data-f="0.9">hiperplasia</span>
  </div>
  <div class="grid g2">
    <div class="card stat rv" data-seg="1"><div class="mega w">RR 1,59</div><div class="txt">câncer de endométrio a cada +5 kg/m² de IMC</div></div>
    <div class="card stat rv" data-seg="2"><div class="mega g">−5 a 10%</div><div class="txt">do peso pode devolver a ovulação</div></div>
  </div>
</div>""",
    },
    {
        "id": "joana",
        "segs": [
            "Caso Joana: 38 anos, IMC de 36, ciclos de 35 a 90 dias e hirsutismo. Hemoglobina 9,4, ferritina 8, endométrio de 16 mm.",
            "Diagnóstico: sangramento ovulatório por SOP. Como é obesa e tem endométrio espesso, faz biópsia, mesmo antes dos 45: hiperplasia sem atipia.",
            "Conduta: DIU de levonorgestrel de 52 mg, ferro e perda de peso.",
        ],
        "html": """
<div class="stage">
  <div class="chap"><b>09</b> Caso integrador</div>
  <div class="grid g2">
    <div class="card rv" data-seg="0">
      <div class="lbl a">Joana, 38 anos</div>
      <div class="facts">
        <span class="rv" data-seg="0" data-f="0.12">IMC 36</span>
        <span class="rv" data-seg="0" data-f="0.25">ciclos 35–90 dias</span>
        <span class="rv" data-seg="0" data-f="0.4">hirsutismo</span>
        <span class="rv" data-seg="0" data-f="0.55">Hb 9,4</span>
        <span class="rv" data-seg="0" data-f="0.68">ferritina 8</span>
        <span class="rv" data-seg="0" data-f="0.82">endométrio 16 mm</span>
      </div>
    </div>
    <div class="col">
      <div class="card rv" data-seg="1"><div class="lbl n">Diagnóstico</div><div class="big">SUA-O por SOP</div><div class="txt rv" data-seg="1" data-f="0.55">biópsia (obesa + endométrio espesso): <b>hiperplasia sem atipia</b></div></div>
      <div class="card bg rv" data-seg="2"><div class="lbl g">Conduta</div><div class="txt"><b>DIU de levonorgestrel 52 mg</b> · ferro · perder 5–10% do peso</div></div>
    </div>
  </div>
</div>""",
    },
    {
        "id": "resumo",
        "segs": [
            "Para fechar, as quatro perguntas: está estável? Está grávida? De onde vem o sangue? E por quê?",
            "Responda nessa ordem, e o sangramento uterino anormal deixa de ser um mistério.",
        ],
        "html": """
<div class="stage">
  <div class="chap"><b>10</b> Resumo</div>
  <div class="grid g2 qgrid">
    <div class="card rv" data-seg="0" data-f="0.25" data-fx="pop"><div class="num">1</div><div class="big">Está estável?</div><div class="txt m">hemodinâmica</div></div>
    <div class="card rv" data-seg="0" data-f="0.42" data-fx="pop"><div class="num">2</div><div class="big">Está grávida?</div><div class="txt m">β-hCG</div></div>
    <div class="card rv" data-seg="0" data-f="0.6" data-fx="pop"><div class="num">3</div><div class="big">De onde vem?</div><div class="txt m">exame especular · PALM</div></div>
    <div class="card rv" data-seg="0" data-f="0.82" data-fx="pop"><div class="num">4</div><div class="big">Por quê?</div><div class="txt m">COEIN · exames · biópsia</div></div>
  </div>
  <div class="strip rv" data-seg="1">Nessa ordem: estável → grávida → de onde vem → por quê</div>
</div>""",
    },
]

CENA_TPL = """<template>
  <style>
    #root {{ position: absolute; inset: 0; }}
  </style>
  <div id="root" data-composition-id="{id}" data-width="1920" data-height="1080">
    <div id="{id}-stage" class="scene">{html}
    </div>
  </div>
  <script>
    (function () {{
      const tl = gsap.timeline({{ paused: true }});
      const SEG = {segs};
      const DUR = {dur};
      const root = document.getElementById("{id}-stage");
      root.querySelectorAll(".rv").forEach((el) => {{
        const s = SEG[+el.dataset.seg || 0];
        const t = Math.max(0.05, s[0] + (+el.dataset.f || 0) * s[1] - 0.12);
        const fx = el.dataset.fx || "up";
        if (fx === "pop") tl.fromTo(el, {{ opacity: 0, scale: 0.86 }}, {{ opacity: 1, scale: 1, duration: 0.45, ease: "back.out(1.6)" }}, t);
        else if (fx === "fade") tl.fromTo(el, {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4, ease: "power2.out" }}, t);
        else tl.fromTo(el, {{ opacity: 0, y: 26, filter: "blur(6px)" }}, {{ opacity: 1, y: 0, filter: "blur(0px)", duration: 0.5, ease: "expo.out" }}, t);
      }});
      tl.to(root, {{ opacity: 0, filter: "blur(8px)", duration: 0.3, ease: "power3.in" }}, DUR - 0.34);
      window.__timelines["{id}"] = tl;
    }})();
  </script>
</template>
"""


def tts(texto, destino):
    cmd = [HF, "tts", texto, "-v", VOZ, "-l", "pt-br", "-s", VELOCIDADE, "-o", destino]
    r = subprocess.run(cmd, capture_output=True, text=True, env={**os.environ, "HYPERFRAMES_TELEMETRY": "0"})
    if r.returncode != 0 or not os.path.exists(destino):
        sys.exit("TTS falhou: " + r.stdout[-500:] + r.stderr[-500:])


FRACAS = {"de", "a", "o", "e", "do", "da", "dos", "das", "no", "na", "em", "com", "que", "um", "uma", "por", "se", "à", "ao", "as", "os"}


def aparar(dados, sr, limiar=0.008, margem=0.04):
    """Tira o silêncio que o TTS deixa no começo e no fim de cada frase."""
    voz = np.flatnonzero(np.abs(dados) > limiar)
    if not len(voz):
        return dados
    m = int(margem * sr)
    return dados[max(0, voz[0] - m): voz[-1] + m]


def pausas(dados, sr, n, janela=0.02, limiar=0.012, minimo=0.15):
    """Meio das n pausas mais longas do áudio, em ordem de tempo."""
    if n <= 0:
        return []
    w = int(janela * sr)
    rms = np.sqrt(np.convolve(dados ** 2, np.ones(w) / w, mode="same"))[::w]
    quieto = rms < limiar
    trechos, ini = [], None
    for i, q in enumerate(quieto):
        if q and ini is None:
            ini = i
        elif not q and ini is not None:
            if (i - ini) * janela >= minimo:
                trechos.append(((i - ini) * janela, (ini + i) / 2 * janela))
            ini = None
    escolhidos = sorted(trechos, reverse=True)[:n]
    meios = sorted(m for _, m in escolhidos)
    while len(meios) < n:  # sem pausas suficientes: divide o que falta igualmente
        meios.append((meios[-1] if meios else 0) + 0.5)
    return meios


def legendar(legendas, frase, ini, dur):
    """Dentro da frase, tempo de cada grupo proporcional ao número de caracteres."""
    gs = grupos(frase)
    pesos = [len(g) + 6 * len(re.findall(r"[.?!:;,]", g)) for g in gs]
    tot = sum(pesos)
    acc = 0
    for g, p in zip(gs, pesos):
        a = ini + dur * acc / tot
        acc += p
        legendas.append([a, ini + dur * acc / tot, g])


def grupos(texto, max_palavras=6):
    """Quebra a legenda em grupos curtos, preferindo pontuação."""
    palavras = texto.split()
    out, cur = [], []
    for p in palavras:
        cur.append(p)
        fim_frase = re.search(r"[.?!:;]$", p)
        virgula = p.endswith(",") and len(cur) >= 3
        fraca = p.lower() in FRACAS or re.match(r"^[\d≥≤<>+−-]", p)
        if fim_frase or virgula or (len(cur) >= max_palavras and not fraca) or len(cur) >= max_palavras + 3:
            out.append(" ".join(cur))
            cur = []
    if cur:
        if out and len(cur) <= 2 and len(out[-1].split()) <= 4:
            out[-1] += " " + " ".join(cur)
        else:
            out.append(" ".join(cur))
    return out


def main():
    os.makedirs(os.path.join(ROOT, "assets", "tts"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "compositions"), exist_ok=True)
    sr = None
    audio = []
    t = INICIO
    legendas = []
    cenas_t = []
    for ci, cena in enumerate(CENAS):
        if ci:
            t += PAUSA_CENA
        cena_ini = t
        segs = []
        for si, cap in enumerate(cena["segs"]):
            if si:
                t += PAUSA_FALA
            pecas = [x for x in re.split(r"(?<=[.?!:;])\s+", cap) if x]
            seg_ini = t
            if FONTE == "eleven":
                dados, sr_ = sf.read(os.path.join(ROOT, "assets", "eleven", f"{cena['id']}-{si}.mp3"), dtype="float32")
                if dados.ndim > 1:
                    dados = dados.mean(axis=1)
                sr = sr or sr_
                dados = aparar(dados, sr)
                audio.append((t, dados))
                # as pausas já estão no áudio: cada frase vai de uma pausa até a próxima
                cortes = [0.0] + pausas(dados, sr, len(pecas) - 1) + [len(dados) / sr]
                for pi, peca in enumerate(pecas):
                    a, b = cortes[pi], cortes[pi + 1]
                    legendar(legendas, peca, t + a, b - a)
                t += len(dados) / sr
                segs.append([seg_ini, t - seg_ini])
                continue
            # cada frase é gerada à parte, com silêncio de verdade entre elas
            for pi, peca in enumerate(pecas):
                say = fala(peca)
                h = hashlib.md5((VOZ + VELOCIDADE + say).encode()).hexdigest()[:12]
                wav = os.path.join(ROOT, "assets", "tts", f"{cena['id']}-{si}-{pi}-{h}.wav")
                if not os.path.exists(wav):
                    print("TTS", cena["id"], si, pi, flush=True)
                    tts(say, wav)
                dados, sr_ = sf.read(wav, dtype="float32")
                if dados.ndim > 1:
                    dados = dados.mean(axis=1)
                sr = sr or sr_
                dados = aparar(dados, sr)
                dur = len(dados) / sr
                audio.append((t, dados))
                legendar(legendas, peca, t, dur)
                t += dur
                if pi + 1 < len(pecas):
                    t += PAUSA_CURTA if peca[-1] in ":;" else PAUSA_FRASE
            segs.append([seg_ini, t - seg_ini])
        cenas_t.append((cena, cena_ini, segs))
    total = t + FIM

    # mixagem da narração
    n = int(total * sr)
    mix = np.zeros(n, dtype="float32")
    for ini, dados in audio:
        a = int(ini * sr)
        mix[a:a + len(dados)] += dados[: n - a]
    pico = np.abs(mix).max() or 1
    mix = mix / pico * 0.89
    wav = os.path.join(ROOT, "assets", "narracao.wav")
    sf.write(wav, mix, sr)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-ac", "1", "-b:a", "96k",
                    os.path.join(ROOT, "assets", "narracao.mp3")], check=True)
    os.remove(wav)

    # cenas: cada uma vai do meio da pausa anterior ao meio da próxima
    hosts = []
    for i, (cena, ini, segs) in enumerate(cenas_t):
        a = 0 if i == 0 else round(ini - PAUSA_CENA / 2, 3)
        if i + 1 < len(cenas_t):
            b = round(cenas_t[i + 1][1] - PAUSA_CENA / 2, 3)
        else:
            b = round(total, 3)
        rel = [[round(s - a, 3), round(d, 3)] for s, d in segs]
        dur = round(b - a, 3)
        if i + 1 == len(cenas_t):
            dur += 1  # a última cena não some
        with open(os.path.join(ROOT, "compositions", cena["id"] + ".html"), "w") as f:
            f.write(CENA_TPL.format(id=cena["id"], html=cena["html"], segs=json.dumps(rel), dur=dur))
        hosts.append(
            f'      <div id="{cena["id"]}" data-composition-id="{cena["id"]}" data-composition-src="compositions/{cena["id"]}.html"'
            f' data-start="{a}" data-duration="{round(b - a, 3)}" data-track-index="1" data-track-kind="graphics"'
            f' data-width="1920" data-height="1080"></div>'
        )

    # legendas
    linhas, tweens = [], []
    for i, (ini, fim, g) in enumerate(legendas):
        abre = ini - 0.05
        prox = legendas[i + 1][0] - 0.05 if i + 1 < len(legendas) else fim + 1
        fecha = prox if prox - fim < 0.5 else fim + 0.25
        linhas.append(f'    <div class="cg" id="cg{i}"><span>{html.escape(g)}</span></div>')
        tweens.append(f"      [{abre:.3f},{fecha:.3f}]")
    with open(os.path.join(ROOT, "compositions", "legendas.html"), "w") as f:
        f.write(LEG_TPL.replace("{{LINHAS}}", "\n".join(linhas)).replace("{{TEMPOS}}", ",\n".join(tweens)))
    hosts.append(
        f'      <div id="legendas" data-composition-id="legendas" data-composition-src="compositions/legendas.html"'
        f' data-start="0" data-duration="{round(total, 3)}" data-track-index="2" data-track-kind="captions"'
        f' data-width="1920" data-height="1080"></div>'
    )

    with open(os.path.join(ROOT, "index.tpl")) as f:
        idx = f.read()
    idx = idx.replace("{{TOTAL}}", str(round(total, 3))).replace("{{HOSTS}}", "\n".join(hosts))
    with open(os.path.join(ROOT, "index.html"), "w") as f:
        f.write(idx)
    print(f"ok: {len(CENAS)} cenas, {len(legendas)} legendas, {total:.1f} s ({total / 60:.1f} min)")


LEG_TPL = """<template>
  <style>
    #root { position: absolute; inset: 0; pointer-events: none; }
    .cg { position: absolute; left: 0; right: 0; bottom: 84px; text-align: center; opacity: 0; }
    .cg span {
      display: inline-block; max-width: 1560px; padding: 12px 30px; border-radius: 16px;
      background: rgba(6, 10, 22, 0.82); color: #ffffff;
      font: 600 50px/1.25 "Inter", sans-serif; letter-spacing: -0.005em;
    }
  </style>
  <div id="root" data-composition-id="legendas" data-width="1920" data-height="1080">
{{LINHAS}}
  </div>
  <script>
    (function () {
      const tl = gsap.timeline({ paused: true });
      const T = [
{{TEMPOS}}
      ];
      T.forEach(([a, b], i) => {
        const el = document.getElementById("cg" + i);
        tl.fromTo(el, { opacity: 0 }, { opacity: 1, duration: 0.08, ease: "power1.out" }, Math.max(0.1, a));
        tl.to(el, { opacity: 0, duration: 0.08, ease: "power2.in" }, b - 0.08);
        tl.set(el, { opacity: 0, visibility: "hidden" }, b);
      });
      window.__timelines["legendas"] = tl;
    })();
  </script>
</template>
"""

if __name__ == "__main__":
    main()
