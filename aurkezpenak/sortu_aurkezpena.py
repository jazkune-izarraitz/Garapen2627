#!/usr/bin/env python3
"""DBH ikasleen harrera-aurkezpena — Oñati Institutua 2026-2027."""

from pathlib import Path

from reportlab.lib.colors import Color, HexColor, white, black
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = Path(__file__).resolve().parent / "DBH_Ikasleen_Harrera_Aurkezpena_2026-2027.pdf"
ASSETS = Path(__file__).resolve().parent / "assets"

# Widescreen slide
W, H = 338 * mm, 190 * mm  # ~16:9

# Palette — ikastetxeko urdin-berdexka + atmosfera leuna
TEAL = HexColor("#3A9BB5")
TEAL_DEEP = HexColor("#1F6F86")
TEAL_DARK = HexColor("#0E3D4C")
INK = HexColor("#1A2A30")
MUTED = HexColor("#5A6E76")
SOFT = HexColor("#E8F4F7")
SOFT2 = HexColor("#F3FAFB")
ACCENT = HexColor("#E07A3D")  # laranja leuna, ez terrakota
LINE = HexColor("#B7D5DE")
OK = HexColor("#2E8B6A")

pdfmetrics.registerFont(TTFont("Yrsa", "/usr/share/fonts/truetype/fonts-yrsa-rasa/Yrsa-Regular.ttf"))
pdfmetrics.registerFont(TTFont("YrsaBold", "/usr/share/fonts/truetype/fonts-yrsa-rasa/Yrsa-Bold.ttf"))
pdfmetrics.registerFont(TTFont("YrsaMed", "/usr/share/fonts/truetype/fonts-yrsa-rasa/Yrsa-Medium.ttf"))
pdfmetrics.registerFont(TTFont("Mont", "/usr/share/fonts/truetype/montserrat/Montserrat-Regular.ttf"))
pdfmetrics.registerFont(TTFont("MontMed", "/usr/share/fonts/truetype/montserrat/Montserrat-Medium.ttf"))
pdfmetrics.registerFont(TTFont("MontSemi", "/usr/share/fonts/truetype/montserrat/Montserrat-SemiBold.ttf"))
pdfmetrics.registerFont(TTFont("MontBold", "/usr/share/fonts/truetype/montserrat/Montserrat-Bold.ttf"))
pdfmetrics.registerFont(TTFont("MontLight", "/usr/share/fonts/truetype/montserrat/Montserrat-Light.ttf"))


def bg_atmosphere(c: canvas.Canvas):
    """Atzealde gradiente leuna + uhinen patroi fina."""
    steps = 40
    for i in range(steps):
        t = i / (steps - 1)
        r = 0.95 + 0.02 * (1 - t)
        g = 0.97 + 0.01 * t
        b = 0.98
        c.setFillColor(Color(r, g, b))
        y0 = H * (1 - (i + 1) / steps)
        c.rect(0, y0, W, H / steps + 1, fill=1, stroke=0)
    # ezkerreko banda
    c.setFillColor(TEAL_DARK)
    c.rect(0, 0, 8 * mm, H, fill=1, stroke=0)
    # goiko uhin-lerroak
    c.setStrokeColor(Color(0.45, 0.68, 0.76, alpha=0.25))
    c.setLineWidth(1.2)
    for i, y in enumerate([H - 12 * mm, H - 16 * mm, H - 20 * mm]):
        c.setDash(2 + i, 4)
        c.line(18 * mm, y, W - 12 * mm, y)
    c.setDash()


def footer(c: canvas.Canvas, page: int, total: int):
    c.setFillColor(MUTED)
    c.setFont("Mont", 8)
    c.drawString(18 * mm, 7 * mm, "Oñati Institutua · DBH · 2026-2027")
    c.drawRightString(W - 12 * mm, 7 * mm, f"{page} / {total}")
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    c.line(18 * mm, 11 * mm, W - 12 * mm, 11 * mm)


def title_block(c: canvas.Canvas, title: str, subtitle: str | None = None):
    c.setFillColor(TEAL_DARK)
    c.setFont("YrsaBold", 28)
    c.drawString(18 * mm, H - 22 * mm, title)
    if subtitle:
        c.setFillColor(TEAL_DEEP)
        c.setFont("MontMed", 11)
        c.drawString(18 * mm, H - 30 * mm, subtitle)
    c.setStrokeColor(TEAL)
    c.setLineWidth(2.5)
    c.line(18 * mm, H - 34 * mm, 55 * mm, H - 34 * mm)


