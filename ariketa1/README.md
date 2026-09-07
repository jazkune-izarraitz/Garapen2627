# Ariketa 1 – DirektorioZerrenda (Eclipse)

Java proiektua Eclipse-rako prestatuta dago. Klasea `ariketa1` paketean dago.

## Eclipse-n ireki

1. **File → Import… → Existing Projects into Workspace**
2. **Select root directory**: aukeratu `ariketa1` karpeta (ez repo osoa)
3. Proiektua agertuko da: `ariketa1` → **Finish**

## Klase berria sortu

1. Package Explorer-en: `ariketa1` → `src` → `ariketa1` (paketea)
2. Eskuineko klik paketean → **New → Class**
3. **Package** eremuan idatzi: `ariketa1` (ez utzi hutsik)
4. Class name jarri → **Finish**

### "A package name must be specified for a module" errorea

Proiektua `module-info.java`-rekin sortu bada, Eclipse-k **pakete izena derrigorrez** eskatzen du (default package ez da balio).

**Konponbidea (bata aukeratu):**
- Klasea sortzean **Package** eremuan izena jarri (adib. `ariketa1`)
- Edo proiektu berria sortzean **Create module-info.java** desmarkatu
- Edo `module-info.java` ezabatu Package Explorer-etik (ez baduzu modulurik behar)

## Exekutatu

1. Eskuineko klik `DirektorioZerrenda.java`-n → **Run As → Java Application**
2. Argumentuak: **Run → Run Configurations… → Arguments** → adib. `C:\Users`

Terminaletik:
```bash
cd ariketa1
javac -d bin src/ariketa1/DirektorioZerrenda.java
java -cp bin ariketa1.DirektorioZerrenda
java -cp bin ariketa1.DirektorioZerrenda C:\Users
```

## Egitura

```
ariketa1/
  .project
  .classpath
  src/
    ariketa1/                    ← paketea
      DirektorioZerrenda.java
  bin/                           ← Eclipse-k sortzen du
```
