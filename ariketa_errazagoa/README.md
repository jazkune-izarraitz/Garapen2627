# Ariketa errazagoa — Fitxategiak irakurri/idatzi (Java)

Azterketako 1. ariketaren (**Pulp Fiction** / `"fuck"`) bertsio errazagoa.

## Zer dago hemen?

| Fitxategia | Deskribapena |
|------------|--------------|
| `ENUNTZIATUA.md` | Ikasleari emateko ariketa-enuntziatua |
| `datuak/alice.txt` | Sarrerako testua (Alice in Wonderland, laburra) |
| `src/.../ariketa1_1.java` | Soluzioa: lerro kopurua |
| `src/.../ariketa1_2.java` | Soluzioa: `"Alice"` duten lerroak |
| `src/.../ariketa1_3.java` | Soluzioa: irteera `alice-lerroak.txt`-era |

## Nola exekutatu

```bash
cd ariketa_errazagoa
javac -d out src/datu_atzipena_azterketa/*.java
java -cp out datu_atzipena_azterketa.ariketa1_1
java -cp out datu_atzipena_azterketa.ariketa1_2
java -cp out datu_atzipena_azterketa.ariketa1_3
```

## Jatorrizkoarekiko aldeak (errazagoa)

- Testua laburragoa eta eskolan erabilgarria (`alice.txt`)
- Bilatu beharreko hitza argia: `"Alice"` (ez hitz gogorra)
- Fitxategi-bide erlatiboak (`datuak/alice.txt`)
- 1.3-n ez da behar agerpenak lerroan barnean kontatzea
