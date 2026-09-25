#!/usr/bin/env python3
"""ZiberIT metadatuak – ikasleen aurkezpena (PPTX)."""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt, Emu

OUT = Path(__file__).resolve().parent / "ziberit-metadatuak-ikasleak.pptx"

# Koloreak (ez morea / cream AI-look)
BG = RGBColor(0x0F, 0x1C, 0x2E)       # navy iluna
CARD = RGBColor(0x1A, 0x2F, 0x45)
ACCENT = RGBColor(0xE8, 0xA8, 0x38)   # amber
TEXT = RGBColor(0xF2, 0xF0, 0xEA)
MUTED = RGBColor(0xA8, 0xB4, 0xC0)
CODE_BG = RGBColor(0x0A, 0x14, 0x22)
CODE = RGBColor(0x7D, 0xDA, 0xA5)     # berde argia


def set_slide_bg(slide, color: RGBColor) -> None:
    fill = slide.shapes.add_shape(
        1,  # rectangle
        Inches(0),
        Inches(0),
        Inches(13.333),
        Inches(7.5),
    )
    fill.fill.solid()
    fill.fill.fore_color.rgb = color
    fill.line.fill.background()
    # atzean utzi
    spTree = slide.shapes._spTree
    sp = fill._element
    spTree.remove(sp)
    spTree.insert(2, sp)


def add_text(slide, left, top, width, height, text, size=18, bold=False, color=TEXT, align=PP_ALIGN.LEFT, font="Calibri"):
    box = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(size)
    p.font.bold = bold
    p.font.color.rgb = color
    p.font.name = font
    p.alignment = align
    return box


def add_bullets(slide, left, top, width, height, items, size=16, color=TEXT):
    box = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"•  {item}"
        p.font.size = Pt(size)
        p.font.color.rgb = color
        p.font.name = "Calibri"
        p.space_after = Pt(8)
    return box


def add_code(slide, left, top, width, height, lines):
    # atzeko laukia
    shape = slide.shapes.add_shape(1, Inches(left), Inches(top), Inches(width), Inches(height))
    shape.fill.solid()
    shape.fill.fore_color.rgb = CODE_BG
    shape.line.color.rgb = RGBColor(0x2A, 0x40, 0x58)

    box = slide.shapes.add_textbox(
        Inches(left) + Inches(0.15),
        Inches(top) + Inches(0.12),
        Inches(width) - Inches(0.3),
        Inches(height) - Inches(0.2),
    )
    tf = box.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line
        p.font.size = Pt(13)
        p.font.name = "Consolas"
        p.font.color.rgb = CODE
        p.space_after = Pt(4)
    return box


def title_bar(slide, title: str, subtitle: str | None = None) -> None:
    add_text(slide, 0.5, 0.25, 12, 0.5, title, size=28, bold=True, color=ACCENT)
    if subtitle:
        add_text(slide, 0.5, 0.75, 12, 0.4, subtitle, size=14, color=MUTED)
    # lerro
    line = slide.shapes.add_shape(1, Inches(0.5), Inches(1.15), Inches(12.3), Inches(0.03))
    line.fill.solid()
    line.fill.fore_color.rgb = ACCENT
    line.line.fill.background()


def new_slide(prs: Presentation):
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
    set_slide_bg(slide, BG)
    return slide


