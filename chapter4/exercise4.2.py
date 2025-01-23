grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def main(list):
    str = []
    for i in range(len(list)):
        for j in range(len(list[i])):
            if(i == 0):
                str.append('')
            str[j] += list[i][j]

    for i in range(len(str)):
        print(str[i])

# main(grid)

def main2(list):
    i = len(list)
    j = len(list[0])
    for k in range(j):
        for l in range(i):
            if l == i-1:
              print(list[l][k])
            else:
                print(list[l][k], end='')
        
main2(grid)    
