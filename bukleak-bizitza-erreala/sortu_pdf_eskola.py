#!/usr/bin/env python3
"""Izarraitz school-format worksheet for Bukleak bizitza errealean."""
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    Image, PageBreak, Flowable, KeepTogether,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
import copy

pdfmetrics.registerFont(TTFont("Body", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("Body-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

PAGE = landscape(A4)
MARGIN = 1.15 * cm
CONTENT_W = PAGE[0] - 2 * MARGIN

TEAL = HexColor("#1a4a6e")
GRAY_BG = HexColor("#d9d9d9")
BOX = HexColor("#222222")
LIGHT = HexColor("#f7f7f7")


def S(name, **kw):
    base = dict(fontName="Body", fontSize=9, leading=12)
    base.update(kw)
    return ParagraphStyle(name, **base)


STY = {
    "title": S("title", fontName="Body-Bold", fontSize=13, alignment=1, leading=16),
    "intro": S("intro", fontSize=9, leading=12),
    "sec": S("sec", fontName="Body-Bold", fontSize=11, textColor=TEAL, leading=14),
    "ex": S("ex", fontName="Body-Bold", fontSize=9.5, leading=12),
    "body": S("body", fontSize=8.5, leading=11),
    "req": S("req", fontName="Body-Bold", fontSize=8, leading=10, textColor=HexColor("#444")),
    "bul": S("bul", fontSize=8, leading=10.5),
    "exl": S("exl", fontName="Body-Bold", fontSize=7.5, leading=9, textColor=HexColor("#555")),
    "exm": S("exm", fontSize=7.5, leading=9.5),
    "note": S("note", fontSize=7.5, leading=9.5, textColor=HexColor("#8B4513")),
    "foot": S("foot", fontSize=7, textColor=HexColor("#666"), alignment=1),
    "sch": S("sch", fontName="Body-Bold", fontSize=12, textColor=TEAL, alignment=2),
    "sch2": S("sch2", fontSize=9, textColor=TEAL, alignment=2),
    "sch3": S("sch3", fontSize=7.5, textColor=HexColor("#666"), alignment=2),
}


def esc(t: str) -> str:
    return (
        t.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br/>")
    )


def P(text, style):
    return Paragraph(esc(text), STY[style])


def title_bar(text):
    t = Table([[P(text, "title")]], colWidths=[CONTENT_W])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), GRAY_BG),
                ("BOX", (0, 0), (-1, -1), 1.15, black),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    return t


def box_cell(parts, width, bg=white):
    data = [[p] for p in parts]
    t = Table(data, colWidths=[width - 4])
    t.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.8, BOX),
                ("BACKGROUND", (0, 0), (-1, -1), bg),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (0, 0), 5),
                ("BOTTOMPADDING", (0, -1), (0, -1), 5),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 1), (-1, -2), 1),
                ("BOTTOMPADDING", (0, 1), (-1, -2), 1),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return t


def exercise_parts(title, body, reqs=None, example=None, note=None):
    parts = [P(title, "ex"), P(body, "body")]
    if reqs:
        parts.append(P("Eskatzen da:", "req"))
        for r in reqs:
            parts.append(P("•  " + r, "bul"))
    if example:
        parts.append(Spacer(1, 2))
        parts.append(P("Adibidea:", "exl"))
        parts.append(P(example, "exm"))
    if note:
        parts.append(P("Oharra: " + note, "note"))
    return parts


def two_col(left_parts, right_parts, gap=0.35 * cm):
    col = (CONTENT_W - gap) / 2
    left = box_cell(left_parts, col)
    right = box_cell(right_parts, col)
    t = Table([[left, right]], colWidths=[col, col])
    t.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return t


def header():
    logo = Image(
        "/workspace/bukleak-bizitza-erreala/izarraitz-logoa.png",
        width=4.0 * cm,
        height=4.0 * cm * 67 / 231,
    )
    right = [P("IZARRAITZ", "sch"), P("Lanbide Heziketa", "sch2"), P("Garapen-inguruneak · Pseint · Bukleak", "sch3")]
    t = Table([[logo, right]], colWidths=[4.8 * cm, CONTENT_W - 4.8 * cm])
    t.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (1, 0), (1, 0), "RIGHT"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return t


