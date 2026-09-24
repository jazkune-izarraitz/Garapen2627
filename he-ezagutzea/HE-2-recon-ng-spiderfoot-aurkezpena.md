# Ezagutzea — recon-ng eta SpiderFoot
**Hacking etikoa** · Aurkezpena (HE-2 formatua)  
Nabigazioa HTML bertsioan: geziak / zuriunea.

---

## Diapositiba 1 — Titulua
**Ezagutzea (Footprinting)**  
Tresnak: recon-ng eta SpiderFoot  
Hacking etikoa — Kali Linux

---

## Diapositiba 2 — Testuingurua
- Ezagutze fasean informazio publikoa biltzen dugu (OSINT).
- Lan errepikakorrak automatizatu daitezke.
- Gaur: komando-lerroko / web tresna bi.

---

## Diapositiba 3 — Zertarako balio dute?
- Domeinuei, webguneei, korreoei… buruzko datuak biltzeko.
- Beste zerbitzuen **API**-ak bateratzeko toki bakarrean.
- Eskuz orduak hartuko luketen bilaketak errazteko.

---

## Diapositiba 4 — Zer informazio
- Azpidomeinuak eta hostak
- IP helbideak
- Korreo helbideak
- DNS / WHOIS / web teknologia
- Sare sozialetako arrastoak

---

## Diapositiba 5 — API key-ak
- Emaitza onak lortzeko, askotan **API key** behar da.
- Zerbitzu horietan erregistratu behar gara.
- Doako planak egon daitezke; batzuetan ez.
- Key gabe: modulu batzuk hutsik edo mugatuta.

---

## Diapositiba 6 — API adibideak
- **Hunter.io** — korreo bilaketa
- **Shodan** — Interneteko host/portuak
- **HackerTarget** — azpidomeinuak (maiz key gabe / muga)
- GitHub, Virustotal…

---

## Diapositiba 7 — recon-ng (titulua)
OSINT framework — komando-lerroa

---

## Diapositiba 8 — Zer da
- Kali-n instalatuta etortzen den tresna.
- Moduluetan oinarritutako framework-a.
- Emaitzak workspace / datu-basean gordetzen ditu.

---

## Diapositiba 9 — Nabigazioa
**Workspaces** → proiektua / helburua  
**Modules** → bilaketa-tresna bakoitza  

Mailaka mugitzen gara; maila bakoitzean aukera desberdinak.

---

## Diapositiba 10 — Abiarazi Kali-n
```bash
sudo apt update
sudo apt install recon-ng
recon-ng
```

---

## Diapositiba 11 — Zeregina
1. Workspace bat sortu  
2. Modulu pare bat kargatu  
3. Domeinu baten gainean exekutatu  
4. Emaitzarik ez → beste domeinu / modulu  

---

## Diapositiba 12 — Komandoak
```text
workspaces create nire_helburua
marketplace install recon/domains-hosts/hackertarget
modules load recon/domains-hosts/hackertarget
options set SOURCE example.com
run
show hosts
```

---

## Diapositiba 13 — Keys
```text
keys add hunter_io ZURE_API_KEY
keys add shodan_api ZURE_API_KEY
keys list
```

---

## Diapositiba 14 — Emaitza adibidea
`show hosts` ostean, adibidez:
- www.example.com → 93.184.216.34
- mail.example.com → 93.184.216.55
- blog.example.com → 93.184.216.71

---

## Diapositiba 15 — Esportatu
```text
db export csv hosts.csv
```
Txostenarekin batera igo.

---

## Diapositiba 16 — SpiderFoot (titulua)
OSINT automatizatua — web interfazea

---

## Diapositiba 17 — Zer da
- OSINT bilaketa automatikoa (footprint).
- 2022an Intel 471-ek erosi; fork eguneratua GitHub-en.
- Web UI batekin erabiltzen da.  
https://github.com/poppopjmp/spiderfoot

---

## Diapositiba 18 — Docker
- Klasean Docker erabiliko dugu.
- Dokumentazioaren urratsak jarraitu.
- Nabigatzailean web interfazea.

---

## Diapositiba 19 — Docker adibidea
```bash
docker pull poppopjmp/spiderfoot
docker run -p 5001:5001 poppopjmp/spiderfoot
```
`http://127.0.0.1:5001`

---

## Diapositiba 20 — Zeregina SpiderFoot
- Footprint eskaneo bat domeinuaren gainean
- hunter.io API key konfiguratu
- Moduluak ikusi + beste zerbitzu batean erregistratu
- Eskaneo: hunter.io + aukeratutako modulua

---

## Diapositiba 21 — Emaitza adibidea
Helburua: example.com  
· Email: info@…, support@…  
· Azpidomeinuak, DNS/IP, web teknologia  
· Grafikoan nodoak eta loturak

---

## Diapositiba 22 — Entrega
- Dokumentua: urratsak + informazioa
- Pantaila-argazkiak
- Esportazioak erantsi

---

## Diapositiba 23 — Etika
- Iturri publikoak eta legezkoak.
- Helburu propioak edo baimenduak.
- API key-ak ez partekatu txostenean.

---

## Diapositiba 24 — Galderak?
Praktikak: Kali (recon-ng) eta Docker (SpiderFoot)
