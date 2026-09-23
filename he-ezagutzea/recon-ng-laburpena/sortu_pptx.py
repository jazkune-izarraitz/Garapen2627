#!/usr/bin/env python3
"""Birsortu recon-ng-osint-laburpena.pptx plantillatik.

Erabilera:
  python3 sortu_pptx.py
"""
from __future__ import annotations

import shutil
import zipfile
from copy import deepcopy
from pathlib import Path

from lxml import etree
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE / "plantilla-datu_atzipenak_laburpena.pptx"
OUT = HERE / "recon-ng-osint-laburpena.pptx"
IMG_RUN = HERE / "irudiak" / "01_run.png"
IMG_HOSTS = HERE / "irudiak" / "02_show_hosts.png"

SLIDES = [
    {
        "title": "recon-ng — OSINT laburpena",
        "desc": (
            "Hacking etikoa (HE-2): informazio publikoa biltzeko komando-lerroko "
            "framework-a. Aurkezpen honek praktikaren pausuak laburbiltzen ditu."
        ),
        "steps": [
            "OSINT tresnak eta API-ak ulertu",
            "recon-ng instalatu / abiarazi",
            "Workspace + modulua kargatu",
            "Domeinu baten gainean exekutatu",
            "Emaitzak esportatu eta dokumentatu",
        ],
        "code": [
            "# Helburua: domeinu/web/korreo OSINT",
            "# Tresna: recon-ng (Kali / Linux)",
            "# Entrega: proba + pantaila-argazkiak + esportazioak",
        ],
    },
    {
        "title": "OSINT CLI tresnak",
        "desc": (
            "Domeinuei, webgunei eta korreoei buruzko datu publikoak biltzeko "
            "tresnak. Lan errepikakorrak API bidez automatiza daitezke."
        ),
        "steps": [
            "Domeinuak eta azpidomeinuak bilatu",
            "Webguneen arrastoak bildu",
            "Korreo helbideak aurkitu",
            "Beste zerbitzuen API-ak toki bakarrean bateratu",
            "Eskuzko bilaketak erraztu / azkartu",
        ],
        "code": [
            "# Adibideak (kontzeptua):",
            "#   whois / dig / host",
            "#   recon-ng moduluen bidez API deiak",
            "#   Hunter.io, Shodan, HackerTarget...",
        ],
    },
    {
        "title": "API key-ak",
        "desc": (
            "Emaitza onak lortzeko, askotan API key behar da. Doako planak egon "
            "daitezke; batzuetan ordainpekoak dira. Key gabe modulu batzuk "
            "mugatuta geratzen dira."
        ),
        "steps": [
            "Zerbitzuan erregistratu",
            "Doako vs ordainpeko plana egiaztatu",
            "API key jaso (ez partekatu)",
            "recon-ng-n keys add bidez gorde",
            "Key gabe: emaitza hutsak / mugatuak",
        ],
        "code": [
            "# Adibideak:",
            "#   Hunter.io  → korreo bilaketa",
            "#   Shodan     → host / portuak",
            "#   HackerTarget → azpidomeinuak (maiz key gabe)",
        ],
    },
    {
        "title": "recon-ng instalazioa",
        "desc": (
            "Kali Linux-ek recon-ng ekarri ohi du. Beste Linux banaketan "
            "dokumentazio ofizialaren urratsak jarraitu."
        ),
        "steps": [
            "Kali: paketea egiaztatu / instalatu",
            "Linux: dokumentazioa jarraitu",
            "recon-ng abiarazi terminalean",
            "Marketplace / moduluak kudeatu",
            "Workspace bat sortu helburu bakoitzeko",
        ],
        "code": [
            "sudo apt update",
            "sudo apt install recon-ng",
            "recon-ng",
            "# Bertsioa egiaztatu:",
            "recon-ng --version",
        ],
    },
    {
        "title": "Nabigazioa: Workspaces → modules",
        "desc": (
            "Nabigazioa testuingurukoa da: lehenik workspace (proiektua), gero "
            "modulua (bilaketa-tresna). Maila bakoitzean aukera desberdinak daude."
        ),
        "steps": [
            "Workspace: helburu / proiektua",
            "Modules: bilaketa-tresna bakoitza",
            "options: SOURCE eta gainerakoak",
            "run: modulua exekutatu",
            "show / db: emaitzak ikusi",
        ],
        "code": [
            "workspaces create nire_helburua",
            "modules load recon/domains-hosts/hackertarget",
            "options set SOURCE example.com",
            "run",
            "show hosts",
        ],
    },
    {
        "title": "Praktika: komandoak",
        "desc": (
            "Workspace sortu, HackerTarget modulua instalatu/kargatu, SOURCE "
            "ezarri eta exekutatu. Ondoren hostak ikusi eta CSV esportatu."
        ),
        "steps": [
            "workspaces create nire_helburua",
            "marketplace install .../hackertarget",
            "modules load .../hackertarget",
            "options set SOURCE example.com",
            "run → show hosts → db export",
        ],
        "code": [
            "workspaces create nire_helburua",
            "marketplace install recon/domains-hosts/hackertarget",
            "modules load recon/domains-hosts/hackertarget",
            "options set SOURCE example.com",
            "run",
            "show hosts",
            "db export csv hosts.csv",
        ],
    },
    {
        "title": "Keys: hunter_io / shodan_api",
        "desc": (
            "API gakoak framework-ean gordetzen dira. Txostenean ez idatzi gako "
            "errealik; placeholder bat erabili."
        ),
        "steps": [
            "keys add hunter_io <ZURE_API_KEY>",
            "keys add shodan_api <ZURE_API_KEY>",
            "keys list — gordetakoak ikusi",
            "Gakoak ez partekatu / ez commit-atu",
            "Doako kuota mugatua izan daiteke",
        ],
        "code": [
            "keys add hunter_io ZURE_API_KEY",
            "keys add shodan_api ZURE_API_KEY",
            "keys list",
            "# Oharra: ez erabili gako errealik aurkezpenean",
        ],
    },
    {
        "title": "Emaitzak eta esportazioa",
        "desc": (
            "show hosts emaitzak taulan erakusten ditu. Esportatu CSV (edo DB "
            "query) eta erantsi txostenari pantaila-argazkiekin batera."
        ),
        "steps": [
            "show hosts — taula ikusi",
            "db export csv hosts.csv (edo sqlite export)",
            "Fitxategia txostenarekin igo",
            "Pantaila-argazkiak erantsi",
            "Helburua / data / modulua dokumentatu",
        ],
        "code": [
            "show hosts",
            "db export csv hosts.csv",
            "# Adibide emaitza (example.com):",
            "#   example.com      → 172.66.147.243",
            "#   www.example.com  → 104.20.23.154",
        ],
        "image": IMG_HOSTS,
    },
    {
        "title": "Exekuzioaren pantaila-argazkia",
        "desc": (
            "Laborategian example.com-en gainean hackertarget modulua exekutatu "
            "da. Pantaila-argazki gehiago gehitu daitezke praktikaren ondoren."
        ),
        "steps": [
            "Modulua: recon/domains-hosts/hackertarget",
            "SOURCE: example.com",
            "2 host berri aurkitu",
            "Emaitzak workspace DB-an gordeta",
            "hosts.csv esportatuta",
        ],
        "code": [
            "MODULE => recon/domains-hosts/hackertarget",
            "SOURCE => example.com",
            "[*] Host: example.com",
            "[*] Ip_Address: 172.66.147.243",
            "[*] Host: www.example.com",
            "[*] Ip_Address: 104.20.23.154",
            "[*] 2 total (2 new) hosts found.",
        ],
        "image": IMG_RUN,
    },
    {
        "title": "Entrega",
        "desc": (
            "Entregagaia: proben dokumentazioa + pantaila-argazkiak. "
            "Esportazio-fitxategiak erabili ahal direnean erantsi."
        ),
        "steps": [
            "Urratsak idatzi (workspace, modulua, SOURCE)",
            "Pantaila-argazkiak erantsi",
            "hosts.csv edo antzekoa igo",
            "API key-arik ez sartu",
            "Ondorio labur bat idatzi",
        ],
        "code": [
            "# Entregatzekoak:",
            "#   1) Dokumentua (urratsak + emaitzak)",
            "#   2) Pantaila-argazkiak",
            "#   3) Esportazioak (hosts.csv, ...)",
        ],
    },
    {
        "title": "Etika",
        "desc": (
            "Iturri publikoak eta legezkoak soilik. Helburu propioak edo "
            "baimenduak. API key-ak ez partekatu txostenean."
        ),
        "steps": [
            "Iturri publikoak / legezkoak",
            "Helburu propioak edo baimenduak",
            "API key-ak sekretu mantendu",
            "Ez erabili datuak gaizki",
            "Klaseko arauak errespetatu",
        ],
        "code": [
            "# Gogoratu:",
            "#   - OSINT ≠ baimenik gabeko erasoa",
            "#   - example.com / helburu baimenduak",
            "#   - keys: ZURE_API_KEY (placeholder)",
        ],
    },
]


