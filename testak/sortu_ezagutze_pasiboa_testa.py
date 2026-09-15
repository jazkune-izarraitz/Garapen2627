#!/usr/bin/env python3
"""Ezagutze pasiboa moduluko 15 galderako testa (Word)."""

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt

# Galdera bakoitzeko aukerak: (testua, mota) — mota: zuzena | txikia | handia
# Dokumentuan ordena nahasia; erantzun-orrian azalpena.
# Aukeren ordena nahasia: zuzena ez da beti "a".
GALDERAK = [
    {
        "zenbakia": 1,
        "galdera": "Zer da ezagutze pasiboa (passive reconnaissance)?",
        "aukerak": [
            ("Helburuko sisteman sartzea eta fitxategiak aldatzea.", "handia"),
            ("Helburuaren informazioa iturri publikoetatik biltzea, helburuarekin zuzenean kontaktatu gabe.", "zuzena"),
            ("Helburuaren informazioa iturri publikoetatik biltzea, baina Nmap erabiliz soilik.", "txikia"),
        ],
    },
    {
        "zenbakia": 2,
        "galdera": "Enpresa baten Facebook orria bisitatzen duzu langileen izenak lortzeko. Zer motatako ezagutzea da?",
        "aukerak": [
            ("Pasiboa, informazio publikoa soilik erabiltzen delako.", "zuzena"),
            ("Ez da ezagutzea; marketing jarduera bat da.", "handia"),
            ("Aktiboa, sare sozialak beti ezagutze aktibotzat hartzen direlako.", "txikia"),
        ],
    },
    {
        "zenbakia": 3,
        "galdera": "Enpresaren web-zerbitzariaren IP helbidea ping egiten duzu ICMP blokeatuta dagoen jakiteko. Zer motatako ezagutzea da?",
        "aukerak": [
            ("Pasiboa, ping komandoa DNS kontsulta bat delako.", "txikia"),
            ("Ez da ezagutzea; sarearen mantentze-lan arrunta da.", "handia"),
            ("Aktiboa, helburuari paketeak bidaltzen zaizkiolako.", "zuzena"),
        ],
    },
    {
        "zenbakia": 4,
        "galdera": "WHOIS protokoloak zer informazio ematen du normalean?",
        "aukerak": [
            ("Zerbitzariaren root pasahitza eta irekitako ataka guztiak.", "handia"),
            ("Domeinuaren erregistro-datuak: erregistratzailea, datak, name-zerbitzariak, etab.", "zuzena"),
            ("Domeinuaren erregistro-datuak eta webguneko HTML kode osoa.", "txikia"),
        ],
    },
    {
        "zenbakia": 5,
        "galdera": "Tradizionalki, WHOIS zerbitzariek zein TCP atakan entzuten dute?",
        "aukerak": [
            ("53", "txikia"),
            ("80", "handia"),
            ("43", "zuzena"),
        ],
    },
    {
        "zenbakia": 6,
        "galdera": "nslookup eta dig tresnek zertarako balio dute?",
        "aukerak": [
            ("DNS erregistroak kontsultatzeko (A, MX, TXT, etab.).", "zuzena"),
            ("WHOIS erregistroak soilik bilatzeko.", "handia"),
            ("DNS erregistroak kontsultatzeko eta, gainera, atakak eskaneatzeko.", "txikia"),
        ],
    },
    {
        "zenbakia": 7,
        "galdera": "dig tresnari buruz, zein baieztapen da zuzena?",
        "aukerak": [
            ("Webguneak deskargatzeko eta HTML analizatzeko tresna da.", "handia"),
            ("DNS kontsultetarako tresna modernoa da, baina TTL balioak inoiz ez ditu erakusten.", "txikia"),
            ("DNS kontsultetarako tresna modernoa da; TTL balioak erakusten ditu eta nslookup baino xehetasun gehiago ematen du.", "zuzena"),
        ],
    },
    {
        "zenbakia": 8,
        "galdera": "DNSDumpster bezalako tresnek zertarako laguntzen dute ezagutze pasiboan?",
        "aukerak": [
            ("Azpidomeinuak aurkitzeko, baina soilik helburuari Nmap bidalita.", "txikia"),
            ("Azpidomeinuak, DNS erregistroak eta azpiegituraren mapa bisuala lortzeko.", "zuzena"),
            ("Malwarea instalatzeko eta saioak bahitzeko.", "handia"),
        ],
    },
    {
        "zenbakia": 9,
        "galdera": "Shodan.io zer da?",
        "aukerak": [
            ("Antivirus programa bat ordenagailu pertsonaletarako.", "handia"),
            ("Internetera konektatutako gailu eta zerbitzuen bilatzailea (OSINT).", "zuzena"),
            ("Soilki DNS MX erregistroak bilatzeko tresna.", "txikia"),
        ],
    },
    {
        "zenbakia": 10,
        "galdera": "Zer esan nahi du DNS siglak?",
        "aukerak": [
            ("Domain Network Service", "txikia"),
            ("Data Numbering Software", "handia"),
            ("Domain Name System", "zuzena"),
        ],
    },
    {
        "zenbakia": 11,
        "galdera": "Zein erregistro motak kudeatzen ditu IPv6 helbideak?",
        "aukerak": [
            ("AAAA", "zuzena"),
            ("MX", "handia"),
            ("A (IPv6 ere onartzen duelako)", "txikia"),
        ],
    },
    {
        "zenbakia": 12,
        "galdera": "Zein erregistro motak adierazten du nora bidali behar den posta elektronikoa?",
        "aukerak": [
            ("CNAME", "txikia"),
            ("MX", "zuzena"),
            ("AAAA", "handia"),
        ],
    },
    {
        "zenbakia": 13,
        "galdera": "CNAME erregistro batek zer egiten du?",
        "aukerak": [
            ("Posta-zerbitzarien lehentasuna (priority) ezartzen du.", "handia"),
            ("Hostname bat IPv4 helbide batera soilik lotzen du.", "txikia"),
            ("Hostname bat beste domeinu-izen batera (alias) lotzen du.", "zuzena"),
        ],
    },
    {
        "zenbakia": 14,
        "galdera": "TTL eremuan zer zehazten da?",
        "aukerak": [
            ("Zenbat denboraz cachean gorde daitekeen DNS erregistro bat.", "zuzena"),
            ("Domeinuaren erregistroaren iraungitze-data WHOIS-en.", "handia"),
            ("Zenbat denboraz cachean gorde daitekeen, baina soilik MX erregistroetan.", "txikia"),
        ],
    },
    {
        "zenbakia": 15,
        "galdera": "Zein DNS zerbitzari motak gordetzen ditu domeinu baten erregistro guztiak?",
        "aukerak": [
            ("WHOIS zerbitzaria, TCP 43 atakan", "handia"),
            ("Authoritative (agintaritza-zerbitzaria)", "zuzena"),
            ("Recursive (ISP-k ematen duena), erregistro guztiak beti bertan daudelako", "txikia"),
        ],
    },
]

