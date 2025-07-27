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
python scr/main.py
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
- tkinter (součást standardní knihovny)

## 🧑‍💻 Autor

- [Více o autorovi](https://www.michalsara.cz)

Vytvořeno s cílem zjednodušit import do HomeBank pro české uživatele mBank.