def set_run_text(run_elem, text: str) -> None:
    t = run_elem.find(qn("a:t"))
    if t is None:
        t = etree.SubElement(run_elem, qn("a:t"))
    t.text = text
    if text.startswith(" ") or text.endswith(" ") or "  " in text:
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")


def clear_paragraphs(tx_body) -> None:
    for p in list(tx_body.findall(qn("a:p"))):
        tx_body.remove(p)


def add_paragraph(tx_body, text: str, *, bold=None, size_pt=None, font=None, bullet_prefix=None):
    p = etree.SubElement(tx_body, qn("a:p"))
    etree.SubElement(p, qn("a:pPr"))
    r = etree.SubElement(p, qn("a:r"))
    r_pr = etree.SubElement(r, qn("a:rPr"))
    r_pr.set("dirty", "0")
    if size_pt is not None:
        r_pr.set("sz", str(int(size_pt * 100)))
    if bold:
        r_pr.set("b", "1")
    if font:
        etree.SubElement(r_pr, qn("a:latin"), typeface=font)
        etree.SubElement(r_pr, qn("a:cs"), typeface=font)
    solid = etree.SubElement(r_pr, qn("a:solidFill"))
    etree.SubElement(solid, qn("a:srgbClr"), val="000000")
    display = (bullet_prefix + text) if bullet_prefix else text
    set_run_text(r, display)


