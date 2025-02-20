import csv

from chapter13.filePath import filePath

exampleFile = open(filePath('example.csv'))
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)
print(exampleData[0][0])