def build() -> Path:
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # 1 – Azala
    s = new_slide(prs)
    add_text(s, 0.8, 2.0, 11.5, 1, "ZiberIT – Metadatuen analisia", size=40, bold=True, color=ACCENT)
    add_text(s, 0.8, 3.1, 11.5, 0.5, "Web fitxategiak jeitsi eta EXIF / PDF metadatuak aztertu", size=20, color=TEXT)
    add_text(s, 0.8, 4.0, 11.5, 0.4, "HE – Ezagutzea / OSINT oinarriak  ·  Ikasleen gida", size=16, color=MUTED)
    add_text(s, 0.8, 6.5, 11.5, 0.4, "fpcloud.izarraitz.eus  ·  Arp Kali + Ubuntu ziberit.org", size=14, color=MUTED)

    # 2 – Helburua
    s = new_slide(prs)
    title_bar(s, "1. Jardueraren helburua", "Zer egin behar duzu?")
    add_bullets(
        s,
        0.6,
        1.5,
        12,
        5,
        [
            "http://ziberit.org webgunetik ahalik eta fitxategi gehien lortu",
            "Direktorio ezkutuak bilatu (gobuster + hiztegia)",
            "Fitxategiak jeitsi karpeta bakarrean (wget)",
            "Metadatuak atera (exiftool): JPG → GPS, PDF → Author",
            "Hiru emaitza igo: lokalizazioak, autore bakarrak, fitxategi-zerrenda",
        ],
        size=18,
    )

    # 3 – Ingurunea
    s = new_slide(prs)
    title_bar(s, "2. Laborategiko ingurunea", "Bi makina, sarea berezia")
    add_bullets(
        s,
        0.6,
        1.5,
        6,
        4,
        [
            "Arp Kali → erasotzailea / ikaslearen makina",
            "Ubuntu ziberit → helburua (webgunea)",
            "Sarea: 10.10.10.0/24 (personal2)",
            "Helburua: 10.10.10.12 = ziberit.org",
        ],
        size=17,
    )
    add_code(
        s,
        7.0,
        1.6,
        5.5,
        3.5,
        [
            "# Kali-n egiaztatu",
            "ip -br a",
            "",
            "# 10.10.10.x ikusi behar duzu",
            "# (eth1 / eth2...)",
            "",
            "ping -c 2 10.10.10.12",
        ],
    )

    # 4 – DNS kontzeptua
    s = new_slide(prs)
    title_bar(s, "3. DNS eta /etc/hosts", "Izenak → IP helbideak")
    add_bullets(
        s,
        0.6,
        1.5,
        12,
        2.2,
        [
            "DNS: izen bat (ziberit.org) IP bihurtzen du (10.10.10.12)",
            "Laborategian DNS berezia erabiliko dugu: 10.10.10.9",
            "Ez badabil: /etc/hosts fitxategian eskuz lotu izena eta IPa",
            "Zergatik? Nabigatzaileak eta tresnek http://ziberit.org erabiltzeko",
        ],
        size=17,
    )
    add_code(
        s,
        0.6,
        4.0,
        12,
        2.8,
        [
            "# Aukera A – DNS zerbitzaria",
            "echo 'nameserver 10.10.10.9' | sudo tee /etc/resolv.conf",
            "",
            "# Aukera B – hosts (DNS huts egiten badu)",
            "echo '10.10.10.12 ziberit.org' | sudo tee -a /etc/hosts",
            "",
            "ping -c 2 ziberit.org",
        ],
    )

    # 5 – Gobuster kontzeptua
    s = new_slide(prs)
    title_bar(s, "4. Direktorioak bilatu", "Zer da gobuster?")
    add_bullets(
        s,
        0.6,
        1.5,
        12,
        2.5,
        [
            "Webguneek karpeta ezkutuak izan ditzakete (/images, /docs…)",
            "gobuster: hiztegi bateko hitz bakoitza URL gisa probatzen du",
            "Erantzun interesgarriak: 200 (OK), 301/302 (berbideratu), 403…",
            "Hiztegia: directory-list-custom.txt (jarduerak emana)",
        ],
        size=17,
    )
    add_code(
        s,
        0.6,
        4.2,
        12,
        2.6,
        [
            "mkdir -p ~/ziberit-lab/emaitzak",
            "gobuster dir -u http://ziberit.org \\",
            "  -w ~/directory-list-custom.txt -t 30 \\",
            "  -o ~/ziberit-lab/emaitzak/gobuster.txt",
            "cat ~/ziberit-lab/emaitzak/gobuster.txt",
        ],
    )

    # 6 – Gobuster parametroak
    s = new_slide(prs)
    title_bar(s, "5. gobuster parametroak", "Zertarako balio du bakoitzak?")
    rows = [
        ("dir", "Direktorio/fitxategi bilaketa modua"),
        ("-u URL", "Helburuko webgunea"),
        ("-w fitxategia", "Hiztegia (probatu beharreko izenak)"),
        ("-t 30", "Hari paraleloak (abiadura)"),
        ("-o fitxategia", "Emaitzak fitxategian gorde"),
    ]
    y = 1.5
    for cmd, desc in rows:
        card = s.shapes.add_shape(1, Inches(0.6), Inches(y), Inches(12.1), Inches(0.7))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD
        card.line.fill.background()
        add_text(s, 0.85, y + 0.15, 3.5, 0.4, cmd, size=16, bold=True, color=CODE, font="Consolas")
        add_text(s, 4.5, y + 0.15, 7.8, 0.4, desc, size=16, color=TEXT)
        y += 0.85

    # 7 – wget
    s = new_slide(prs)
    title_bar(s, "6. Fitxategiak jeitsi – wget", "Deskargatu aurkitutako karpetak")
    add_bullets(
        s,
        0.6,
        1.5,
        12,
        2.0,
        [
            "wget: HTTP bidez fitxategiak deskargatzeko tresna",
            "Jarduerak: fitxategi guztiak karpeta bakarrean, azpidirektoriorik gabe",
            "Gobuster-ek topatutako bideak erabili (images, docs, download…)",
        ],
        size=17,
    )
    add_code(
        s,
        0.6,
        3.7,
        12,
        3.3,
        [
            "cd ~/ziberit-lab && mkdir -p fitxategiak",
            "wget -r -np -nH -P fitxategiak -A jpg,jpeg,pdf \\",
            "  http://ziberit.org/images/ \\",
            "  http://ziberit.org/docs/ \\",
            "  http://ziberit.org/download/",
            "# Lautu (azpidirektoriorik gabe):",
            "find fitxategiak -mindepth 2 -type f -exec mv -n {} fitxategiak/ \\;",
            "find fitxategiak -type d -empty -delete",
        ],
    )

    # 8 – wget flags
    s = new_slide(prs)
    title_bar(s, "7. wget aukerak", "Parametro bakoitzaren zentzua")
    rows = [
        ("-r", "Errekurtsiboki jeitsi (estekak / karpetak)"),
        ("-np", "Guraso-direktoriora ez igo (No Parent)"),
        ("-nH", "Host-izeneko karpeta ez sortu"),
        ("-P dir", "Helmuga-karpeta"),
        ("-A ext", "Luzapen iragazkia (jpg, pdf…)"),
    ]
    y = 1.5
    for cmd, desc in rows:
        card = s.shapes.add_shape(1, Inches(0.6), Inches(y), Inches(12.1), Inches(0.7))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD
        card.line.fill.background()
        add_text(s, 0.85, y + 0.15, 2.5, 0.4, cmd, size=16, bold=True, color=CODE, font="Consolas")
        add_text(s, 3.8, y + 0.15, 8.5, 0.4, desc, size=16, color=TEXT)
        y += 0.85

    # 9 – Metadatuak
    s = new_slide(prs)
    title_bar(s, "8. Zer dira metadatuak?", "Fitxategiaren “atzeko” informazioa")
    add_bullets(
        s,
        0.6,
        1.5,
        12,
        5,
        [
            "Metadatuak: fitxategian gordetako datuak, edukia bera ez direnak",
            "JPG (EXIF): kamera, data, eta batzuetan GPS kokapena",
            "PDF: egilea (Author), izenburua, softwarea…",
            "OSINT / forentsean baliagarriak: nork sortu duen, non atera den argazkia",
            "exiftool: metadatuak irakurri eta esportatzeko tresna estandarra",
        ],
        size=18,
    )

    # 10 – exiftool JPG
    s = new_slide(prs)
    title_bar(s, "9. JPG – geolokalizazioa", "GPS Latitude / Longitude / Position")
    add_bullets(
        s,
        0.6,
        1.5,
        12,
        1.8,
        [
            "Argazki batzuek GPS koordenatuak dituzte EXIF-ean",
            "Ikasleak: informazio hori fitxategi batean gorde (lokalizazioak.txt)",
            "Kontuz: -ext jpg eta -ext jpeg desberdinak dira",
        ],
        size=17,
    )
    add_code(
        s,
        0.6,
        3.6,
        12,
        3.2,
        [
            "cd ~/ziberit-lab",
            "exiftool -GPSLatitude -GPSLongitude -GPSPosition -csv \\",
            "  -ext jpg -ext jpeg fitxategiak/ \\",
            "  > emaitzak/lokalizazioak.txt",
            "",
            "cat emaitzak/lokalizazioak.txt",
        ],
    )

    # 11 – exiftool PDF
    s = new_slide(prs)
    title_bar(s, "10. PDF – Author bakarrak", "Errepikatu gabe")
    add_bullets(
        s,
        0.6,
        1.5,
        12,
        1.8,
        [
            "PDF bakoitzak Author eremu bat izan dezake",
            "Jarduerak: egile ezberdinak soilik (sort -u = unique)",
            "awk 'NF' → lerro hutsak kendu",
        ],
        size=17,
    )
    add_code(
        s,
        0.6,
        3.6,
        12,
        3.2,
        [
            "cd ~/ziberit-lab",
            "exiftool -q -p '$Author' -ext pdf fitxategiak/ \\",
            "  | awk 'NF' | sort -u \\",
            "  > emaitzak/autoreak.txt",
            "",
            "cat emaitzak/autoreak.txt",
        ],
    )

    # 12 – Bidali beharrekoa
    s = new_slide(prs)
    title_bar(s, "11. Zer igo behar da?", "Hiru fitxategi")
    items = [
        ("lokalizazioak.txt", "JPG-etako GPS metadatuak"),
        ("autoreak.txt", "PDF Author bakarrak (errepikatu gabe)"),
        ("fitxategi-zerrenda.txt", "wget-ek jeitsitako fitxategien zerrenda"),
    ]
    y = 1.6
    for name, desc in items:
        card = s.shapes.add_shape(1, Inches(1.5), Inches(y), Inches(10.3), Inches(1.1))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD
        card.line.fill.background()
        add_text(s, 1.8, y + 0.2, 9.5, 0.35, name, size=20, bold=True, color=ACCENT, font="Consolas")
        add_text(s, 1.8, y + 0.55, 9.5, 0.35, desc, size=16, color=TEXT)
        y += 1.35
    add_code(
        s,
        1.5,
        5.8,
        10.3,
        1.2,
        ["find fitxategiak -type f | sort > emaitzak/fitxategi-zerrenda.txt"],
    )

    # 13 – Fluxua
    s = new_slide(prs)
    title_bar(s, "12. Prozesu osoa", "Ordena gogoratu")
    steps = [
        "1  Sarea egiaztatu (10.10.10.x)",
        "2  DNS / hosts → ping ziberit.org",
        "3  gobuster + directory-list-custom.txt",
        "4  wget (images, docs, download…)",
        "5  Fitxategiak lautu karpeta bakarrean",
        "6  exiftool JPG → lokalizazioak.txt",
        "7  exiftool PDF → autoreak.txt (sort -u)",
        "8  Zerrenda sortu eta hiru fitxategiak igo",
    ]
    add_bullets(s, 0.8, 1.5, 11.5, 5.5, steps, size=18)

    # 14 – Oharrak
    s = new_slide(prs)
    title_bar(s, "13. Ohiko erroreak", "Zer begiratu trabatzen zarenean")
    add_bullets(
        s,
        0.6,
        1.5,
        12,
        5.5,
        [
            "ping ziberit.org huts → hosts edo DNS berrikusi",
            "gobuster-ek ezer ez → webgunea piztuta dago? curl http://ziberit.org/",
            "wget-ek jpg gutxi → -ext jpg (ez soilik jpeg)",
            "autoreak.txt zikin → erabili -q -p '$Author' eta awk 'NF'",
            "^ karakterea Isard-en → awk 'NF' erabili sed '/^$/d' ordez",
            "Makina berrabiarazi ondoren → IP eta nginx/web edukia egiaztatu",
        ],
        size=17,
    )

    # 15 – Amaiera
    s = new_slide(prs)
    add_text(s, 0.8, 2.5, 11.5, 0.8, "Galderarik?", size=40, bold=True, color=ACCENT)
    add_text(s, 0.8, 3.5, 11.5, 0.5, "Proba ezazu pausoz pauso Arp Kali-n.", size=20, color=TEXT)
    add_text(s, 0.8, 5.5, 11.5, 0.4, "Tresnak: ping · gobuster · wget · exiftool · find · sort", size=16, color=MUTED)

    prs.save(OUT)
    return OUT


if __name__ == "__main__":
    path = build()
    print(f"Sortuta: {path}")