def bullet(c: canvas.Canvas, x, y, text, max_w, size=10.5, color=INK, leading=None):
    leading = leading or size + 4
    c.setFillColor(TEAL)
    c.circle(x + 1.6 * mm, y + 1.2 * mm, 1.1 * mm, fill=1, stroke=0)
    c.setFillColor(color)
    c.setFont("Mont", size)
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if c.stringWidth(trial, "Mont", size) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    for i, line in enumerate(lines):
        c.drawString(x + 5 * mm, y - i * leading, line)
    return len(lines) * leading


def card(c: canvas.Canvas, x, y, w, h, fill=SOFT2):
    c.setFillColor(fill)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, 4 * mm, fill=1, stroke=1)


def section_label(c: canvas.Canvas, x, y, text):
    c.setFillColor(TEAL)
    c.setFont("MontSemi", 9)
    c.drawString(x, y, text.upper())


# ─── SLIDES ───────────────────────────────────────────────────────────

def slide_cover(c: canvas.Canvas):
    # Hero full-bleed atmosphere
    for i in range(50):
        t = i / 49
        c.setFillColor(Color(0.06 + 0.08 * t, 0.28 + 0.18 * t, 0.34 + 0.20 * t))
        c.rect(0, H * (1 - (i + 1) / 50), W, H / 50 + 1, fill=1, stroke=0)

    # Decorative arcs
    c.setStrokeColor(Color(0.45, 0.75, 0.85, alpha=0.35))
    c.setLineWidth(1.5)
    for r in (40, 55, 70):
        c.circle(W - 30 * mm, 25 * mm, r * mm, fill=0, stroke=1)

    # Brand
    c.setFillColor(TEAL)
    c.setFont("MontSemi", 12)
    c.drawString(22 * mm, H - 28 * mm, "OÑATI INSTITUTUA")
    c.setStrokeColor(TEAL)
    c.setLineWidth(1)
    c.line(22 * mm, H - 31 * mm, 78 * mm, H - 31 * mm)

    c.setFillColor(white)
    c.setFont("YrsaBold", 46)
    c.drawString(22 * mm, H - 55 * mm, "Ikasleen Harrera")
    c.drawString(22 * mm, H - 72 * mm, "Aurkezpena")

    c.setFillColor(Color(0.85, 0.93, 0.96))
    c.setFont("MontLight", 16)
    c.drawString(22 * mm, H - 88 * mm, "DBH · 2026-2027 ikasturtea")

    c.setFillColor(white)
    c.setFont("Mont", 11)
    c.drawString(22 * mm, 38 * mm, "Guztiona, guztion artean")

    # Photos strip
    img1 = ASSETS / "eraikina_1.png"
    img2 = ASSETS / "eraikina_2.png"
    if img1.exists():
        c.drawImage(str(img1), W - 145 * mm, 28 * mm, width=78 * mm, height=73 * mm,
                    preserveAspectRatio=True, anchor="c", mask="auto")
    if img2.exists():
        c.drawImage(str(img2), W - 62 * mm, 28 * mm, width=42 * mm, height=73 * mm,
                    preserveAspectRatio=True, anchor="c", mask="auto")

    # Accent bar
    c.setFillColor(TEAL)
    c.rect(0, 0, W, 10 * mm, fill=1, stroke=0)
    c.setFillColor(TEAL_DARK)
    c.setFont("Mont", 8)
    c.drawCentredString(W / 2, 3.5 * mm, "Zuazola egoitza · Unibertsitate Etorbidea 6 · 20560 Oñati")


def slide_aurkibidea(c: canvas.Canvas):
    bg_atmosphere(c)
    title_block(c, "Zer ikusiko dugu?", "Aurkibidea")
    items = [
        ("01", "Oñati Institutua eta gure balioak"),
        ("02", "Non gaude: Zuazola eta kontaktoak"),
        ("03", "Eguneroko ordutegia"),
        ("04", "Ebaluazio egutegia"),
        ("05", "Eskubideak eta betebeharrak"),
        ("06", "Bizikidetza arauak"),
        ("07", "Tresna digitalak"),
        ("08", "Segurtasuna eta ebakuazioa"),
    ]
    cols = 2
    for i, (num, label) in enumerate(items):
        col = i % cols
        row = i // cols
        x = 18 * mm + col * 155 * mm
        y = H - 55 * mm - row * 28 * mm
        card(c, x, y - 8 * mm, 145 * mm, 24 * mm)
        c.setFillColor(TEAL_DEEP)
        c.setFont("YrsaBold", 22)
        c.drawString(x + 6 * mm, y + 2 * mm, num)
        c.setFillColor(INK)
        c.setFont("MontMed", 12)
        c.drawString(x + 28 * mm, y + 3 * mm, label)


