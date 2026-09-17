#!/usr/bin/env python3
"""Produkzio-sistemari aplikatutako jasangarritasuna – jarduera praktikoa."""

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt

GJH = [
    (1, "Pobrezia amaitzea", "Pobrezia forma guztietan amaitu."),
    (2, "Goserik ez", "Gosea amaitu, elikadura-segurtasuna eta nekazaritza jasangarria."),
    (3, "Osasuna eta ongizatea", "Bizitza osasuntsua eta ongizatea adin guztietan."),
    (4, "Kalitatezko hezkuntza", "Hezkuntza inklusiboa, ekitatiboa eta kalitatezkoa."),
    (5, "Genero-berdintasuna", "Emakumeen eta nesken ahalduntzea."),
    (6, "Ur garbia eta saneamendua", "Uraren eta saneamenduaren kudeaketa jasangarria."),
    (7, "Energia eskuragarri eta garbia", "Energia merkea, fidagarria eta jasangarria."),
    (8, "Lan duina eta hazkunde ekonomikoa", "Hazkunde inklusiboa eta enplegu duina."),
    (9, "Industria, berrikuntza eta azpiegitura", "Azpiegitura iraunkorra eta berrikuntza."),
    (10, "Desberdintasunak murriztea", "Herrialdeen barneko eta arteko desberdintasunak."),
    (11, "Hiri eta komunitate jasangarriak", "Hiri inklusiboak, seguruak eta jasangarriak."),
    (12, "Ekoizpen eta kontsumo arduratsuak", "Kontsumo- eta ekoizpen-eredu jasangarriak."),
    (13, "Klimaren aldeko ekintza", "Klima-aldaketari aurre egiteko neurriak."),
    (14, "Itsaspeko bizitza", "Ozeanoak, itsasoak eta itsas baliabideak."),
    (15, "Lurreko bizitza", "Ekosistemak, basoak, biodibertsitatea."),
    (16, "Bakea, justizia eta erakunde sendoak", "Gizarte baketsuak eta erakunde eraginkorrak."),
    (17, "Helburuen aldeko aliantzak", "Inplementaziorako aliantza globalak."),
]

# Produkzioan bereziki garrantzitsuak
GJH_NAGUSIAK = "7, 8, 9, 12 eta 13"


def galdera(doc, zb, testua, lerroak=1):
    p = doc.add_paragraph()
    p.add_run(f"{zb}. ").bold = True
    p.add_run(testua)
    for _ in range(lerroak):
        doc.add_paragraph("_______________________________________________")


