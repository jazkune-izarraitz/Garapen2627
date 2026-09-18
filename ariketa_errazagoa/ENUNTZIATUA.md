# Datu Atzipena — Ariketa 1 (bertsio errazagoa)

**Puntuazioa:** 1.5 puntu  
**Helburua:** Testu-fitxategi bat irakurri (`BufferedReader` / `FileReader`) eta emaitzak kontsolan (eta fitxategian) idatzi.

---

## Deskribapena

Lehenik, `alice.txt` fitxategia lortu (proiektuko `datuak/` karpetan dago).  
"Alice's Adventures in Wonderland" liburuaren zati labur bat da.

Programa bat egin beharko da fitxategi hori irakurri eta kontsolatik datu hauek ematen dituena, **orden honetan**:

1. Fitxategiaren **lerro kopurua**
2. `"Alice"` katea **zenbat lerrotan** azaltzen den
3. `"Alice"` katea **zein lerrotan** azaltzen den
4. `"Alice"` katea azaltzen diren lerroak `"alice-lerroak.txt"` izeneko fitxategian gorde

---

## Nola banatu lana (gomendatua)

Azterketako estiloan, hiru klase progresibo egin ditzakezu:

| Klasea        | Zer egin behar du                         |
|---------------|-------------------------------------------|
| `ariketa1_1`  | Lerro kopurua soilik erakutsi             |
| `ariketa1_2`  | Lerro kopurua + `"Alice"` duten lerroak   |
| `ariketa1_3`  | Aurrekoa + lerroak `alice-lerroak.txt`-en |

---

## Baldintza teknikoak

- Java erabili (`java.io` paketea).
- `BufferedReader` + `FileReader` irakurtzeko.
- `BufferedWriter` + `FileWriter` idazteko (3. zatian).
- Bilaketa: `line.contains("Alice")` nahikoa da (maiuskula/minuskula bereizten du).
- Fitxategiaren bidea proiektuaren erlatiboa izan daiteke, adib.: `datuak/alice.txt`.

---

## Entrega

Zip batean sartu beharrezko guztia:

- Iturburu-kodea (`.java`)
- `alice.txt` (edo nola lortu jakiteko argibidea)
- (Aukerakoa) irteerako `alice-lerroak.txt` adibidea

Proiektu bat ariketa guztientzako izan daiteke, edo proiektu bat ariketako.
