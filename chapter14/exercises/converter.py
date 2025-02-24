#! python3
import csv
import os, openpyxl

for excelFile in os.listdir('D:\\tmp\\excelSpreadsheets'):
    # Skip non-xlsx files, load the workbook object.
    if excelFile.endswith('.xlsx'):
        filePath = os.path.join('D:\\tmp\\excelSpreadsheets', excelFile)
        wb = openpyxl.load_workbook(filePath)
        for sheetName in wb.sheetnames:
            # Loop through every sheet in the workbook.
            sheet = wb[sheetName]

            # Create the CSV filename from the Excel filename and sheet title.
            csvFile = open('%s_%s.csv' % (excelFile.replace('.xlsx', ''), sheetName), 'w', newline='')
            # Create the csv.writer object for the CSV file.
            writer = csv.writer(csvFile)

            # Loop through every row in the sheet.
            for rowNum in range(1, sheet.max_row + 1):
                rowData = []  # append each cell to this list
                # Loop through each cell in the row
                for colNum in range(1, sheet.max_column + 1):
                    v = sheet.cell(row=rowNum, column=colNum).value
                    # Append each cell's data to rowData
                    rowData.append(sheet.cell(row=rowNum, column=colNum).value)

                # Write the rowData list to the CSV file.
                writer.writerow(rowData)

            csvFile.close()
