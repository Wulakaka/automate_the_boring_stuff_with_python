tableData = [
    ['apples', 'oranges', 'cherries', 'bananas'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose'],
]


def printTable(tableData):
    colLength = len(tableData)
    rowLength = len(tableData[0])
    colWidths = [0] * colLength
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            length = len(tableData[i][j])
            if i != 0:
                length += 1
            if length > colWidths[i]:
                colWidths[i] = length

    for j in range(rowLength):
        for i in range(colLength):
            print(tableData[i][j].rjust(colWidths[i], ' '), end='')

        print('\n', end='')


printTable(tableData)
