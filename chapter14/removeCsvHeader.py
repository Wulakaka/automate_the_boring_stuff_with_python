#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.

import csv, os
os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.

for csvFilename in os.listdir('D:\\tmp\\removeCsvHeader'):
    if not csvFilename.endswith('.csv'):
        continue

    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file in (skipping first row).
    csvRows = []
    csfFileObj = open(os.path.join('D:\\tmp\\removeCsvHeader', csvFilename))
    readerObj = csv.reader(csfFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue  # skip first row
        csvRows.append(row)

    # Write out the CSV file.
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()