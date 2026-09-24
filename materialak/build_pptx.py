#!/usr/bin/env python3
"""Build JDBC classroom presentation as PPTX."""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Emu, Inches, Pt

OUT = Path(__file__).resolve().parent / "Konektoreekin-hasiera-demodb.pptx"
DIAGRAM = Path(__file__).resolve().parent / "konektorea-diagrama.png"

# Widescreen 16:9
W, H = Inches(13.333), Inches(7.5)

BG_DEEP = RGBColor(0x0F, 0x2A, 0x32)
BG_LIGHT = RGBColor(0xEE, 0xF4, 0xF6)
TEAL = RGBColor(0x0D, 0x6E, 0x6E)
TEAL_SOFT = RGBColor(0xD4, 0xEC, 0xEC)
AMBER = RGBColor(0xC4, 0x7A, 0x14)
AMBER_SOFT = RGBColor(0xF4, 0xE6, 0xD0)
INK = RGBColor(0x14, 0x24, 0x28)
MUTED = RGBColor(0x4A, 0x60, 0x68)
WHITE = RGBColor(0xF4, 0xF8, 0xF9)
PANEL = RGBColor(0xF7, 0xFA, 0xFB)
LINE = RGBColor(0xC5, 0xD4, 0xDA)
DANGER = RGBColor(0xA3, 0x3B, 0x2C)
OK = RGBColor(0x1F, 0x6B, 0x45)
CODE_BG = RGBColor(0x10, 0x26, 0x2C)
CODE_FG = RGBColor(0xD7, 0xEC, 0xE9)


def set_slide_bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_textbox(slide, left, top, width, height, text, *, size=18, bold=False, color=INK, font="Calibri", align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    try:
        tf._txBody.bodyPr.set("anchor", {MSO_ANCHOR.TOP: "t", MSO_ANCHOR.MIDDLE: "ctr", MSO_ANCHOR.BOTTOM: "b"}[anchor])
    except Exception:
        pass
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = font
    return box


def add_paras(slide, left, top, width, height, lines, *, size=16, color=MUTED, bold_first=False, font="Calibri", spacing=6):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(spacing)
        run = p.add_run()
        run.text = line
        run.font.size = Pt(size)
        run.font.bold = bold_first and i == 0
        run.font.color.rgb = color if not (bold_first and i == 0) else INK
        run.font.name = font
    return box


def add_kicker(slide, text, *, dark=False):
    add_textbox(
        slide, Inches(0.7), Inches(0.35), Inches(12), Inches(0.35),
        text.upper(), size=12, bold=True, color=(RGBColor(0x9F, 0xD7, 0xD4) if dark else TEAL),
        font="Calibri",
    )


def add_title(slide, text, *, dark=False, top=0.7):
    add_textbox(
        slide, Inches(0.7), Inches(top), Inches(12), Inches(1.1),
        text, size=36, bold=True, color=(WHITE if dark else BG_DEEP), font="Georgia",
    )


def add_why(slide, label, text, left=0.7, top=6.2, width=12):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(0.85))
    shape.fill.solid()
    shape.fill.fore_color.rgb = AMBER_SOFT
    shape.line.fill.background()
    # amber bar
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Inches(0.08), Inches(0.85))
    bar.fill.solid()
    bar.fill.fore_color.rgb = AMBER
    bar.line.fill.background()
    add_textbox(slide, Inches(left + 0.25), Inches(top + 0.08), Inches(width - 0.4), Inches(0.28), label.upper(), size=10, bold=True, color=AMBER)
    add_textbox(slide, Inches(left + 0.25), Inches(top + 0.32), Inches(width - 0.4), Inches(0.48), text, size=14, color=RGBColor(0x5A, 0x3A, 0x10))


