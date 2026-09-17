#!/usr/bin/env python3
"""Jasangarritasuna LH – jarduera praktikoa (eskola/enpresa + 17 GJH)."""

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt

# 17 Garapen Jasangarrirako Helburuak (labur)
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

    h = doc.add_heading("Jasangarritasuna – Jarduera praktikoa", level=0)
    h.alignment = WD_ALIGN_PARAGRAPH.CENTER

    azpi = doc.add_paragraph()
    azpi.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = azpi.add_run(
        "17 Garapen Jasangarrirako Helburuak (GJH / ODS)\n"
        "Eskola edo enpresa erreal baten auditoria laburra"
    )
    r.italic = True

    doc.add_heading("Zergatik jarduera hau?", level=1)
    doc.add_paragraph(
        "Helburua ez da 17 helburuak memorizatzea bakarrik, baizik eta "
        "erakunde erreal batean (zure eskola edo aukeratutako enpresa) "
        "zer egiten den eta zer falta den aztertzea. "
        "Horrela, jasangarritasuna praktikan ikusten da."
    )

    doc.add_heading("Entrega", level=1)
    doc.add_paragraph(
        "Entregatu Word dokumentu bat (.docx): "
        "Jasangarritasuna_IzenaAbizena.docx (edo taldearen izena)."
    )
    for item in (
        "Aukeratutako erakundea (eskola / enpresa) eta zergatik.",
        "Informazio-iturriak (webgunea, bisita, elkarrizketa, behaketa…).",
        "17 GJH-en taula beteta (egoera + froga + hobekuntza).",
        "3 hobekuntza-proposamen konkretu (nor, zer, nola, noiz).",
        "Ondorio laburra (5–8 esaldi).",
    ):
        doc.add_paragraph(item, style="List Number")

    doc.add_heading("Lanaren formatua", level=1)
    for item in (
        "Banaka edo binaka (gehienez 3).",
        "Iraupena: 2–4 saio (+ kanpo-bilaketa / elkarrizketa, aukeran).",
        "Amaieran: 5–7 minutuko aurkezpen laburra (ez teorikoa: zuen emaitzak).",
    ):
        doc.add_paragraph(item, style="List Bullet")

    doc.add_heading("1. Erakundea aukeratu", level=1)
    doc.add_paragraph(
        "Aukeratu BATA: (A) zure ikastetxea / zentroa, edo (B) enpresa erreal bat "
        "(tokikoa, familiakoa, praktiketakoa, ezaguna…). "
        "Enpresa aukeratuz gero, informazio publikoa erabili edo baimena eskatu."
    )
    galdera(doc, "1.1", "Erakundearen izena:")
    galdera(doc, "1.2", "Mota: eskola / enpresa / bestelakoa:")
    galdera(doc, "1.3", "Zergatik aukeratu duzue? (1–2 esaldi)", lerroak=2)
    galdera(
        doc,
        "1.4",
        "Informazioa nola lortuko duzue? "
        "(web, memoria, behaketa, irakasle/zuzendaritza, langile bat…)",
        lerroak=2,
    )

    doc.add_heading("2. Diagnostikoa: 17 helburuak puntuz puntu", level=1)
    doc.add_paragraph(
        "Helburu bakoitzerako, bete taula hau (zure dokumentuan kopiatu edo "
        "taula berria egin). Ez da beharrezkoa 17etan aditua izatea: "
        "erakundeari dagokiona aztertu, eta ez badago loturarik, azaldu zergatik."
    )

    doc.add_paragraph().add_run("Egoeraren kodea:").bold = True
    for item in (
        "A – Dagoeneko egiten da / neurri argiak daude",
        "B – Zerbait egiten da, baina hobetu daiteke",
        "C – Ia ez da lantzen / aukera handia dago",
        "D – Ez da aplikagarria erakunde honetan (justifikatu)",
    ):
        doc.add_paragraph(item, style="List Bullet")

    # Taula: GJH | Egoera | Zer egiten da | Zer falta da
    table = doc.add_table(rows=1, cols=4)
    table.style = "Table Grid"
    hdr = table.rows[0].cells
    hdr[0].text = "GJH"
    hdr[1].text = "Egoera (A/B/C/D)"
    hdr[2].text = "Zer egiten da? (froga / adibidea)"
    hdr[3].text = "Zer dago egiteko? (ideia bat)"
    for zb, izena, _desk in GJH:
        row = table.add_row().cells
        row[0].text = f"{zb}. {izena}"
        row[1].text = ""
        row[2].text = ""
        row[3].text = ""

    doc.add_paragraph()
    doc.add_paragraph(
        "Oharra: froga izan daiteke argazkia, web-esteka, politika idatzia, "
        "behaketaren deskribapena edo elkarrizketaren laburpena. "
        "Asmatutakoa ez; oinarritu ikusitakoan."
    )

    doc.add_heading("3. Pista praktikoak (eskola / enpresa)", level=1)
    doc.add_paragraph("Eskolan, adibidez, begiratu:").bold = False
    for item in (
        "Energia: LED, itzalaldiak, panel fotovoltaikoak, tenperatura.",
        "Hondakinak: birziklatzea, papera, plastikoa, jangela.",
        "Ur: komunak, ihesak, kontzientziazioa.",
        "Mugikortasuna: oinez, bizikleta, garraio publikoa, autoa.",
        "Inklusioa: irisgarritasuna, generoa, aniztasuna, jazarpenaren prebentzioa.",
        "Erosketak: material jasangarria, tokiko hornitzaileak, berrerabili.",
        "Curriculum / proiektuak: jasangarritasuna ikasgaietan.",
    ):
        doc.add_paragraph(item, style="List Bullet")

    doc.add_paragraph("Enpresan, adibidez:")
    for item in (
        "Produktua/zerbitzua: bizitza erabilgarria, konponketa, ontziak.",
        "Hornikuntza-katea: jatorria, baldintza sozialak, kilometroak.",
        "Langileak: lan-baldintzak, prestakuntza, berdintasuna.",
        "Energia eta emisioak: fakturak, garraioa, digitalizazioa.",
        "Komunitatea: boluntariotza, tokiko eragina, gardentasuna.",
    ):
        doc.add_paragraph(item, style="List Bullet")

    doc.add_heading("4. Prioritateak: 3 hobekuntza", level=1)
    doc.add_paragraph(
        "17etatik, aukeratu 3 hobekuntza errealistak erakunde horrentzat. "
        "Ez idatzi «gehiago birziklatu» soilik: izan zehatza."
    )
    for i in range(1, 4):
        p = doc.add_paragraph()
        p.add_run(f"Hobekuntza {i}").bold = True
        galdera(doc, f"4.{i}.a", "Zein GJHri lotuta?")
        galdera(doc, f"4.{i}.b", "Zer egin behar da zehazki?", lerroak=2)
        galdera(doc, f"4.{i}.c", "Nor arduratu liteke? (rola / saila)")
        galdera(doc, f"4.{i}.d", "Nola neurtuko zenuke arrakasta? (adierazle bat)")
        galdera(doc, f"4.{i}.e", "Zailtasun posibleak:")

    doc.add_heading("5. Aurkezpena (5–7 min)", level=1)
    doc.add_paragraph("Egitura gomendatua:")
    for item in (
        "Erakundea (30 s)",
        "Egoeraren mapa laburra: zenbat A / B / C / D (1 min)",
        "Adibide on bat + hobetu beharreko bat (2 min)",
        "3 proposamenak (2–3 min)",
        "Galderak (1 min)",
    ):
        doc.add_paragraph(item, style="List Number")
    doc.add_paragraph(
        "Ez irakurri 17 helburuen definizioak denbora guztian. "
        "Zuhaitzaren fruitua: zuen diagnostikoa."
    )

    doc.add_heading("6. Ondorioa (idatziz)", level=1)
    doc.add_paragraph(
        "5–8 esalditan: zer harritu zaituen, zein helburu dauden sendoago, "
        "zein ahulago, eta zer egingo zenuketen zuek aste honetan erakundean."
    )
    for _ in range(6):
        doc.add_paragraph("_______________________________________________")

    doc.add_paragraph()
    ev = doc.add_paragraph()
    ev.add_run("Ebaluazio-iradokizuna (irakaslea): ").bold = True
    ev.add_run(
        "erakunde errealaren aukera · taula beteta frogaekin · "
        "3 proposamen neurgarri · aurkezpen praktikoa · ondorioa."
    )

    # Irakaslearen gida
    doc.add_page_break()
    gh = doc.add_heading("Irakaslearen gida", level=1)
    gh.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph().add_run("Nola dinamizatu").bold = True
    for item in (
        "1. saioa: GJH labur (10–15 min) + erakundea aukeratu + iturriak.",
        "2. saioa: behaketa / bilaketa / elkarrizketa laburra (eskola barruan erraza).",
        "3. saioa: taula bete + 3 hobekuntzak idatzi.",
        "4. saioa: aurkezpen laburrak + feedback.",
    ):
        doc.add_paragraph(item, style="List Bullet")

    doc.add_paragraph().add_run("Zergatik hobea aurkezpen teorikoak baino").bold = True
    doc.add_paragraph(
        "Ikasleak froga bilatzen, lehentasunak jartzen eta ekintzak proposatzen "
        "dituzte. 17 helburuak tresna bihurtzen dira, ez memorizatu beharreko zerrenda."
    )

    doc.add_paragraph().add_run("Aldaera azkarra (saio bakarra)").bold = True
    doc.add_paragraph(
        "Eskola bakarrik, 5 GJH aukeratu (adib. 4, 5, 7, 12, 13) eta taula laburtu. "
        "3 hobekuntzen ordez, 1 proposamen kolektiboa gelan."
    )

    doc.add_paragraph().add_run("17 GJH – oroigarria").bold = True
    for zb, izena, desk in GJH:
        p = doc.add_paragraph()
        p.add_run(f"{zb}. {izena}: ").bold = True
        p.add_run(desk)

    outs = [
        Path("/workspace/testak/jasangarritasuna/Jasangarritasuna_jarduera_praktikoa.docx"),
        Path("/opt/cursor/artifacts/Jasangarritasuna_jarduera_praktikoa.docx"),
    ]
    for p in outs:
        p.parent.mkdir(parents=True, exist_ok=True)
        doc.save(p)
        print("Gordeta:", p)


if __name__ == "__main__":
    main()
