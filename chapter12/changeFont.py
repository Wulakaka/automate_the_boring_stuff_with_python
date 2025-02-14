#! python3

import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb['Sheet']
italic24Font = Font(size=24, italic=True)  # Create a Font object.
sheet['A1'].font = italic24Font  # Apply the Font object to A1.
sheet['A1'] = 'Hello, world!'
wb.save('styled.xlsx')
