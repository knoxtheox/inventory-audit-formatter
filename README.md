# Inventory Audit Formatter

Turns one raw PawnMate physical-inventory export (`inventory_count_###.xls`) into one print-ready audit workbook (`.xlsx`) with four tabs: Reg Discrepancy, Reg Missing, Com Discrepancy and Com Missing.

## Use it

Open the app's GitHub Pages link in any browser, or download `index.html` and double-click it to run it offline.

1. Pick the store.
2. Drop in the PawnMate `.xls` export.
3. Check the line counts, totals and warnings, then click **Download workbook**.

Everything runs in the browser. The export is never uploaded anywhere.

## Change the rules

All report rules (columns, headings, widths, formats, colours and page-header text) are in the `CONFIG` block at the top of `build/template.html`. After editing it, rebuild `index.html`:

```bash
cd build && npm ci && python3 build.py
```

`index.html` has SheetJS Community Edition 0.18.5 (Apache-2.0) and ExcelJS 4.4.0 (MIT) built in, so it works offline.