def fill_textbox_shape(sp, lines, *, default_size=14, default_bold=False, font=None, first_bold=False, first_size=None):
    tx_body = sp.find(qn("p:txBody"))
    clear_paragraphs(tx_body)
    for i, line in enumerate(lines):
        if isinstance(line, tuple):
            text, opts = line
        else:
            text, opts = line, {}
        bold = opts.get("bold", first_bold if i == 0 and first_bold else default_bold)
        size = opts.get("size", first_size if i == 0 and first_size else default_size)
        fnt = opts.get("font", font)
        prefix = opts.get("bullet")
        add_paragraph(tx_body, text, bold=bold, size_pt=size, font=fnt, bullet_prefix=prefix)


def rebuild_slide_content(slide, data) -> None:
    shapes = [s for s in slide.shapes if s.has_text_frame]
    title_sp, steps_sp, desc_sp, code_sp = shapes[0], shapes[1], shapes[2], shapes[3]
    fill_textbox_shape(title_sp._element, [data["title"]], default_size=28, default_bold=True)
    step_lines = [("Pausuak:", {"bold": True, "size": 16})]
    for s in data["steps"]:
        step_lines.append((s, {"size": 14, "bullet": "• "}))
    fill_textbox_shape(steps_sp._element, step_lines, default_size=14)
    fill_textbox_shape(desc_sp._element, [data["desc"]], default_size=14)
    code_lines = [(line, {"font": "Courier New", "size": 12}) for line in data["code"]]
    fill_textbox_shape(code_sp._element, code_lines, default_size=12, font="Courier New")


def duplicate_slide(prs, index=0):
    source = prs.slides[index]
    new_slide = prs.slides.add_slide(source.slide_layout)
    for shp in source.shapes:
        new_slide.shapes._spTree.insert_element_before(deepcopy(shp._element), "p:extLst")
    return new_slide


