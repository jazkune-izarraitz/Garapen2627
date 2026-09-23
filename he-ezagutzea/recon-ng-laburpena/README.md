# recon-ng OSINT laburpena (PPTX)

HE-2 / recon-ng praktikaren laburpena, `datu_atzipenak_laburpena` plantillaren diseinuari jarraituz.

## Fitxategiak

| Fitxategia | Deskribapena |
|---|---|
| `recon-ng-osint-laburpena.pptx` | Aurkezpena (euskara) |
| `hosts.csv` | `example.com` probaren esportazioa (hackertarget) |
| `irudiak/` | Terminalaren pantaila-argazkiak (`show hosts`, `run`) |
| `sortu_pptx.py` | Plantillatik PPTX birsortzeko scripta |

## Plantilla

Iturburua: `datu_atzipenak_laburpena_bd3b.pptx` (Blank layout, Calibri, izenburua + Pausuak + deskribapena + kodea / Courier New).

## Proba laburra

Ingurunean `recon-ng` 5.1.2 erabili da:

```text
workspaces create nire_helburua
marketplace install recon/domains-hosts/hackertarget
modules load recon/domains-hosts/hackertarget
options set SOURCE example.com
run
show hosts
```

Emaitza: `example.com` eta `www.example.com`.  
Oharra: recon-ng 5.1.2-n `db export csv` ez dago; CSV `sqlite3` bidez esportatu da. Klaseko bertsioan `db export csv hosts.csv` erabili.
