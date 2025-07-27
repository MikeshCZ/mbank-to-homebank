# mBank to HomeBank CSV Converter

Tento nástroj převádí výpisy z mBank CZ (CSV) do formátu, který lze přímo importovat do [HomeBank](https://www.gethomebank.org).

---

## ✨ Funkce

- Automaticky detekuje a extrahuje seznam transakcí z mBank výpisu
- Normalizuje formát podle požadavků HomeBank
- GUI: vyber vstupní soubor a cílový název výstupního souboru
- Nepotřebuje žádné přihlašování ani API

## 🖥️ Jak spustit

1. Nainstaluj si Python 3 a [pip](https://pip.pypa.io/)
2. Nainstaluj závislosti:

```bash
pip install -r requirements.txt
```
3.	Spusť nástroj:

```bash
python scr/mbank-to-homebank.py
```
4.	Vyber CSV výpis z mBank (exportovaný z internetového bankovnictví)
5.	Ulož výsledný CSV soubor – připravený pro import do HomeBank

## 📂 Struktura výstupního CSV

Formát odpovídá HomeBank specifikaci:

| Sloupec  | Popis                                |
| -------- | ------------------------------------ |
| date     | Datum transakce (YYYY-MM-DD)         |
| payment  | Typ platby (všude 4 = bank transfer) |
| number   | Číslo dokladu (prázdné)              |
| payee    | Příjemce / obchodník (prázdné)       |
| memo     | Popis operace                        |
| amount   | Částka (kladná nebo záporná)         |
| category | Kategorie z výpisu                   |
| tags     | (prázdné)                            |

## 🛠️ Požadavky

- Python 3.7+
- pandas
- tkinter (součást standardní python knihovny)

## 🧑‍💻 Autor

- [Více o autorovi](https://www.michalsara.cz)

Vytvořeno s cílem zjednodušit import do HomeBank pro české uživatele mBank.

## 💻 Vytvoření desktopové aplikace (Windows / macOS / Linux)

Chceš z tohoto skriptu udělat klasickou aplikaci, kterou si můžeš spouštět jako `.exe` nebo `.app`?
Použij nástroj [PyInstaller](https://pyinstaller.org/), který z Python skriptu vytvoří samostatný spustitelný soubor.

### 🛠️ Jak vytvořit aplikaci

#### Automaticky
 Pro macOS spusť script `build_scripts/build_mac.sh`

#### Ručně

1. Otevři terminál nebo příkazový řádek
2. Nainstaluj PyInstaller (pouze jednou):

   ```bash
   pip install pyinstaller
   ```

3. Vytvoř spustitelný soubor:

   ```bash
   pyinstaller --onedir --windowed --icon=resources/icon.icns --version-file=resources/mbank-to-homebank.version scr/mbank-to-homebank.py
   ```

   - `--onedir` = vše v jedné složce (rychlejší spuštění než onefile; u MacOS je to jedno, vše je v app bundle)
      - lze nahradit `--onefile` = vše zabalené do jednoho `.exe` nebo `.app`
   - `--windowed` = bez konzole (vhodné pro grafické aplikace)
   - `--icon` = přidání ikony pro aplikaci

4. Po dokončení najdeš výsledek ve složce `dist/`:
   - Windows: `mbank_to_homebank/mbank_to_homebank.exe`
   - macOS: `mbank_to_homebank.app`
      - zkopíruj `resources/Info.plist` do `dist/mbank-to-homebank.app/Contents/Info.plist`
   - Linux: spustitelný binární soubor `mbank_to_homebank/mbank_to_homebank`

### 📌 Poznámky

- Na macOS musíš buildovat aplikaci přímo **na macOS** (nelze z Windows)
- Na Linuxu se spustitelný soubor spouští z terminálu:
  ```bash
  ./dist/mbank_to_homebank/mbank_to_homebank
  ```