def add_card(slide, left, top, width, height, title, body_lines):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    shape.fill.solid()
    shape.fill.fore_color.rgb = PANEL
    shape.line.color.rgb = LINE
    add_textbox(slide, Inches(left + 0.2), Inches(top + 0.15), Inches(width - 0.4), Inches(0.35), title, size=16, bold=True, color=TEAL)
    add_paras(slide, Inches(left + 0.2), Inches(top + 0.5), Inches(width - 0.4), Inches(height - 0.65), body_lines, size=14, color=MUTED, spacing=4)


def add_code(slide, left, top, width, height, code):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    shape.fill.solid()
    shape.fill.fore_color.rgb = CODE_BG
    shape.line.fill.background()
    box = slide.shapes.add_textbox(Inches(left + 0.2), Inches(top + 0.15), Inches(width - 0.4), Inches(height - 0.3))
    tf = box.text_frame
    tf.word_wrap = True
    for i, line in enumerate(code.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(2)
        run = p.add_run()
        run.text = line
        run.font.size = Pt(12)
        run.font.color.rgb = CODE_FG
        run.font.name = "Consolas"


def blank_slide(prs, dark=False):
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
    set_slide_bg(slide, BG_DEEP if dark else BG_LIGHT)
    return slide


def build():
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H

    # 1 Portada
    s = blank_slide(prs, dark=True)
    add_kicker(s, "Garapen Inguruneak · JDBC", dark=True)
    add_textbox(s, Inches(0.7), Inches(3.6), Inches(11), Inches(1.4), "Konektoreekin hasiera", size=48, bold=True, color=WHITE, font="Georgia")
    add_textbox(
        s, Inches(0.7), Inches(5.2), Inches(11), Inches(1.2),
        "Gaur: zergatik behar dugun konektorea, nola konektatzen garen MySQL-ra, eta nola irakurri/idatzi demodb datu-basean Java-tik.",
        size=18, color=RGBColor(0xD5, 0xE4, 0xE7),
    )

    # 2 Helburua
    s = blank_slide(prs)
    add_kicker(s, "Helburua")
    add_title(s, "Zer ikasiko dugu gaur?")
    add_card(s, 0.7, 2.0, 3.8, 2.8, "1. Ideia", ["Zer den JDBC konektorea", "eta zergatik dagoen", "aplikazioaren eta", "datu-basearen artean."])
    add_card(s, 4.75, 2.0, 3.8, 2.8, "2. Prestaketa", ["MySQL (Docker), demodb.sql", "eta JAR-a proiektuan", "jartzea — bakoitzaren", "zergatia."])
    add_card(s, 8.8, 2.0, 3.8, 2.8, "3. Praktika", ["SELECT → UPDATE (Statement)", "→ PreparedStatement", "→ transakzioak."])
    add_why(s, "Zergatik orden honetan?", "Lehenik ulertu komunikazioa; gero irakurri; gero idatzi; azkenik idazketa seguruagoa eta kontrolatua.")

    # 3 Arazoa
    s = blank_slide(prs)
    add_kicker(s, "Arazoa")
    add_title(s, "Java-k ez du MySQL “hizkuntzarik”")
    add_textbox(
        s, Inches(0.7), Inches(2.0), Inches(6.5), Inches(1.5),
        "Zure programak objektuak eta metodoak erabiltzen ditu. MySQL-k SQL eta bere protokoloa ulertzen du. Bi mundu horiek ez dira berdinak.",
        size=18, color=MUTED,
    )
    add_card(s, 0.7, 3.7, 6.5, 2.0, "Galdera klabea", ["Nola esango dio Java aplikazio batek datu-baseari:", "“Ekarri DEPT taulako sailak”?"])
    add_card(s, 7.5, 2.0, 5.1, 3.7, "Bi aldeak", [
        "• Java: klaseak, metodoak, String, int…",
        "• MySQL: taulak, SQL, portuak, erabiltzaileak…",
        "• Tartean falta dena: itzultzaile/zubi bat.",
    ])

    # 4 Zer da konektorea
    s = blank_slide(prs)
    add_kicker(s, "Definizioa")
    add_title(s, "Zer da konektorea?")
    add_textbox(
        s, Inches(0.7), Inches(1.9), Inches(6.2), Inches(1.6),
        "Konektorea (driver) zure aplikazioaren eta DBKSaren arteko zubia da. JDBC API-ko komandoak hartu eta datu-basearen protokolo natibora bihurtzen ditu.",
        size=17, color=MUTED,
    )
    add_why(s, "Zertarako erabiliko dugu?", "Java-tik demodb irakurri eta aldatzeko: sailak zerrendatu, izenak eguneratu, erroreetan atzera egin.", top=3.7, width=6.2)
    add_textbox(s, Inches(0.7), Inches(4.8), Inches(6.2), Inches(0.8), "JDBC = Java API estandarra\nDriver = MySQL-rako inplementazioa (JAR)", size=14, bold=True, color=TEAL)
    if DIAGRAM.exists():
        s.shapes.add_picture(str(DIAGRAM), Inches(7.1), Inches(1.8), width=Inches(5.5))

    # 5 Hiru geruza
    s = blank_slide(prs)
    add_kicker(s, "Arkitektura")
    add_title(s, "Hiru geruza, rol bakoitza")
    boxes = [
        (0.7, "Java aplikazioa", "Zure kodea:\nStatement, ResultSet…", TEAL),
        (4.9, "Konektorea", "mysql-connector.jar\nItzulpena + sarea", AMBER),
        (9.1, "MySQL", "demodb\nDEPT / EMP", TEAL),
    ]
    for left, title, body, border in boxes:
        shape = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(2.0), Inches(3.5), Inches(2.0))
        shape.fill.solid()
        shape.fill.fore_color.rgb = PANEL if border == TEAL else AMBER_SOFT
        shape.line.color.rgb = border
        shape.line.width = Pt(2)
        add_textbox(s, Inches(left + 0.2), Inches(2.25), Inches(3.1), Inches(0.5), title, size=18, bold=True, color=BG_DEEP, align=PP_ALIGN.CENTER)
        add_textbox(s, Inches(left + 0.2), Inches(2.85), Inches(3.1), Inches(0.9), body, size=14, color=MUTED, align=PP_ALIGN.CENTER)
    for x in (4.2, 8.4):
        add_textbox(s, Inches(x), Inches(2.6), Inches(0.6), Inches(0.5), "→", size=28, bold=True, color=TEAL, align=PP_ALIGN.CENTER)
    add_card(s, 0.7, 4.4, 3.8, 1.6, "Zergatik JAR?", ["MySQL-ren “hizkuntza” ez dator", "Javarekin. Classpath-ean gehitu."])
    add_card(s, 4.75, 4.4, 3.8, 1.6, "Zergatik JDBC URL?", ["Non, zein portu, zein DB:", "jdbc:mysql://localhost:3306/demodb"])
    add_card(s, 8.8, 4.4, 3.8, 1.6, "Zergatik Docker?", ["Instalazio berdina denentzat.", "Portua mapeatu kanpotik sartzeko."])

    # 6 Prestaketa
    s = blank_slide(prs)
    add_kicker(s, "Prestaketa · 0")
    add_title(s, "Ariketa baino lehen: 3 pieza")
    steps = [
        ("MySQL martxan (Docker)", "Datuak nonbait egon behar dute. Kontainerra = DBKS berdina ikasle guztientzat."),
        ("demodb.sql inportatu", "Taularik gabe ez dago zer kontsultatu. Script-ak DEPT eta EMP sortzen ditu."),
        ("mysql-connector JAR proiektuan", "Java-k MySQL-rekin hitz egiteko driver-a behar du. Gabe: SQLException."),
    ]
    for i, (t, b) in enumerate(steps):
        y = 2.0 + i * 1.15
        circ = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.7), Inches(y), Inches(0.55), Inches(0.55))
        circ.fill.solid()
        circ.fill.fore_color.rgb = TEAL
        circ.line.fill.background()
        add_textbox(s, Inches(0.7), Inches(y + 0.08), Inches(0.55), Inches(0.4), str(i + 1), size=16, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(y - 0.05), Inches(11), Inches(1.0))
        card.fill.solid()
        card.fill.fore_color.rgb = PANEL
        card.line.color.rgb = LINE
        add_textbox(s, Inches(1.75), Inches(y), Inches(10.5), Inches(0.35), t, size=16, bold=True, color=INK)
        add_textbox(s, Inches(1.75), Inches(y + 0.35), Inches(10.5), Inches(0.45), b, size=14, color=MUTED)
    add_why(s, "Gogoratu", "Host 127.0.0.1 · Portua 3306 (edo zure hostPort) · Erabiltzailea root · Datu-basea demodb")

    # 7 Konexioa
    s = blank_slide(prs)
    add_kicker(s, "1. urratsa")
    add_title(s, "Konexioa: atea ireki")
    add_textbox(
        s, Inches(0.7), Inches(1.9), Inches(6.2), Inches(1.3),
        "DriverManager.getConnection(...) deitzen duzunean, JDBC-k driver egokia bilatzen du URL-aren arabera eta Connection objektua itzultzen du.",
        size=16, color=MUTED,
    )
    add_why(s, "Zergatik lehenengo hau?", "Konexiorik gabe ezin da SQL bidali. Ariketa guztiak Connection horretatik abiatzen dira.", top=3.3, width=6.2)
    add_card(s, 0.7, 4.4, 6.2, 1.8, "Ondo egiteko", [
        "• try-with-resources → konexioa beti itxi",
        "• URL + erabiltzaile + pasahitz zuzenak",
        "• Errorea? JAR, portua edo demodb falta",
    ])
    add_code(s, 7.2, 1.9, 5.4, 4.3, """// JDBC URL
String url =
  "jdbc:mysql://localhost:3306/demodb";
String user = "root";
String pass = "2paag3";

try (Connection con =
  DriverManager.getConnection(
    url, user, pass)) {
  System.out.println("Konektatuta!");
}""")

    # 8 Statement motak
    s = blank_slide(prs)
    add_kicker(s, "Tresnak")
    add_title(s, "Statement motak (gaur behar ditugunak)")
    add_card(s, 0.7, 2.0, 5.8, 3.2, "Statement", [
        "SQL kate osoa bidaltzen duzu. Sinplea.",
        "Ariketan 1 eta 2rako.",
        "",
        "• executeQuery → SELECT",
        "• executeUpdate → INSERT/UPDATE/DELETE",
    ])
    add_card(s, 6.8, 2.0, 5.8, 3.2, "PreparedStatement", [
        "SQL txantiloi bat ? parametroekin.",
        "Ariketa 3 (eta 4).",
        "",
        "• Seguruagoa (injection)",
        "• Garbiagoa parametroekin",
        "• Berrerabilgarria",
    ])
    add_why(s, "Zergatik biak ikasi?", "Lehenik Statement-ekin mekanika ulertu; gero PreparedStatement-ekin ohitura ona finkatu. Produkzioan PreparedStatement nahiago.")

    # 9 Ariketa 1
    s = blank_slide(prs)
    add_kicker(s, "Ariketa 1")
    add_title(s, "Sailak irakurri (SELECT)")
    add_textbox(s, Inches(0.7), Inches(1.9), Inches(6.2), Inches(0.5), "Helburua: sail bakoitzaren zenbakia eta izena pantailaratu.", size=16, color=MUTED)
    for i, (t, b) in enumerate([
        ("Statement sortu", "con.createStatement()"),
        ("executeQuery", "SELECT → ResultSet (taula)"),
        ("while (rs.next())", "Kurtsorea errenkadaz errenkada"),
    ]):
        y = 2.5 + i * 0.85
        circ = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.7), Inches(y), Inches(0.45), Inches(0.45))
        circ.fill.solid()
        circ.fill.fore_color.rgb = TEAL
        circ.line.fill.background()
        add_textbox(s, Inches(0.7), Inches(y + 0.05), Inches(0.45), Inches(0.35), str(i + 1), size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
        add_textbox(s, Inches(1.35), Inches(y), Inches(5.5), Inches(0.3), t, size=15, bold=True, color=INK)
        add_textbox(s, Inches(1.35), Inches(y + 0.3), Inches(5.5), Inches(0.35), b, size=13, color=MUTED)
    add_why(s, "Zergatik SELECT lehenik?", "Idatzi aurretik irakurri: datuak daudela ikusi, URL/JAR/taulak ondo daudela frogatu.", top=5.3, width=6.2)
    add_code(s, 7.2, 1.9, 5.4, 4.5, """Statement st = con.createStatement();
ResultSet rs = st.executeQuery(
  "SELECT DEPTNO, DNAME FROM DEPT"
);
while (rs.next()) {
  int no = rs.getInt("DEPTNO");
  String iz = rs.getString("DNAME");
  System.out.println(no + " - " + iz);
}""")

    # 10 Ariketa 2
    s = blank_slide(prs)
    add_kicker(s, "Ariketa 2")
    add_title(s, "Sailaren izena aldatu (Statement)")
    add_textbox(
        s, Inches(0.7), Inches(1.9), Inches(6.2), Inches(0.9),
        "main-eko bi parametro: sail-zenbakia eta izen berria. Oraingoz Statement soilik (ez PreparedStatement).",
        size=16, color=MUTED,
    )
    add_card(s, 0.7, 2.9, 6.2, 1.5, "Exekuzio adibidea", [
        "java AldatuSaila 30 Logistika",
        "args[0] = 30 · args[1] = Logistika",
    ])
    add_why(s, "Zergatik executeUpdate?", "UPDATE batean ez dugu taularik itzultzen; eraginiko errenkada-kopurua itzultzen du. Hori inprimatu.", top=4.6, width=6.2)
    add_code(s, 7.2, 1.9, 5.4, 3.5, """int deptno = Integer.parseInt(args[0]);
String izena = args[1];

String sql =
  "UPDATE DEPT SET DNAME='" + izena +
  "' WHERE DEPTNO=" + deptno;

int n = st.executeUpdate(sql);
System.out.println("Aldatuta: " + n);""")
    warn = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.2), Inches(5.55), Inches(5.4), Inches(1.2))
    warn.fill.solid()
    warn.fill.fore_color.rgb = RGBColor(0xFB, 0xE8, 0xE5)
    warn.line.color.rgb = DANGER
    add_textbox(s, Inches(7.4), Inches(5.65), Inches(5.0), Inches(0.3), "Kontuz (horregatik doa 3. ariketa)", size=13, bold=True, color=DANGER)
    add_textbox(s, Inches(7.4), Inches(5.95), Inches(5.0), Inches(0.65), "SQL kateatzeak arriskutsua da (SQL injection). Hurrengo pausoak hori zuzentzen du.", size=12, color=MUTED)

    # 11 Ariketa 3
    s = blank_slide(prs)
    add_kicker(s, "Ariketa 3")
    add_title(s, "Gauza bera, PreparedStatement-ekin")
    add_textbox(
        s, Inches(0.7), Inches(1.9), Inches(6.2), Inches(1.1),
        "SQL finkoa idazten duzu; balioak gero setXxx bidez sartzen dira. Konektoreak balioak segurtasunez bidaltzen ditu.",
        size=16, color=MUTED,
    )
    bad = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(3.2), Inches(2.9), Inches(1.3))
    bad.fill.solid()
    bad.fill.fore_color.rgb = PANEL
    bad.line.color.rgb = DANGER
    add_textbox(s, Inches(0.9), Inches(3.35), Inches(2.5), Inches(0.3), "Lehen", size=14, bold=True, color=DANGER)
    add_textbox(s, Inches(0.9), Inches(3.7), Inches(2.5), Inches(0.6), "SQL + aldagaiak kateatu", size=13, color=MUTED)
    good = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.9), Inches(3.2), Inches(3.0), Inches(1.3))
    good.fill.solid()
    good.fill.fore_color.rgb = PANEL
    good.line.color.rgb = OK
    add_textbox(s, Inches(4.1), Inches(3.35), Inches(2.6), Inches(0.3), "Orain", size=14, bold=True, color=OK)
    add_textbox(s, Inches(4.1), Inches(3.7), Inches(2.6), Inches(0.6), "? + setString / setInt", size=13, color=MUTED)
    add_why(s, "Zergatik hau ikasi?", "Parametroak bereizteak kodea argitzen du eta injekzioa saihesten du. Ohitura ona lehen egunetik.", top=4.8, width=6.2)
    add_code(s, 7.2, 1.9, 5.4, 4.5, """String sql =
  "UPDATE DEPT SET DNAME=? WHERE DEPTNO=?";

PreparedStatement ps =
  con.prepareStatement(sql);
ps.setString(1, izena);   // 1. ?
ps.setInt(2, deptno);     // 2. ?

int n = ps.executeUpdate();
System.out.println("Aldatuta: " + n);""")

    # 12 Transakzioak
    s = blank_slide(prs)
    add_kicker(s, "Ariketa 4")
    add_title(s, "Transakzioak: guztia edo ezer ez")
    add_textbox(
        s, Inches(0.7), Inches(1.9), Inches(6.2), Inches(0.9),
        "Defektuz autocommit piztuta dago: sententzia bakoitza berehala gordetzen da. Multzokatu nahi badugu, itzali.",
        size=16, color=MUTED,
    )
    for i, (t, b) in enumerate([
        ("setAutoCommit(false)", "Hemendik aurrerakoak pakete batean."),
        ("commit()", "Dena ondo → aldaketak behin betiko."),
        ("rollback()", "SQLException → ezer ez da gordetzen."),
    ]):
        y = 2.9 + i * 0.75
        circ = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.7), Inches(y), Inches(0.4), Inches(0.4))
        circ.fill.solid()
        circ.fill.fore_color.rgb = TEAL
        circ.line.fill.background()
        add_textbox(s, Inches(0.7), Inches(y + 0.03), Inches(0.4), Inches(0.35), str(i + 1), size=12, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
        add_textbox(s, Inches(1.3), Inches(y), Inches(5.5), Inches(0.25), t, size=14, bold=True, color=INK)
        add_textbox(s, Inches(1.3), Inches(y + 0.28), Inches(5.5), Inches(0.3), b, size=12, color=MUTED)
    add_why(s, "Zergatik behar dugu?", "Eguneraketa bat baino gehiago elkarren menpekoak direnean: erdi-eginda uztea okerragoa da ezer ez egitea baino.", top=5.3, width=6.2)
    add_code(s, 7.2, 1.9, 5.4, 4.5, """con.setAutoCommit(false);
try {
  ps.executeUpdate();
  // beste sententziak...
  con.commit();
} catch (SQLException e) {
  con.rollback();
  throw e;
} finally {
  con.setAutoCommit(true);
}""")

    # 13 Eskema
    s = blank_slide(prs)
    add_kicker(s, "Eskema")
    add_title(s, "demodb: bi taula, erlazio bat")
    add_card(s, 0.7, 2.0, 5.8, 3.2, "DEPT (sailak)", [
        "• DEPTNO  PK",
        "• DNAME   izena",
        "• LOC     kokapena",
        "",
        "Gaurko ariketak hemen zentratzen dira.",
    ])
    add_card(s, 6.8, 2.0, 5.8, 3.2, "EMP (langileak)", [
        "• EMPNO   PK",
        "• ENAME, JOB, SAL…",
        "• DEPTNO  FK → DEPT",
        "",
        "Saila aldatzean FK kontuan hartu.",
    ])
    add_why(s, "Zergatik eskema hau?", "Adibide klasikoa eta txikia: SELECT eta UPDATE erraz frogatzeko, erlazio erreal batekin.")

    # 14 Proba-ordena
    s = blank_slide(prs)
    add_kicker(s, "Klasean")
    add_title(s, "Proba-ordena gomendatua")
    order = [
        ("Workbench-en konektatu", "MySQL bizirik dagoela ziurtatu (Docker + portua)."),
        ("demodb.sql", "Taulak eta datuak kargatu."),
        ("Ariketa 1", "SELECT → 4 sail agertu behar dira."),
        ("Ariketa 2", "UPDATE Statement → “Aldatuta: 1”. Workbench-en egiaztatu."),
        ("Ariketa 3", "PreparedStatement → emaitza bera, kode garbia."),
        ("Ariketa 4", "Errore bat behartu → rollback → datuak bere horretan."),
    ]
    for i, (t, b) in enumerate(order):
        col = i % 2
        row = i // 2
        left = 0.7 + col * 6.3
        top = 1.95 + row * 1.45
        shape = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(6.0), Inches(1.25))
        shape.fill.solid()
        shape.fill.fore_color.rgb = PANEL
        shape.line.color.rgb = LINE
        circ = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(left + 0.15), Inches(top + 0.35), Inches(0.45), Inches(0.45))
        circ.fill.solid()
        circ.fill.fore_color.rgb = TEAL
        circ.line.fill.background()
        add_textbox(s, Inches(left + 0.15), Inches(top + 0.4), Inches(0.45), Inches(0.35), str(i + 1), size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
        add_textbox(s, Inches(left + 0.8), Inches(top + 0.25), Inches(4.9), Inches(0.35), t, size=15, bold=True, color=INK)
        add_textbox(s, Inches(left + 0.8), Inches(top + 0.6), Inches(4.9), Inches(0.5), b, size=13, color=MUTED)

    # 15 Laburpena
    s = blank_slide(prs)
    add_kicker(s, "Laburpena")
    add_title(s, "Gogoratzeko 5 ideia")
    ideas = [
        ("Konektorea", "Java ↔ MySQL zubia. JAR gabe ez dago komunikaziorik."),
        ("Connection", "Atea. Hortik sortzen dira Statement / PreparedStatement."),
        ("Query vs Update", "SELECT → ResultSet. UPDATE → eraginiko kopurua."),
        ("PreparedStatement", "Parametroak ?-rekin: seguruagoa eta argiagoa."),
        ("Transakzioa", "commit = gorde guztia. rollback = ezer ez."),
        ("Gaurko fokua", "Pool-ak eta prozedurak gerorako. Gaur oinarria."),
    ]
    for i, (t, b) in enumerate(ideas):
        col = i % 3
        row = i // 3
        add_card(s, 0.7 + col * 4.15, 2.0 + row * 2.2, 3.95, 1.95, t, [b])

    # 16 Amaiera
    s = blank_slide(prs, dark=True)
    add_kicker(s, "Hurrengoa", dark=True)
    add_textbox(s, Inches(0.7), Inches(3.4), Inches(11), Inches(1.2), "Zuek probatzeko", size=44, bold=True, color=WHITE, font="Georgia")
    add_textbox(
        s, Inches(0.7), Inches(4.8), Inches(11.5), Inches(1.4),
        "Ireki proiektua, JAR gehitu, konektatu demodb-ra eta hasi 1. ariketa: sailak pantailaratu. Blokeatzen bazarete: URL, portua, pasahitza edo JAR falta ohi da.",
        size=18, color=RGBColor(0xD5, 0xE4, 0xE7),
    )

    prs.save(OUT)
    print(f"Saved: {OUT}")
    print(f"Size: {OUT.stat().st_size} bytes")
    return OUT


if __name__ == "__main__":
    build()
