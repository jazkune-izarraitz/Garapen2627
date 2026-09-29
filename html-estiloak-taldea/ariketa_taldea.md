# Ariketa taldeka: estiloak web orrietatik

**Gaia:** HTML + **CSS kanpoko fitxategia** (`estiloa.css`)  
**Taldeak:** 3–4 ikasle  
**Denbora orientagarria:** 2–3 saio

---

## Helburua

Talde bakoitzak **3 orriko web txiki bat** sortuko du. Orri bakoitzak **interneteko (edo klasean aztertutako) web baten estilo-ideia** izango du, baina edukia **zuena** izango da (ez kopiatu testuak edo irudiak copyrightpekoak).

Kanpoko CSS fitxategi **bakar** bat erabili behar da (`estiloa.css`), guztientzat.

---

## Taldearen antolaketa

| Rol | Zeregina |
|-----|----------|
| **Koordinatzailea** | Egitura HTMLa koherentea, estekak ondo, `estiloa.css` elkarrekin bateratzen |
| **Orri 1 – «Hasiera»** | Nabigazioa + hero / titulua (web **A** motako estiloa) |
| **Orri 2 – «Edukia»** | Zerrendak, kartak edo taula (web **B** motako estiloa) |
| **Orri 3 – «Harremana»** | Formularioa edo kontaktu blokea (web **C** motako estiloa) |

3 ikasleko taldean: koordinatzaileak orri bat ere egiten du. 4 ikasleko taldean: rolak banatuta.

---

## Web erreferentziak (klasean ikusi dituzuenak)

Talde bakoitzak **3 web desberdin** aukeratu (irakasleak onartu edo zerrenda batetik). Adibideak:

| Web mota | Adibideak (ideia, ez kopiatu) | CSS propietate / kontzeptu tipikoak |
|----------|-------------------------------|-------------------------------------|
| **A – Berri / bloga** | egunkari online, blog bat | `font-family`, `line-height`, `color`, `max-width`, `:hover` esteketan |
| **B – Erosketa / zerrenda** | dendaren katalogoa, menua | `display: flex`, `gap`, `border`, `border-radius`, `box-shadow`, `padding` |
| **C – Erakundea / ikastola** | LH, udaletxea, elkartea | goiburuko koloreak, `background-color`, logo + menu horizontal |
| **D – App / SaaS** | tresna baten hasiera-orria | gradientea, botoi handia, `text-align: center`, `margin` |
| **E – Wikipedia / dokumentazioa** | artikulu luzea | `h1`–`h3` hierarkia, `list-style`, `border-left` aipamenetan |

**Baldintza:** talde bakoitzak **A, B eta C mota desberdinak** erabili behar ditu (edo irakasleak emandako 3 mota).

---

## Entregatu beharrekoak

1. **`index.html`** – Hasiera (menua beste bi orrietara)
2. **`edukia.html`** (edo izen egokia) – Bigarren orria
3. **`harremana.html`** (edo izen egokia) – Hirugarren orria
4. **`css/estiloa.css`** – Estilo guztiak hemen (inline `style=` **debekatua**)
5. **`README.txt`** (4–6 lerro): zein web izan diren inspirazioa (URL + zer propietate kopiatu duzue)

Oinarria: [plantilla/](plantilla/) karpetatik has dezakezue.

---

## CSS propietateak erabili behar dira (gutxienez)

Taldeak **gutxienez 12 propietate desberdin** erabili behar ditu `estiloa.css`-en. Klasean landu dituzuenak, adibidez:

- **Testua:** `font-family`, `font-size`, `font-weight`, `color`, `text-align`, `text-decoration`, `line-height`
- **Kutxa:** `width`, `max-width`, `height`, `margin`, `padding`, `border`, `border-radius`
- **Atzeko planoa:** `background-color`, `background-image` (aukerakoa)
- **Layout:** `display` (`block`, `inline`, `flex`), `flex-direction`, `justify-content`, `align-items`, `gap`
- **Efektuak:** `:hover`, `box-shadow`, `opacity` (aukerakoa)

CSS fitxategian **komentarioak** jarri:

```css
/* Ana – index.html – blog motako tipografia */
```

---

## HTML baldintzak

- `<!DOCTYPE html>`, `lang="eu"` (edo `es`)
- `<meta charset="UTF-8">`
- `<title>` desberdin orri bakoitzean
- `<link rel="stylesheet" href="css/estiloa.css">` **head**-ean
- Nabigazio `<nav>` estekak `<a href="...">` (fitxategi erlatiboak)
- Gutxienez: `header`, `main`, `footer`; eduki semantikoa (`section`, `article` edo `aside` bat)

---

## Taldeko lan-fluxua (gomendioa)

1. **15 min** – Aukeratu 3 web erreferentzia; zer propietate erabiliko diren idatzi.
2. **20 min** – HTML eskeletoa (plantilla), estekak probatu.
3. **40 min** – CSS banaka atal bakoitza; koordinatzaileak bateratu.
4. **15 min** – Proba nabigatzailean, README idatzi, entrega.

---

## Ebaluazioa (orientagarria)

| Irizpidea | Puntuazioa |
|-----------|------------|
| 3 orri + nabigazioa + CSS kanpokoa | /4 |
| 3 estilo-mota desberdin argi ikusita | /3 |
| ≥12 propietate + `:hover` bat | /3 |
| HTML semantikoa, kode garbia, README | /2 |
| Talde-lana (komentarioak CSS-n, banaketa) | /2 |

**Gehikuntza:** irudi bat (`<img>` + `alt`), formularioa (`<form>`, `<input>`, `<label>`), edo `@media` sinple bat (mugikorra).

---

## Oharrak ikasleentzat

- **Ez** kopiatu web baten CSS osoa; **inspiratu** kolore, tarte eta layout ideiak.
- Koloreak: hex (`#1a4a6e`) edo `rgb()` — klasean ikasi duzuen moduan.
- Fitxategi-izenak: letra xeheak, azenturik gabe (`edukia.html`).

---

## Irakaslearentzat

- Taldeak sortzeko: zenbaki edo karta (A/B/C mota banatu desberdintasuna bermatzeko).
- Entrega: karpeta bat Moodle/Teams-en edo Git branch bat (Garapen2627).
- Plantilla: [plantilla/](plantilla/) — ez du estilorik; soilik egitura.
