# Audit Report Formatter

Turns a raw PawnMate count export (`inventory_count_###.xls`) into a print-ready audit workbook (`.xlsx`). Choose the audit on the landing page, then drop in the export.

| Audit | Compared against | Output tabs |
| --- | --- | --- |
| Inventory | Sellable inventory | Reg Discrepancy, Reg Missing, Com Discrepancy, Com Missing |
| Pawn | Open pawns and buys | Pawn Missing, Pawn Discrepancy, Not On Pawn |
| Layaway | Open layaways | Layaway Missing, Layaway Discrepancy, Not On Layaway |

The app checks the export's first line ("...not found in Sellable / Open Pawns And Open Buys / Layaways") and stops if the file doesn't match the audit you picked.

## Use it

Open the app's GitHub Pages link in any browser, or download `index.html` and double-click it to run it offline. Direct links: `#inventory`, `#pawn`, `#layaway`.

1. Choose the audit.
2. Pick the store.
3. Drop in the PawnMate `.xls` export.
4. Check the line counts, totals and warnings, then click **Download workbook**.

Everything runs in the browser. The export is never uploaded anywhere.

## Change the rules

All rules are in the config blocks at the top of `build/template.html`:

- `SHARED`: stores, Excel styling and print setup, used by every audit
- `COLUMNS`: every column a report can use (heading, width, format)
- `FLAGS`: automatic row notes such as "Scanned twice - found"
- `AUDITS`: one block per audit (source tabs, columns, output tabs, flags)

After editing, rebuild `index.html`:

```bash
cd build && npm ci && python3 build.py
```

`index.html` has SheetJS Community Edition 0.18.5 (Apache-2.0) and ExcelJS 4.4.0 (MIT) built in, so it works offline.
