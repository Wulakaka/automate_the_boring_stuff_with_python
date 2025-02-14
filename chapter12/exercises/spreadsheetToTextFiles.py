#! python3

import sys, openpyxl
wb = openpyxl.load_workbook(sys.argv[1])
sheet = wb.active

fileOrder = 1
for column in sheet.columns:
    cells = list(column)
    # print(cells)
    file = open('text%s.txt' % fileOrder, 'w')
    for cell in cells:
        print(cell.value)
        if cell.value:
            file.write(cell.value)
    file.close()
    fileOrder += 1