# Invoice Matcher - Zadání

## Co postavit
Webová aplikace pro párování faktur s platbami z platebního terminálu.

## Funkce
- Upload více souborů s fakturami (.xls, .xlsx) — formát viz níže
- Upload více souborů s platbami (.xls — HTML export z banky) — formát viz níže
- Spárování plateb k fakturám
- Zobrazení výsledků v přehledné tabulce
- Export výsledků do .xlsx s barevným označením

## Logika párování
- Platba se párovací k faktuře podle: **stejná částka** + **časová blízkost** (platba přijde 0–10 min před vystavením faktury)
- Variabilní symbol v platbách bývá prázdný — nelze použít
- Jedna platba = jedna faktura

## Výstupní stavy
### Faktury:
- `Zaplaceno` — nalezena odpovídající platba
- `Nezaplaceno` — žádná odpovídající platba nenalezena

### Platby:
- `Přiřazená` — spárována s fakturou
- `Nepřiřaditelná` — žádná faktura nenalezena (manuální kontrola)

## Formát faktur (CSV/XLS sloupce)
Číslo, Vystaveno (datum+čas), Odběratel, Celkem k úhradě, Celkem s DPH, Měna, Variabilní symbol, atd.

## Formát plateb (HTML jako .xls — bankovní export)
Datum a hodina transakce, Částka transakce brutto, Kód autorizace, Variabilní symbol, atd.
Header je na řádku 2 (index).

## Tech stack
- Backend: FastAPI (Python 3.9+)
- Frontend: jednoduchý HTML/JS (vanilla, žádný framework)
- Python venv: /Users/Robai/.venv (pandas, openpyxl, lxml, python-calamine nainstalované)
- Spouštění: uvicorn app:app --host 0.0.0.0 --port 8080

## Existující párování skript (referenční logika)
viz /Users/Robai/match_invoices.py