def slide_institutua(c: canvas.Canvas):
    bg_atmosphere(c)
    title_block(c, "Oñati Institutua", "Ongi etorri!")
    c.setFillColor(INK)
    c.setFont("Mont", 12)
    text = (
        "Ikaslea bere bizitza pertsonal, sozial, akademiko eta laboralerako "
        "prestatzea, kalitatezko hezkuntza euskalduna eta publikoa eskainiz."
    )
    # wrap
    max_w = W - 36 * mm
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if c.stringWidth(trial, "Mont", 12) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    y = H - 48 * mm
    for line in lines:
        c.drawString(18 * mm, y, line)
        y -= 6 * mm

    c.setFillColor(MUTED)
    c.setFont("MontMed", 10)
    c.drawString(18 * mm, y - 4 * mm, "Bi egoitza:")
    # Two campus cards
    card(c, 18 * mm, 42 * mm, 145 * mm, 72 * mm, SOFT)
    card(c, 175 * mm, 42 * mm, 145 * mm, 72 * mm, SOFT)
    c.setFillColor(TEAL_DEEP)
    c.setFont("YrsaBold", 18)
    c.drawString(26 * mm, 98 * mm, "Zuazola")
    c.drawString(183 * mm, 98 * mm, "Larraña")
    c.setFillColor(INK)
    c.setFont("Mont", 10)
    for i, t in enumerate(["DBH", "ZIG", "Batxilergoa"]):
        c.drawString(26 * mm, 85 * mm - i * 8 * mm, "•  " + t)
    for i, t in enumerate(["Oinarrizko Heziketa Zikloa", "Erdi / Goi Mailako Zikloak", "Hezkuntza ez arautua"]):
        c.drawString(183 * mm, 85 * mm - i * 8 * mm, "•  " + t)
    c.setFillColor(TEAL)
    c.setFont("MontSemi", 9)
    c.drawString(26 * mm, 52 * mm, "ZURE EGOITZA")