def trim_extra_slides(pptx_path: Path, keep: int) -> None:
    tmp = HERE / "_pptx_build"
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir()
    with zipfile.ZipFile(pptx_path, "r") as z:
        z.extractall(tmp)

    pres_rels = tmp / "ppt" / "_rels" / "presentation.xml.rels"
    rel_tree = etree.parse(str(pres_rels))
    rel_root = rel_tree.getroot()

    pres_xml = tmp / "ppt" / "presentation.xml"
    pre_tree = etree.parse(str(pres_xml))
    sld_id_lst = pre_tree.find(
        ".//{http://schemas.openxmlformats.org/presentationml/2006/main}sldIdLst"
    )
    for extra in list(sld_id_lst)[keep:]:
        rid = extra.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
        sld_id_lst.remove(extra)
        for rel in list(rel_root):
            if rel.get("Id") == rid:
                target = rel.get("Target")
                rel_root.remove(rel)
                slide_path = tmp / "ppt" / target
                if slide_path.exists():
                    slide_path.unlink()
                rels_path = tmp / "ppt" / "slides" / "_rels" / (Path(target).name + ".rels")
                if rels_path.exists():
                    rels_path.unlink()

    pre_tree.write(str(pres_xml), xml_declaration=True, encoding="UTF-8", standalone=True)
    rel_tree.write(str(pres_rels), xml_declaration=True, encoding="UTF-8", standalone=True)

    ct_path = tmp / "[Content_Types].xml"
    ct_tree = etree.parse(str(ct_path))
    ct_root = ct_tree.getroot()
    existing = {p.name for p in (tmp / "ppt" / "slides").glob("slide*.xml")}
    for ov in list(ct_root):
        pn = ov.get("PartName", "")
        if "/ppt/slides/slide" in pn and Path(pn).name not in existing:
            ct_root.remove(ov)
    ct_tree.write(str(ct_path), xml_declaration=True, encoding="UTF-8", standalone=True)

    with zipfile.ZipFile(pptx_path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in tmp.rglob("*"):
            if f.is_file():
                z.write(f, f.relative_to(tmp).as_posix())
    shutil.rmtree(tmp)


def place_image(prs, slide, image_path: Path) -> None:
    if not image_path.exists():
        return
    for shp in list(slide.shapes):
        if shp.shape_type == MSO_SHAPE_TYPE.PICTURE:
            slide.shapes._spTree.remove(shp._element)
    textboxes = sorted([s for s in slide.shapes if s.has_text_frame], key=lambda s: s.top)
    code_box = textboxes[-1]
    code_box.height = Emu(1750000)
    from PIL import Image as PILImage

    im = PILImage.open(image_path)
    aspect = im.size[1] / im.size[0]
    max_w, max_h = Inches(8.5), Inches(1.85)
    w, h = max_w, int(max_w * aspect)
    if h > max_h:
        h, w = max_h, int(max_h / aspect)
    left = Emu(365760)
    top = code_box.top + code_box.height + Emu(80000)
    if top + h > prs.slide_height - Emu(60000):
        h = prs.slide_height - Emu(60000) - top
        w = int(h / aspect)
    slide.shapes.add_picture(str(image_path), left, top, width=w, height=h)


def main() -> None:
    if not TEMPLATE.exists():
        raise SystemExit(f"Plantilla falta: {TEMPLATE}")
    shutil.copy(TEMPLATE, OUT)
    prs = Presentation(str(OUT))
    while len(prs.slides) < len(SLIDES):
        duplicate_slide(prs, 0)
    for i, data in enumerate(SLIDES):
        rebuild_slide_content(prs.slides[i], data)
    prs.save(str(OUT))
    trim_extra_slides(OUT, len(SLIDES))

    prs2 = Presentation(str(OUT))
    for i, data in enumerate(SLIDES):
        if data.get("image"):
            place_image(prs2, prs2.slides[i], Path(data["image"]))
    prs2.save(str(OUT))
    print(f"Idatzi da: {OUT} ({len(SLIDES)} diapositiba)")


if __name__ == "__main__":
    main()
