import csv

from chapter13.filePath import filePath

exampleFile = open(filePath('exampleWithHeader.csv'))
exampleDictReader = csv.DictReader(exampleFile)
for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