def slide_balioak(c: canvas.Canvas):
    bg_atmosphere(c)
    title_block(c, "Gure balioak", "Zer gara eta zer nahi dugu")
    vals = [
        ("Euskalduna eta eleanitza", "Euskara erdigunean; dokumentuak euskaraz."),
        ("Jasangarritasuna", "EA2030 eta hondakinen bilketa selektiboa."),
        ("Bizikidetza eta hezkidetza", "Errespetua, berdintasuna eta elkarlana."),
        ("Berrikuntza eta sormena", "Ikaslearen garapen integralerako bideak."),
    ]
    for i, (t, d) in enumerate(vals):
        col = i % 2
        row = i // 2
        x = 18 * mm + col * 155 * mm
        y = H - 52 * mm - row * 55 * mm
        card(c, x, y - 38 * mm, 145 * mm, 48 * mm)
        c.setFillColor(TEAL)
        c.circle(x + 12 * mm, y - 5 * mm, 5 * mm, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("MontBold", 11)
        c.drawCentredString(x + 12 * mm, y - 7 * mm, str(i + 1))
        c.setFillColor(TEAL_DARK)
        c.setFont("YrsaBold", 16)
        c.drawString(x + 24 * mm, y - 5 * mm, t)
        c.setFillColor(MUTED)
        c.setFont("Mont", 10)
        c.drawString(x + 24 * mm, y - 18 * mm, d)


def slide_kontaktua(c: canvas.Canvas):
    bg_atmosphere(c)
    title_block(c, "Zuazola egoitza", "Non gaude eta nola harremanetan jarri")
    card(c, 18 * mm, 55 * mm, 190 * mm, 90 * mm)
    rows = [
        ("Helbidea", "Unibertsitate Etorbidea 6, 20560 Oñati"),
        ("Telefonoa", "943 89 92 98"),
        ("Emaila", "013015ac@hezkuntza.net"),
        ("Webgunea", "www.onati.net"),
    ]
    y = H - 52 * mm
    for label, val in rows:
        c.setFillColor(TEAL_DEEP)
        c.setFont("MontSemi", 9)
        c.drawString(28 * mm, y, label.upper())
        c.setFillColor(INK)
        c.setFont("MontMed", 14)
        c.drawString(28 * mm, y - 7 * mm, val)
        y -= 20 * mm

    card(c, 220 * mm, 55 * mm, 100 * mm, 90 * mm, HexColor("#D6EEF4"))
    c.setFillColor(TEAL_DARK)
    c.setFont("YrsaBold", 15)
    c.drawString(230 * mm, 128 * mm, "Gogoratu")
    tips = [
        "Tutoreari idatzi eInikaren bidez.",
        "Pasahitzak ondo gorde.",
        "Wifi eta sare datuak koadernoan idatzi.",
        "Familiei berri emateko bidea: eInika.",
    ]
    y = 112 * mm
    for t in tips:
        h = bullet(c, 228 * mm, y, t, 82 * mm, size=9, color=INK)
        y -= h + 3 * mm


def slide_ordutegia(c: canvas.Canvas):
    bg_atmosphere(c)
    title_block(c, "Eguneroko ordutegia", "DBH eta ZIG")
    sessions = [
        ("1. saioa", "8:00 – 8:55"),
        ("2. saioa", "8:55 – 9:50"),
        ("3. saioa", "9:50 – 10:45"),
        ("Jolastordua", "10:45 – 11:15"),
        ("4. saioa", "11:15 – 12:10"),
        ("5. saioa", "12:10 – 13:05"),
        ("6. saioa", "13:05 – 14:00"),
        ("HEZI+", "15:00 – 16:30"),
    ]
    x0, y0 = 18 * mm, H - 48 * mm
    col_w = 75 * mm
    for i, (name, time) in enumerate(sessions):
        col = i % 4
        row = i // 4
        x = x0 + col * (col_w + 5 * mm)
        y = y0 - row * 48 * mm
        is_break = name in ("Jolastordua", "HEZI+")
        card(c, x, y - 32 * mm, col_w, 38 * mm, HexColor("#FFF3E8") if is_break else SOFT)
        c.setFillColor(ACCENT if is_break else TEAL_DEEP)
        c.setFont("MontSemi", 9)
        c.drawString(x + 5 * mm, y - 2 * mm, name.upper())
        c.setFillColor(INK)
        c.setFont("YrsaBold", 18)
        c.drawString(x + 5 * mm, y - 16 * mm, time)

    c.setFillColor(MUTED)
    c.setFont("Mont", 9)
    c.drawString(18 * mm, 22 * mm, "Txirrinak jotzean gelan egon behar duzu. Puntualtasuna oinarrizkoa da.")


def slide_ebaluazioa(c: canvas.Canvas):
    bg_atmosphere(c)
    title_block(c, "Ebaluazio egutegia", "DBH eta ZIG · 2026-2027")
    headers = ["Ebaluazioa", "Iraupena", "Azterketak", "Notak"]
    rows = [
        ["1. ebaluazioa", "Ira. 7 – Aza. 27", "Aza. 19 – 30", "Abe. 3 (ikasleei)\nAbe. 4 (Inika)"],
        ["2. ebaluazioa", "Aza. 30 – Mar. 5", "Mar. 1 – 8", "Mar. 12 (ikasleei)\nMar. 15 (Inika)"],
        ["Ohikoa", "Mar. 8 – Eka. 18", "Eka. 1 – 11", "Eka. 18\nErrekl.: Eka. 18, 21"],
    ]
    x0 = 18 * mm
    widths = [42 * mm, 55 * mm, 50 * mm, 70 * mm]
    y = H - 48 * mm
    # header
    c.setFillColor(TEAL_DARK)
    c.roundRect(x0, y - 4 * mm, sum(widths) + 6 * mm, 12 * mm, 2 * mm, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("MontSemi", 9)
    x = x0 + 3 * mm
    for h, w in zip(headers, widths):
        c.drawString(x, y, h.upper())
        x += w
    y -= 18 * mm
    for ri, row in enumerate(rows):
        bg = SOFT if ri % 2 == 0 else SOFT2
        card(c, x0, y - 18 * mm, sum(widths) + 6 * mm, 28 * mm, bg)
        x = x0 + 3 * mm
        for ci, (cell, w) in enumerate(zip(row, widths)):
            c.setFillColor(TEAL_DARK if ci == 0 else INK)
            c.setFont("MontSemi" if ci == 0 else "Mont", 9 if "\n" in cell else 10)
            parts = cell.split("\n")
            for pi, p in enumerate(parts):
                c.drawString(x, y - 2 * mm - pi * 5 * mm, p)
            x += w
        y -= 32 * mm

    card(c, 18 * mm, 20 * mm, W - 30 * mm, 22 * mm, HexColor("#FFF3E8"))
    c.setFillColor(ACCENT)
    c.setFont("MontSemi", 9)
    c.drawString(24 * mm, 32 * mm, "DATA GARRANTZITSUAK")
    c.setFillColor(INK)
    c.setFont("Mont", 10)
    c.drawString(24 * mm, 24 * mm, "Kurtso hasiera: irailak 7  ·  Gabonak: abe. 24 – ura. 6  ·  Aste Santua: mar. 25 – api. 4  ·  Amaiera: ekainak 18")


def slide_eskubideak(c: canvas.Canvas):
    bg_atmosphere(c)
    title_block(c, "Zure eskubideak", "201/2008 Dekretua — laburpena")
    left = [
        "Hezkuntza integrala jasotzea",
        "Balorazio akademiko objektiboa",
        "Orientazio akademiko eta lanbidekoa",
        "Osotasuna, nortasuna eta duintasuna",
        "Kontzientzia-askatasuna",
        "Biltzeko eta adierazteko askatasuna",
    ]
    right = [
        "Elkartzeko eskubidea",
        "Parte hartzeko eskubidea",
        "Informazioa eskuratzea",
        "Aukera-berdintasuna",
        "Gizarte-babesa",
        "Eskubideak errespetatuak izatea",
    ]
    y = H - 48 * mm
    for t in left:
        used = bullet(c, 18 * mm, y, t, 140 * mm, size=11)
        y -= used + 4 * mm
    y = H - 48 * mm
    for t in right:
        used = bullet(c, 175 * mm, y, t, 140 * mm, size=11)
        y -= used + 4 * mm


def slide_betebeharrak(c: canvas.Canvas):
    bg_atmosphere(c)
    title_block(c, "Zure betebeharrak", "Eskolak ondo funtzionatzeko oinarriak")
    items = [
        ("Ikasi", "Ikasteko eta lanak egiteko konpromisoa."),
        ("Parte hartu", "Prestakuntza-jardueretan eta klasean."),
        ("Bertaratu", "Egunero eta puntualtasunez etorri."),
        ("Bizikidetza", "Elkarri errespetua eta giro ona zaindu."),
        ("Arauak", "Eskola-arauak eta instalazioak errespetatu."),
        ("Askatasuna", "Bestenen kontzientzia eta iritziak errespetatu."),
    ]
    for i, (t, d) in enumerate(items):
        col = i % 3
        row = i // 3
        x = 18 * mm + col * 103 * mm
        y = H - 50 * mm - row * 55 * mm
        card(c, x, y - 38 * mm, 96 * mm, 48 * mm)
        c.setFillColor(TEAL_DEEP)
        c.setFont("YrsaBold", 16)
        c.drawString(x + 6 * mm, y - 5 * mm, t)
        c.setFillColor(MUTED)
        c.setFont("Mont", 10)
        # wrap
        words = d.split()
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if c.stringWidth(trial, "Mont", 10) <= 84 * mm:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        yy = y - 18 * mm
        for line in lines:
            c.drawString(x + 6 * mm, yy, line)
            yy -= 5 * mm


def slide_arauak(c: canvas.Canvas):
    bg_atmosphere(c)
    title_block(c, "Bizikidetza arauak", "Garrantzitsuenak — Zuazola")
    rules = [
        ("Mugikorra", "Ikastetxean ezin da piztuta eduki (gelan, patioan eta atarian ere ez). Atzemanez gero, ikasketa-buruari emango zaio eta familiari idatziko zaio."),
        ("Pasilloak", "Klase orduetan ezin da pasilloetan egon. Txirrinak jotzean gelan egon."),
        ("Substantziak", "Tabakoa, alkohola edo drogarik ez. Debekatuta dago."),
        ("Garbitasuna", "Eskola-eremua garbi mantendu; zikintzen baduzu, garbitu."),
        ("Irteerak", "Irteeretarako baimena derrigorrezkoa da; bestela ez zara joango."),
        ("Puntualtasuna", "3 berandutze → jokabide desegokiaren txostena Inikan."),
    ]
    for i, (t, d) in enumerate(rules):
        col = i % 2
        row = i // 2
        x = 18 * mm + col * 155 * mm
        y = H - 48 * mm - row * 38 * mm
        c.setFillColor(TEAL if i != 0 else ACCENT)
        c.roundRect(x, y - 22 * mm, 3 * mm, 28 * mm, 1 * mm, fill=1, stroke=0)
        c.setFillColor(TEAL_DARK if i != 0 else HexColor("#9A4A1A"))
        c.setFont("MontSemi", 11)
        c.drawString(x + 8 * mm, y, t)
        c.setFillColor(MUTED)
        c.setFont("Mont", 8.5)
        words = d.split()
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if c.stringWidth(trial, "Mont", 8.5) <= 138 * mm:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        yy = y - 8 * mm
        for line in lines[:3]:
            c.drawString(x + 8 * mm, yy, line)
            yy -= 4.2 * mm


def slide_gela(c: canvas.Canvas):
    bg_atmosphere(c)
    title_block(c, "Gelan nola jokatu", "Oinarrizko jarrerak")
    left = [
        "Zure tokian eserita egon (irakasleak esan ezean).",
        "Hitz egiteko ordena errespetatu; eskua jaso.",
        "Azalpena amaitu arte itxaron galdetzeko.",
        "Arreta mantendu; ez oztopatu besteak.",
        "Materiala ekarri; eragina izan dezake notan.",
        "Gelan ezin da jan.",
    ]
    right = [
        "Klase amaieran: mahaiak txukun, leihoak itxita, argiak itzalita.",
        "Jarrera desegokia: 1) ohartarazpena, 2) 5 min pasillora, 3) kaleratzea.",
        "Kaleratzean: zaintzako irakaslearengana lanarekin.",
        "Jolastorduan gelak itxita; ezin da gelan geratu.",
        "Liburutegian: isilik, ez jan.",
        "HEZI+ (15:00–16:30): errespetua eta isiltasuna.",
    ]
    section_label(c, 18 * mm, H - 45 * mm, "Egunerokoa")
    section_label(c, 175 * mm, H - 45 * mm, "Ondorioak eta espazioak")
    y = H - 55 * mm
    for t in left:
        used = bullet(c, 18 * mm, y, t, 140 * mm, size=10)
        y -= used + 3 * mm
    y = H - 55 * mm
    for t in right:
        used = bullet(c, 175 * mm, y, t, 140 * mm, size=10)
        y -= used + 3 * mm


def slide_digitala(c: canvas.Canvas):
    bg_atmosphere(c)
    title_block(c, "Tresna digitalak", "Zure kontuak eta komunikazioa")
    tools = [
        ("eInika", "www.onati.net", "Notak, hutsegiteak, oharrak eta familiaren komunikazioa."),
        ("Ikastetxeko emaila", "Hezkuntza", "Komunikazio ofiziala eta lanerako tresnak."),
        ("Sarea / Wifi", "Ordenagailuak", "Sarbidea ikasgelako ordenagailuetan."),
        ("XLNET", "Aplikazioak", "Hezkuntza Sailaren aplikazioetarako sarrera."),
    ]
    for i, (name, tag, desc) in enumerate(tools):
        x = 18 * mm + (i % 2) * 155 * mm
        y = H - 52 * mm - (i // 2) * 55 * mm
        card(c, x, y - 38 * mm, 145 * mm, 48 * mm)
        c.setFillColor(TEAL)
        c.setFont("MontSemi", 8)
        c.drawString(x + 8 * mm, y - 2 * mm, tag.upper())
        c.setFillColor(TEAL_DARK)
        c.setFont("YrsaBold", 18)
        c.drawString(x + 8 * mm, y - 14 * mm, name)
        c.setFillColor(MUTED)
        c.setFont("Mont", 10)
        c.drawString(x + 8 * mm, y - 26 * mm, desc)

    c.setFillColor(MUTED)
    c.setFont("Mont", 9)
    c.drawString(18 * mm, 22 * mm, "Pasahitzak koadernoan idatzi eta ez partekatu. Arazo teknikoak: irakasleari edo IKT arduradunari.")


def slide_ebakuazioa(c: canvas.Canvas):
    bg_atmosphere(c)
    title_block(c, "Ebakuazioa", "Zer egin alarma jotzen duenean")
    # Signal
    card(c, 18 * mm, H - 78 * mm, 100 * mm, 38 * mm, HexColor("#FFE8E0"))
    c.setFillColor(ACCENT)
    c.setFont("MontSemi", 9)
    c.drawString(26 * mm, H - 50 * mm, "ALARMA-SEINALEA")
    c.setFillColor(INK)
    c.setFont("YrsaBold", 20)
    c.drawString(26 * mm, H - 64 * mm, "3 txirrin × 3 aldiz")

    steps = [
        "Lasai egon; gauzak dauden lekuan utzi.",
        "Irakaslearen esanetara jarri.",
        "Leihoak itxi, argiak itzali; ilaran jarri.",
        "Aurrekoari jarraitu; ez bueltatu atzera.",
        "Ez egin korrika; paretatik hurbil joan.",
        "Elkargunean irakaslearen ondoan geratu (zenbaketa).",
    ]
    y = H - 50 * mm
    for i, t in enumerate(steps):
        c.setFillColor(TEAL_DEEP)
        c.circle(135 * mm, y + 1.5 * mm, 4 * mm, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("MontBold", 9)
        c.drawCentredString(135 * mm, y, str(i + 1))
        c.setFillColor(INK)
        c.setFont("Mont", 11)
        c.drawString(143 * mm, y, t)
        y -= 14 * mm

    c.setFillColor(MUTED)
    c.setFont("Mont", 9)
    c.drawString(18 * mm, 22 * mm, "Istripua: BABESTU → JAKINARAZI (Zuzendaritza / 112) → LAGUNDU.  Sua: abisatu, ateak itxi, aginduak bete.")


def slide_amaiera(c: canvas.Canvas):
    for i in range(50):
        t = i / 49
        c.setFillColor(Color(0.06 + 0.08 * t, 0.28 + 0.18 * t, 0.34 + 0.20 * t))
        c.rect(0, H * (1 - (i + 1) / 50), W, H / 50 + 1, fill=1, stroke=0)

    c.setFillColor(TEAL)
    c.setFont("MontSemi", 12)
    c.drawCentredString(W / 2, H - 40 * mm, "OÑATI INSTITUTUA")

    c.setFillColor(white)
    c.setFont("YrsaBold", 40)
    c.drawCentredString(W / 2, H - 65 * mm, "Guztiona, guztion artean")

    c.setFillColor(Color(0.85, 0.93, 0.96))
    c.setFont("MontLight", 14)
    c.drawCentredString(W / 2, H - 82 * mm, "Ikasturte ona izan dezazuela!")

    c.setFillColor(white)
    c.setFont("Mont", 11)
    c.drawCentredString(W / 2, 55 * mm, "www.onati.net  ·  943 89 92 98  ·  Zuazola")
    c.setFont("Mont", 10)
    c.drawCentredString(W / 2, 42 * mm, "DBH Ikasleen Harrera · 2026-2027")

    c.setFillColor(TEAL)
    c.rect(0, 0, W, 10 * mm, fill=1, stroke=0)


def main():
    slides = [
        slide_cover,
        slide_aurkibidea,
        slide_institutua,
        slide_balioak,
        slide_kontaktua,
        slide_ordutegia,
        slide_ebaluazioa,
        slide_eskubideak,
        slide_betebeharrak,
        slide_arauak,
        slide_gela,
        slide_digitala,
        slide_ebakuazioa,
        slide_amaiera,
    ]
    c = canvas.Canvas(str(OUT), pagesize=(W, H))
    c.setTitle("DBH Ikasleen Harrera Aurkezpena 2026-2027 — Oñati Institutua")
    c.setAuthor("Oñati Institutua")
    total = len(slides)
    for i, fn in enumerate(slides, 1):
        fn(c)
        if fn not in (slide_cover, slide_amaiera):
            footer(c, i, total)
        c.showPage()
    c.save()
    print(f"Created: {OUT}")


if __name__ == "__main__":
    main()