def main():
    doc = Document()
    for s in doc.sections:
        s.top_margin = Cm(2)
        s.bottom_margin = Cm(2)
        s.left_margin = Cm(2.5)
        s.right_margin = Cm(2.5)

    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)

    h = doc.add_heading(
        "Produkzio-sistemari aplikatutako jasangarritasuna", level=0
    )
    h.alignment = WD_ALIGN_PARAGRAPH.CENTER

    azpi = doc.add_paragraph()
    azpi.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = azpi.add_run(
        "Jarduera praktikoa · 17 GJH (ODS)\n"
        "Enpresa / produkzio-sistema erreal baten diagnostikoa"
    )
    r.italic = True

    doc.add_heading("Ikasgaiari egokitzea", level=1)
    doc.add_paragraph(
        "Jarduera honek produkzio-sistema batean (enpresa, lantegia, "
        "tailerra, zerbitzu-enpresa…) jasangarritasuna nola aplikatzen den "
        "aztertzen du. Helburua: 17 GJH-ak produkzioaren errealitatearekin "
        "lotzea — ez teoria hutsa."
    )
    oh = doc.add_paragraph()
    oh.add_run("Oharra: ").bold = True
    oh.add_run(
        "Ikastetxea / eskola ez da aukera nagusia ikasgai honetan. "
        "Eskolak hezkuntza-sistema da, ez produkzio-sistema tipikoa. "
        "Aukeratu enpresa edo produkzio-prozesu argia duen erakundea."
    )

    doc.add_heading("Entrega", level=1)
    doc.add_paragraph(
        "Word (.docx): Produkzio_jasangarritasuna_IzenaAbizena.docx"
    )
    for item in (
        "Aukeratutako enpresa / produkzio-sistema eta zergatik.",
        "Produktua edo zerbitzua + prozesuaren deskribapen laburra.",
        "Informazio-iturriak (web, memoria, bisita, FCT, elkarrizketa…).",
        "17 GJH taula (egoera + froga + hobekuntza), produkzioari lotuta.",
        "3 hobekuntza-proposamen (produkzioan aplikagarriak).",
        "Ondorioa (5–8 esaldi).",
    ):
        doc.add_paragraph(item, style="List Number")

    doc.add_heading("Lanaren formatua", level=1)
    for item in (
        "Banaka edo binaka (gehienez 3).",
        "Iraupena: 2–4 saio (+ bilaketa / elkarrizketa).",
        "Aurkezpena: 5–7 min (emaitzak eta proposamenak, ez 17 definizioak).",
    ):
        doc.add_paragraph(item, style="List Bullet")

    doc.add_heading("1. Produkzio-sistema aukeratu", level=1)
    doc.add_paragraph("Aukeratu hauetako bat:")
    for item in (
        "Tokiko enpresa (industria, elikagaiak, eraikuntza, logistika…).",
        "Praktiketako / FCT enpresa.",
        "Familiako edo ezaguna den enpresa (baimenarekin).",
        "Enpresa publikoaren informazioa (memoria, web, jasangarritasun-txostena).",
        "Tailer / produkzio-prozesu argia duen zerbitzu-enpresa "
        "(adib. inprimategia, konponketa, catering industrial…).",
    ):
        doc.add_paragraph(item, style="List Bullet")

    doc.add_paragraph(
        "Informazio publikoa erabili edo baimena eskatu. "
        "Datu sekreturik edo konfidentzialik ez entregatu."
    )

    galdera(doc, "1.1", "Enpresaren / erakundearen izena:")
    galdera(doc, "1.2", "Sektorea:")
    galdera(
        doc,
        "1.3",
        "Zer ekoizten / eskaintzen du? (produktua edo zerbitzua)",
        lerroak=2,
    )
    galdera(
        doc,
        "1.4",
        "Produkzio-prozesua labur: sarrerak → eraldaketa → irteerak "
        "(lehengaiak, energia, hondakinak, produktua…)",
        lerroak=3,
    )
    galdera(
        doc,
        "1.5",
        "Informazioa nola lortu duzue? (web, txostena, bisita, elkarrizketa…)",
        lerroak=2,
    )

    doc.add_heading("2. Diagnostikoa: 17 helburuak produkzioan", level=1)
    doc.add_paragraph(
        f"Helburu guztiak bete, baina arreta berezia jarri "
        f"{GJH_NAGUSIAK} helburuetan (energia, lana, industria, "
        f"ekoizpen/kontsumoa, klima): produkzio-sistemetan eragin handiena dute."
    )
    doc.add_paragraph(
        "Ez aplikagarria bada (D), justifikatu produkzioarekin lotuta "
        "(ez idatzi «ez dauka zerikusirik» soilik)."
    )

    doc.add_paragraph().add_run("Egoeraren kodea:").bold = True
    for item in (
        "A – Neurri argiak daude produkzioan / enpresan",
        "B – Zerbait egiten da, hobetu daiteke",
        "C – Ia ez da lantzen / aukera handia",
        "D – Ez da aplikagarria (justifikatu)",
    ):
        doc.add_paragraph(item, style="List Bullet")

    table = doc.add_table(rows=1, cols=4)
    table.style = "Table Grid"
    hdr = table.rows[0].cells
    hdr[0].text = "GJH"
    hdr[1].text = "Egoera (A/B/C/D)"
    hdr[2].text = "Zer egiten da? (froga)"
    hdr[3].text = "Zer dago egiteko?"
    for zb, izena, _d in GJH:
        row = table.add_row().cells
        mark = " ★" if zb in (7, 8, 9, 12, 13) else ""
        row[0].text = f"{zb}. {izena}{mark}"
        row[1].text = ""
        row[2].text = ""
        row[3].text = ""

    doc.add_paragraph()
    doc.add_paragraph(
        "★ = produkzio-sistemetan bereziki garrantzitsua. "
        "Froga: web-esteka, memoria, argazkia, behaketa, elkarrizketaren laburpena."
    )

    doc.add_heading("3. Pista praktikoak (produkzioa)", level=1)
    for item in (
        "Lehengaiak: jatorria, birziklatua, tokiko hornitzaileak, gatazka-mineralak.",
        "Energia: kontsumoa, iturri berriztagarriak, eraginkortasuna, LED, makinen itzalaldiak.",
        "Ura: prozesuko ura, isurketak, berrerabilpena.",
        "Hondakinak: birziklatzea, birmanufaktura, zero waste helburuak, ontziak.",
        "Produktuaren bizi-zikloa: diseinua, konponketa, iraupena, amaierako kudeaketa.",
        "Logistika: garraioa, kilometroak, azken milia, biltegia.",
        "Lan-baldintzak: segurtasuna, prestakuntza, lan-orduak, azpikontratazioa.",
        "Berdintasuna eta inklusioa: generoa, aniztasuna, soldata-arrakala.",
        "Berrikuntza: digitalizazioa, automatizazio eraginkorra, I+G jasangarria.",
        "Gardentasuna: ziurtagiriak (ISO 14001, EMAS…), memoria, trazabilitatea.",
    ):
        doc.add_paragraph(item, style="List Bullet")

    doc.add_heading("4. Hiru hobekuntza (produkzioan)", level=1)
    doc.add_paragraph(
        "Aukeratu 3 hobekuntza errealistak enpresa horrentzat. "
        "Lotu produkzio-prozesuari (ez soilik «kanpaina bat egin»)."
    )
    for i in range(1, 4):
        p = doc.add_paragraph()
        p.add_run(f"Hobekuntza {i}").bold = True
        galdera(doc, f"4.{i}.a", "Zein GJHri lotuta?")
        galdera(
            doc,
            f"4.{i}.b",
            "Zer aldatuko litzateke produkzioan / prozesuan?",
            lerroak=2,
        )
        galdera(doc, f"4.{i}.c", "Nor arduratu liteke? (rola / saila)")
        galdera(
            doc,
            f"4.{i}.d",
            "Nola neurtu? (adierazlea: kWh, kg hondakin, €, istripu-tasa…)",
        )
        galdera(doc, f"4.{i}.e", "Kostua / zailtasuna (labur):")

    doc.add_heading("5. Aurkezpena (5–7 min)", level=1)
    for item in (
        "Enpresa + produktua / prozesua (1 min)",
        "Mapa: A/B/C/D laburra, ★ helburuetan arreta (1 min)",
        "Adibide on bat + ahulezia bat produkzioan (2 min)",
        "3 proposamenak (2–3 min)",
        "Galderak",
    ):
        doc.add_paragraph(item, style="List Number")

    doc.add_heading("6. Ondorioa", level=1)
    doc.add_paragraph(
        "5–8 esalditan: produkzio-sistema horrek jasangarritasunari nola "
        "eragiten dion, non dauden aukerak, eta LH ikasle gisa zer ikasi duzuen."
    )
    for _ in range(6):
        doc.add_paragraph("_______________________________________________")

    doc.add_paragraph()
    ev = doc.add_paragraph()
    ev.add_run("Ebaluazioa (irakaslea): ").bold = True
    ev.add_run(
        "produkzio-sistema argia · prozesuaren deskribapena · "
        "taula frogaekin · 3 proposamen neurgarri · aurkezpen praktikoa."
    )

    doc.add_page_break()
    gh = doc.add_heading("Irakaslearen gida", level=1)
    gh.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p = doc.add_paragraph()
    p.add_run("Eskolari buruz: ").bold = True
    p.add_run(
        "Ikasgaiaren izena «Produkzio-sistemari aplikatutako jasangarritasuna» "
        "denez, eskola ez da kasu ideala. Salbuespena: zentroko "
        "tailerra / jangela / mantentze-lanak produkzio-ikuspegitik aztertzea, "
        "baina lehentasuna enpresari eman."
    )

    doc.add_paragraph().add_run("Saioak").bold = True
    for item in (
        "1: GJH + produkzio-lotura (★ 7,8,9,12,13) + enpresa aukeratu.",
        "2: Bilaketa / elkarrizketa / prozesuaren mapa.",
        "3: Taula + 3 hobekuntzak.",
        "4: Aurkezpenak.",
    ):
        doc.add_paragraph(item, style="List Bullet")

    doc.add_paragraph().add_run("17 GJH – oroigarria").bold = True
    for zb, izena, desk in GJH:
        p = doc.add_paragraph()
        star = " ★" if zb in (7, 8, 9, 12, 13) else ""
        p.add_run(f"{zb}. {izena}{star}: ").bold = True
        p.add_run(desk)

    outs = [
        Path(
            "/workspace/testak/jasangarritasuna/"
            "Jasangarritasuna_jarduera_praktikoa.docx"
        ),
        Path("/opt/cursor/artifacts/Jasangarritasuna_jarduera_praktikoa.docx"),
    ]
    for pth in outs:
        pth.parent.mkdir(parents=True, exist_ok=True)
        doc.save(pth)
        print("Gordeta:", pth)


if __name__ == "__main__":
    main()
