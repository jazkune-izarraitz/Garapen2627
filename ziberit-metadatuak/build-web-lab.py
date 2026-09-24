#!/usr/bin/env python3
"""Build ziberit.org lab website: JPGs with GPS + PDFs with Author metadata."""

from pathlib import Path
import subprocess

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent / "webroot"


def make_jpg(path: Path, title: str, color, lat: float, lon: float) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (800, 600), color)
    draw = ImageDraw.Draw(img)
    draw.rectangle((40, 40, 760, 560), outline=(255, 255, 255), width=3)
    draw.text((60, 80), "ZiberIT", fill=(255, 255, 255))
    draw.text((60, 140), title, fill=(255, 255, 255))
    draw.text((60, 200), f"GPS: {lat:.5f}, {lon:.5f}", fill=(230, 230, 230))
    img.save(path, "JPEG", quality=90)

    # EXIF GPS via exiftool (decimal degrees)
    subprocess.run(
        [
            "exiftool",
            "-overwrite_original",
            f"-GPSLatitude={abs(lat)}",
            f"-GPSLatitudeRef={'N' if lat >= 0 else 'S'}",
            f"-GPSLongitude={abs(lon)}",
            f"-GPSLongitudeRef={'E' if lon >= 0 else 'W'}",
            str(path),
        ],
        check=True,
        capture_output=True,
    )


def make_pdf(path: Path, title: str, author: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(path), pagesize=A4)
    c.setTitle(title)
    c.setAuthor(author)
    c.setSubject("ZiberIT laborategia")
    c.drawString(72, 800, "ZiberIT – Dokumentu laburra")
    c.drawString(72, 780, title)
    c.drawString(72, 760, f"Egilea: {author}")
    c.drawString(72, 730, "Dokumentu hau metadatuen analisiko praktikarako da.")
    c.showPage()
    c.save()


def write_index(directory: Path, heading: str, files: list[str]) -> None:
    links = "\n".join(f'  <li><a href="{name}">{name}</a></li>' for name in files)
    directory.joinpath("index.html").write_text(
        f"""<!DOCTYPE html>
<html lang="eu">
<head><meta charset="utf-8"><title>{heading}</title></head>
<body>
<h1>{heading}</h1>
<ul>
{links}
</ul>
</body>
</html>
""",
        encoding="utf-8",
    )


def main() -> None:
    if ROOT.exists():
        for p in ROOT.rglob("*"):
            if p.is_file():
                p.unlink()
    ROOT.mkdir(parents=True, exist_ok=True)

    # --- images/ (GPS) ---
    images = [
        ("images/donostia-kursaal.jpg", "Kursaal – Donostia", (20, 90, 140), 43.3247, -1.9780),
        ("images/bilbao-guggenheim.jpg", "Guggenheim – Bilbo", (120, 40, 40), 43.2687, -2.9340),
        ("images/gasteiz-plaza.jpg", "Andra Mari Plaza – Gasteiz", (40, 110, 60), 42.8467, -2.6716),
    ]
    for rel, title, color, lat, lon in images:
        make_jpg(ROOT / rel, title, color, lat, lon)
    write_index(ROOT / "images", "ZiberIT – Irudiak", [p[0].split("/")[-1] for p in images])

    # --- docs/ (PDF authors; one author repeated to test uniqueness) ---
    docs = [
        ("docs/memoria-teknikoa.pdf", "Memoria teknikoa", "Ane Goikoetxea"),
        ("docs/txostena-segurtasuna.pdf", "Segurtasun txostena", "Mikel Arriola"),
        ("docs/aurrekontua.pdf", "Aurrekontua 2026", "Laura Sanchez"),
        ("docs/eranskina.pdf", "Eranskina A", "Ane Goikoetxea"),  # errepikatua
    ]
    for rel, title, author in docs:
        make_pdf(ROOT / rel, title, author)
    write_index(ROOT / "docs", "ZiberIT – Dokumentuak", [p[0].split("/")[-1] for p in docs])

    # --- download/ (nahasketa) ---
    make_jpg(ROOT / "download/egoitza.jpg", "Egoitza nagusia", (80, 80, 120), 43.2627, -2.9253)
    make_pdf(ROOT / "download/gida.pdf", "Erabiltzaile gida", "Jon Etxebarria")
    write_index(
        ROOT / "download",
        "ZiberIT – Deskargak",
        ["egoitza.jpg", "gida.pdf"],
    )

    # Root index
    (ROOT / "index.html").write_text(
        """<!DOCTYPE html>
<html lang="eu">
<head><meta charset="utf-8"><title>ZiberIT</title></head>
<body>
<h1>ZiberIT</h1>
<p>Enpresaren webgune ofiziala (laborategia).</p>
<ul>
  <li><a href="/images/">images</a></li>
  <li><a href="/docs/">docs</a></li>
  <li><a href="/download/">download</a></li>
</ul>
</body>
</html>
""",
        encoding="utf-8",
    )

    print(f"Webroot sortuta: {ROOT}")
    for f in sorted(ROOT.rglob("*")):
        if f.is_file():
            print(f"  {f.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
