'''
8.Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать
ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
'''
line = 4
col = 5

matrix = [[0 for _ in range(line)] for _ in range(col)]

for i in range(col):
    for y in range(line - 1):
        itm = input(f'введите {y} элемент  {i} строки матрицы:')
        matrix[i][y] = int(itm)
        matrix[i][line - 1] += int(itm)

print(*matrix, sep='\n')
