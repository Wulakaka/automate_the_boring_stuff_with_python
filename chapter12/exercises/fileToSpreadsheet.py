#! python3
import sys, openpyxl
filenames = sys.argv[1:]
wb = openpyxl.Workbook()
sheet = wb.active
for i in range(len(filenames)):
    file = open(filenames[i])
    lines = file.readlines()
    for rowIndex in range(len(lines)):
        sheet.cell(row=rowIndex + 1, column=i+1).value = lines[rowIndex]

wb.save('txt.xlsx')