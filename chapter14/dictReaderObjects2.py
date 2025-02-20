import csv

from chapter13.filePath import filePath

exampleFile = open(filePath('example.csv'))
exampleDictReader = csv.DictReader(exampleFile, ['time', 'name', 'amount'])
for row in exampleDictReader:
    print('Name: ' + row['name'] + ', Amount: ' + row['amount'])
exampleFile.close()