def build_story():
    story = []
    story.append(header())
    story.append(Spacer(1, 5))
    story.append(title_bar("Bukleak bizitza errealean – ariketa praktikoak"))
    story.append(Spacer(1, 5))
    story.append(
        P(
            "Problema bakoitzak eguneroko edo eskolako testuinguru bat du. "
            "Irakurri enuntziatua, erabaki zein bukle komeni den (PARA, MIENTRAS edo REPETIR) "
            "eta ebatzi Pseint-en edo fluxu-diagraman.",
            "intro",
        )
    )
    story.append(Spacer(1, 4))

    story.append(P("A. PARA buklea", "sec"))
    story.append(Spacer(1, 2))
    a1 = exercise_parts(
        "A1. Klaseko asistentzia",
        "Irakasleak astean zehar 5 egunetan ikasle kopurua jaso nahi du. Programa batek egun bakoitzean (1etik 5era) zenbat ikasle etorri diren galdetuko du eta amaieran asteko asistentzia osoa erakutsiko du. Ikasle kopuru totala ere galdetu egin beharko du.",
        reqs=[
            "Gelako ikasle kopuru totala galdetu.",
            "5 aldiz galdetu eguneko ikasle kopurua (astelehenetik ostiralera).",
            "Asteko asistentzia portzentaia erakutsi.",
        ],
    )
    a2 = exercise_parts(
        "A2. Atzerako kontaketa – atsedenaldia",
        "Kiroldegiko pantailak saskibaloi partida batean talde baten posesioa amaitzeko atzerako kontaketa erakusten du. Programak 24tik 0ra zenbatuko du eta pantailan erakusten joan.",
    )
    a3 = exercise_parts(
        "A3. Kantina – hamaiketakoa",
        "Kantinak 8 pertsonaren hileko gastua kalkulatu behar du. Pertsona bakoitzari galdetuko dio zenbat faktura dituen, eta faktura bakoitzaren prezioa galdetzen joango da. Amaieran:",
        reqs=[
            "Pertsona bakoitzaren gastu totala.",
            "Batez besteko gastua pertsonako.",
        ],
    )
    story.append(two_col(a1, a2 + [Spacer(1, 4)] + a3))
    story.append(Spacer(1, 6))

    story.append(P("B. MIENTRAS buklea", "sec"))
    story.append(Spacer(1, 2))
    b1 = exercise_parts(
        "B1. Liburutegiko maileguak",
        "Liburutegiak ikasleen maileguak erregistratzen ditu. Programak liburu-izenburuak irakurtzen joango da «AMAITU» idatzi arte. Amaieran zenbat liburu mailegatu diren esango du.",
    )
    b2 = exercise_parts(
        "B2. Autobusaren txartela",
        "Ikasleak autobus-txartelean 15 € ditu. Bidai bakoitzak 1,20 € balio du. Programak bidaiak kontatzen joango da saldoa agortu arte (edo txartelak ezin duenean beste bidai bat ordaindu). Amaieran zenbat bidai egin dituen eta sobratutako euroak erakutsiko ditu.",
        note="Saldoa ez bada 1,20 €-ra iristen ere bidaia egiten utzi behar dio eta saldo negatiboa ezarri.",
    )
    b3 = exercise_parts(
        "B3. Notak",
        "Tutoreak ikasle bakoitzaren izena galdetzen du eta banan bana ikaslearen notak sartzen ditu. 0 sartzen duenean amaitzen da. Programak ikasle bakoitzaren izena eta noten batez bestekoa erakutsiko ditu.",
    )
    story.append(two_col(b1 + [Spacer(1, 4)] + b3, b2))

    # Page 2
    story.append(PageBreak())
    story.append(header())
    story.append(Spacer(1, 5))
    story.append(title_bar("Bukleak bizitza errealean – ariketa praktikoak (2)"))
    story.append(Spacer(1, 5))

    story.append(P("C. REPETIR buklea", "sec"))
    story.append(Spacer(1, 2))
    c1 = exercise_parts(
        "C1. Pasahitzaren balidazioa",
        "Eskolako wifiak pasahitza eskatzen du, baina ikasle bakoitzak bere pasahitz propioa du. Programak ikaslearen izena galdetuko du eta pasahitz zuzena «IkaslearenIzena_2026» izango da. Erabiltzaileak asmatu arte galdetzen jarraituko du. Asmatzen duenean «Ongi etorri!» idatzi.",
        example="Zure izena: Jon\nPasahitza: kaixo\nPasahitza: 1234\nPasahitza: Jon_2026\nOngi etorri!",
    )
    c2 = exercise_parts(
        "C2. Menua – jolasaretoa",
        "Jolasaretoko makina batek menu hau erakusten du behin eta berriro, erabiltzaileak 0 aukeratu arte:",
        reqs=[
            "Aukera bakoitzeko mezu labur bat erakutsi (adib. «Futbola aukeratuta»).",
            "0 aukeratzen denean «Agur!» idatzi eta bukatu.",
            "Aukera baliogabea bada, «Aukera okerra» esan eta menua erakutsi berriro.",
        ],
        example="1. Futbola\n2. Saskibaloia\n3. Ping-pongea\n0. Irten\nAukeratu:",
    )
    story.append(two_col(c1, c2))
    story.append(Spacer(1, 6))

    story.append(P("D. Zuk aukeratu bukle mota", "sec"))
    story.append(Spacer(1, 2))
    d1 = exercise_parts(
        "D1. Futbol-taldeko golegileak",
        "Taldeak 11 jokalari ditu. Jokalari bakoitzak zenbat gol sartu dituen galdetu. Amaieran: gol totalak, batez bestekoa, eta golik gehien sartu dituenaren kopurua (izenik gabe, zenbakia soilik).",
    )
    d2 = exercise_parts(
        "D2. Aurrezki-kutxa",
        "Ikasleak astelehenero 5 € sartzen ditu kutxan, 80 € lortu arte. Programak asteak zenbatzen ditu eta aste bakoitzean kutxan zenbat dagoen erakusten du. Helburura iristean «Helburua lortuta!» idatzi.",
        example="Astea 1: 5 €\nAstea 2: 10 €\n…\nHelburua lortuta! Asteak: 16",
    )
    d3 = exercise_parts(
        "D3. Ordutegia – 5 egun × 6 eskola-ordu",
        "Astean 5 egunetan, egun bakoitzean 6 eskola-ordu daude. Programa batek egun bakoitzerako («Astelehena», «Asteartea»…) 1etik 6ra orduak zerrendatuko ditu.",
        example="=== Astelehena ===\n  Ordua 1\n  Ordua 2\n  …\n=== Asteartea ===\n  Ordua 1\n  …",
    )
    d4 = exercise_parts(
        "D4. Pasahitza + 3 saiakera",
        "C1 bezala, baina gehienez 3 saiakera daude. Asmatzen badu: «Ongi etorri!». 3 aldiz huts egiten badu: «Blokeatuta. Joan irakaslearengana.».",
    )
    story.append(two_col(d1 + [Spacer(1, 4)] + d3, d2 + [Spacer(1, 4)] + d4))
    story.append(Spacer(1, 8))
    story.append(
        P(
            "Izarraitz Lanbide Heziketa · Pseint · Bukleak (PARA / MIENTRAS / REPETIR)",
            "foot",
        )
    )
    return story


def main():
    outs = [
        "/workspace/bukleak-bizitza-erreala/Bukleak_bizitza_errealean_ariketak.pdf",
        "/opt/cursor/artifacts/Bukleak_bizitza_errealean_ariketak_izarraitz.pdf",
    ]
    for out in outs:
        doc = SimpleDocTemplate(
            out,
            pagesize=PAGE,
            leftMargin=MARGIN,
            rightMargin=MARGIN,
            topMargin=0.85 * cm,
            bottomMargin=0.85 * cm,
        )
        doc.build(build_story())
        print("OK", out, os.path.getsize(out))


if __name__ == "__main__":
    main()