LETRAK = ("a", "b", "c")


def aukera_letra(galdera: dict, mota: str) -> str:
    for i, (_testua, m) in enumerate(galdera["aukerak"]):
        if m == mota:
            return LETRAK[i]
    raise ValueError(f"Mota ez da aurkitu: {mota}")


def main() -> None:
    doc = Document()

    for section in doc.sections:
        section.top_margin = Cm(2)
        section.bottom_margin = Cm(2)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.5)

    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)

    izenburua = doc.add_heading("Ezagutze pasiboa – Testa", level=0)
    izenburua.alignment = WD_ALIGN_PARAGRAPH.CENTER

    azpi = doc.add_paragraph()
    azpi.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = azpi.add_run(
        "TryHackMe: Passive Reconnaissance eta DNS in Detail\n"
        "15 galdera · 3 aukera (aukera bakarra zuzena da)"
    )
    run.italic = True
    run.font.size = Pt(11)

    info = doc.add_paragraph()
    info.add_run(
        "Jarraibideak: Galdera bakoitzean aukeratu erantzun zuzena (a, b edo c). "
        "Erantzunak dokumentuko hurrengo orrialdean daude."
    )

    doc.add_paragraph()

    for g in GALDERAK:
        p = doc.add_paragraph()
        p.add_run(f"{g['zenbakia']}. {g['galdera']}").bold = True
        for letra, (testua, _mota) in zip(LETRAK, g["aukerak"]):
            doc.add_paragraph(f"{letra}) {testua}")
        doc.add_paragraph()

    # Erantzunak hurrengo orrian
    doc.add_page_break()

    erantzun_izenburua = doc.add_heading("Erantzunak", level=1)
    erantzun_izenburua.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph(
        "Galdera bakoitzean: erantzun zuzena, akats txikia eta akats handia azaltzen dira."
    )
    doc.add_paragraph()

    for g in GALDERAK:
        zuzena_letra = aukera_letra(g, "zuzena")
        txikia_letra = aukera_letra(g, "txikia")
        handia_letra = aukera_letra(g, "handia")

        zuzena_testua = next(t for t, m in g["aukerak"] if m == "zuzena")
        txikia_testua = next(t for t, m in g["aukerak"] if m == "txikia")
        handia_testua = next(t for t, m in g["aukerak"] if m == "handia")

        p = doc.add_paragraph()
        p.add_run(f"{g['zenbakia']}. ").bold = True
        p.add_run(f"Zuzena: {zuzena_letra}) {zuzena_testua}")

        doc.add_paragraph(
            f"   · Akats txikia: {txikia_letra}) {txikia_testua}",
            style="List Bullet",
        )
        doc.add_paragraph(
            f"   · Akats handia: {handia_letra}) {handia_testua}",
            style="List Bullet",
        )
        doc.add_paragraph()

    irteerak = [
        Path("/workspace/testak/Ezagutze_pasiboa_testa.docx"),
        Path("/opt/cursor/artifacts/Ezagutze_pasiboa_testa.docx"),
    ]
    for bidea in irteerak:
        bidea.parent.mkdir(parents=True, exist_ok=True)
        doc.save(bidea)
        print(f"Gordeta: {bidea}")


if __name__ == "__main__":
    main()
