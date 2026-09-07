# Ariketa 1 – DirektorioZerrenda (Eclipse)

Java proiektua Eclipse-rako prestatuta dago.

## Eclipse-n ireki

1. **File → Import… → Existing Projects into Workspace**
2. **Select root directory**: aukeratu `ariketa1` karpeta (ez repo osoa)
3. Proiektua agertuko da: `ariketa1` → **Finish**

## Klase berria sortu

1. Package Explorer-en ireki `ariketa1` → `src`
2. Eskuineko klik `src`-n → **New → Class**
3. Izena jarri eta **Finish**

> Oharra: `New → Class` desgaituta badago, proiektua ez da Java proiektua.
> Orduan inportatu berriro `ariketa1` karpeta (`.project` fitxategia duena), ez `Garapen2627` erroa.

## Exekutatu

1. Eskuineko klik `DirektorioZerrenda.java`-n → **Run As → Java Application**
2. Argumentuak: **Run → Run Configurations… → Arguments** → adib. `C:\Users`

## Egitura

```
ariketa1/
  .project      ← Eclipse Java proiektua
  .classpath
  src/          ← iturburu karpeta (hemen sortu klaseak)
    DirektorioZerrenda.java
  bin/          ← konpilazioa (Eclipse-k sortzen du)
```
