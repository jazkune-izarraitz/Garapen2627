#!/usr/bin/env python3
"""Ezagutze pasiboa – whois / dig / nslookup jarduera praktikoa (Word)."""

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


def gehitu_kontsola(doc: Document, testua: str) -> None:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.left_indent = Cm(0.25)
    pPr = p._element.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), "F0F0F0")
    pPr.append(shd)
    run = p.add_run(testua)
    run.font.name = "Consolas"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Consolas")
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)


def lerro_huts(doc: Document) -> None:
    doc.add_paragraph()


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

    h = doc.add_heading("Ezagutze pasiboa – Jarduera praktikoa", level=0)
    h.alignment = WD_ALIGN_PARAGRAPH.CENTER

    azpi = doc.add_paragraph()
    azpi.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = azpi.add_run(
        "Tresnak: whois · nslookup · dig\n"
        "Helburua: domeinu publikoen informazioa bildu, helburua zuzenean erasotu gabe"
    )
    r.italic = True

    doc.add_paragraph(
        "Lan egin Linux terminalean (Kali, AttackBox, Ubuntu…). "
        "Komandoak zuk exekutatu behar dituzu. Erantzunak idatzi lerroetan. "
        "Irtenbideak dokumentuko azken orrialdean daude."
    )

    # --- Prestaketa ---
    doc.add_heading("0. Prestaketa", level=1)
    doc.add_paragraph("Egiaztatu tresnak instalatuta daudela:")
    gehitu_kontsola(
        doc,
        "which whois nslookup dig\n"
        "# Faltaren bat badago (Debian/Ubuntu):\n"
        "sudo apt update && sudo apt install -y whois dnsutils",
    )
    doc.add_paragraph(
        "Oharra: kontsulta hauek iturri publikoetara doaz (WHOIS/DNS). "
        "Ezagutze pasiboa da; ez bidali paketerik helburuko zerbitzarira (ez ping, ez nmap)."
    )

    # --- Atala 1: whois ---
    doc.add_heading("1. atala – whois", level=1)
    doc.add_paragraph(
        "WHOIS-ek domeinuaren erregistro-datuak ematen ditu: erregistratzailea, datak, name-zerbitzariak…"
    )
    doc.add_paragraph("Exekutatu:")
    gehitu_kontsola(doc, "whois tryhackme.com")

    doc.add_paragraph().add_run("1.1 ").bold = True
    doc.paragraphs[-1].add_run("Noiz erregistratu zen tryhackme.com? (Creation Date)")
    doc.add_paragraph("Erantzuna: _________________________________")

    doc.add_paragraph().add_run("1.2 ").bold = True
    doc.paragraphs[-1].add_run("Zein da erregistratzailea (Registrar)?")
    doc.add_paragraph("Erantzuna: _________________________________")

    doc.add_paragraph().add_run("1.3 ").bold = True
    doc.paragraphs[-1].add_run("Zein enpresaren name-zerbitzariak erabiltzen ditu?")
    doc.add_paragraph("Erantzuna: _________________________________")

    doc.add_paragraph("Beste domeinu batekin proba (aukerakoa):")
    gehitu_kontsola(doc, "whois wikipedia.org | head -n 40")

    # --- Atala 2: nslookup ---
    doc.add_heading("2. atala – nslookup", level=1)
    doc.add_paragraph(
        "nslookup-ek DNS erregistroak kontsultatzen ditu. "
        "Erabilgarria da Windows-en eta dokumentazio zaharrean."
    )
    doc.add_paragraph("A erregistroa (IPv4):")
    gehitu_kontsola(doc, "nslookup tryhackme.com")

    doc.add_paragraph().add_run("2.1 ").bold = True
    doc.paragraphs[-1].add_run("Zein IPv4 helbide (gutxienez bat) lortu duzu?")
    doc.add_paragraph("Erantzuna: _________________________________")

    doc.add_paragraph("TXT erregistroak:")
    gehitu_kontsola(doc, "nslookup -type=TXT thmlabs.com")

    doc.add_paragraph().add_run("2.2 ").bold = True
    doc.paragraphs[-1].add_run("Zein da thmlabs.com-en TXT erregistroan agertzen den bandera (THM{…})?")
    doc.add_paragraph("Erantzuna: _________________________________")

    doc.add_paragraph("MX erregistroak DNS publiko batekin (Cloudflare 1.1.1.1):")
    gehitu_kontsola(doc, "nslookup -type=MX tryhackme.com 1.1.1.1")

    doc.add_paragraph().add_run("2.3 ").bold = True
    doc.paragraphs[-1].add_run("Aipatu gutxienez posta-zerbitzari (mail exchanger) bat:")
    doc.add_paragraph("Erantzuna: _________________________________")

    # --- Atala 3: dig ---
    doc.add_heading("3. atala – dig", level=1)
    doc.add_paragraph(
        "dig tresna modernoa da: irteera garbia, TTL balioak eta scripting-erako egokia."
    )
    doc.add_paragraph("A erregistroa:")
    gehitu_kontsola(doc, "dig tryhackme.com A")

    doc.add_paragraph().add_run("3.1 ").bold = True
    doc.paragraphs[-1].add_run(
        "ANSWER SECTION-en, zenbat segundo durako TTL bat ikusi duzu? (zenbakia)"
    )
    doc.add_paragraph("Erantzuna: _________________________________")

    doc.add_paragraph("TXT (berriro, dig-ekin):")
    gehitu_kontsola(doc, "dig thmlabs.com TXT")

    doc.add_paragraph().add_run("3.2 ").bold = True
    doc.paragraphs[-1].add_run("Berretsi 2.2ko bandera dig-ekin. Berdina da? (Bai/Ez)")
    doc.add_paragraph("Erantzuna: _________________________________")

    doc.add_paragraph("MX Cloudflare DNS erabiliz:")
    gehitu_kontsola(doc, "dig @1.1.1.1 tryhackme.com MX")

    doc.add_paragraph().add_run("3.3 ").bold = True
    doc.paragraphs[-1].add_run(
        "MX lerroetan agertzen den lehentasun (priority) zenbakietatik, zein da txikiena? "
        "Zenbaki txikiagoak lehentasun handiagoa du."
    )
    doc.add_paragraph("Erantzuna: _________________________________")

    # --- Atala 4: konparazioa ---
    doc.add_heading("4. atala – Konparazio laburra", level=1)
    doc.add_paragraph().add_run("4.1 ").bold = True
    doc.paragraphs[-1].add_run(
        "Zergatik jotzen dira whois / nslookup / dig kontsulta hauek ezagutze pasibotzat?"
    )
    doc.add_paragraph("Erantzuna: _________________________________")
    doc.add_paragraph("_______________________________________________")

    doc.add_paragraph().add_run("4.2 ").bold = True
    doc.paragraphs[-1].add_run(
        "nslookup eta dig artean, zein gomendatuko zenuke gaur egun eta zergatik? "
        "(labur)"
    )
    doc.add_paragraph("Erantzuna: _________________________________")
    doc.add_paragraph("_______________________________________________")

    # --- Erronka ---
    doc.add_heading("5. atala – Erronka (aukerakoa)", level=1)
    doc.add_paragraph("Aukeratu domeinu publiko bat (adib. example.com, cloudflare.com) eta:")
    gehitu_kontsola(
        doc,
        "whois DOMEINUA | less\n"
        "dig DOMEINUA A\n"
        "dig DOMEINUA MX\n"
        "dig DOMEINUA TXT\n"
        "dig DOMEINUA NS",
    )
    doc.add_paragraph(
        "Idatzi 3 datu interesgarri (erregistratzailea, NS, MX, TXT…):"
    )
    doc.add_paragraph("1. _________________________________")
    doc.add_paragraph("2. _________________________________")
    doc.add_paragraph("3. _________________________________")

    # --- Erantzunak ---
    doc.add_page_break()
    eh = doc.add_heading("Irtenbideak (irakaslearentzat)", level=1)
    eh.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph(
        "Oharra: WHOIS/DNS datu batzuk denboran alda daitezke (IP, TTL, MX). "
        "Bandera eta kontzeptuak egonkorragoak dira."
    )
    lerro_huts(doc)

    irtenbideak = [
        (
            "1.1",
            "2018-07-05 (Creation Date; TryHackMe room-ean 20180705 gisa ere onartzen da).",
        ),
        ("1.2", "Namecheap / NAMECHEAP INC (namecheap.com)."),
        ("1.3", "Cloudflare (ns*.cloudflare.com)."),
        (
            "2.1",
            "Cloudflare-ren IPv4 bat (adib. 104.26.x.x / 172.67.x.x). IP zehatzak alda daitezke.",
        ),
        (
            "2.2",
            "THM{a5b83929888ed36acb0272971e438d78}",
        ),
        (
            "2.3",
            "Google-ren MX bat, adib. aspmx.l.google.com edo alt1.aspmx.l.google.com.",
        ),
        (
            "3.1",
            "TTL zenbakia ANSWER SECTION-eko bigarren zutabean (adib. 300). Balioa alda daiteke.",
        ),
        ("3.2", "Bai – TXT berdina izan behar du."),
        (
            "3.3",
            "Lehentasun txikiena (normalean 10 tryhackme.com-en MX zerrendan). Egiaztatu irteeran.",
        ),
        (
            "4.1",
            "Informazio publikoa kontsultatzen da (WHOIS/DNS zerbitzari irekiak); "
            "ez zaio paketerik bidaltzen helburuko ostalariari zuzenean.",
        ),
        (
            "4.2",
            "dig: irteera argiagoa, TTL erakusten du, scripting-erako hobea. "
            "nslookup bateragarritasunerako erabilgarria da.",
        ),
        (
            "5",
            "Ikaslearen arabera. Egiaztatu komandoen irteera koherentea den.",
        ),
    ]

    for zb, testua in irtenbideak:
        p = doc.add_paragraph()
        p.add_run(f"{zb}. ").bold = True
        p.add_run(testua)

    irteerak = [
        Path("/workspace/testak/Ezagutze_pasiboa_jarduera_praktikoa.docx"),
        Path("/opt/cursor/artifacts/Ezagutze_pasiboa_jarduera_praktikoa.docx"),
    ]
    for bidea in irteerak:
        bidea.parent.mkdir(parents=True, exist_ok=True)
        doc.save(bidea)
        print(f"Gordeta: {bidea}")


if __name__ == "__main__":
    main()
