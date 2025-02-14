#! python3
# freeze.py - Freezes the top row of a spreadsheet.

import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active
sheet.freeze_panes = 'A2'  # Freeze the rows above A2.
wb.save('freezeExample.xlsx')
