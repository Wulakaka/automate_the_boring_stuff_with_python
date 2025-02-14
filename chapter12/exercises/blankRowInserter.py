#! python3
# blankRowInserter.py
# Usage: python blankRowInserter.py 3 2 myProduce.xlsx
import os.path
import sys, openpyxl, re


def blankRowInserter(N, M, file):
    wb = openpyxl.load_workbook(file)
    basename = os.path.basename(file)
    regex = re.compile(r'(.*?).xlsx')
    filename = regex.match(basename)[1]

    sheet = wb.active
    newWb = openpyxl.Workbook()
    newSheet = newWb.active
    for row in sheet.rows:
        for cell in list(row):
            if cell.row < N:
                newSheet.cell(row=cell.row, column=cell.column).value = cell.value
            else:
                newSheet.cell(row=cell.row + M, column=cell.column).value = cell.value
    newWb.save('%s_copy.xlsx' % (filename))


if len(sys.argv) == 4:
    (N, M, file) = sys.argv[1:]
    blankRowInserter(int(N), int(M), file)
