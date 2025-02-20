import csv

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])

outputFile.close()
