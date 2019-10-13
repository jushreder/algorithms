'''
9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''
import random

line = 4
min_item = 0
max_item = 100
matrix = [[random.randint(min_item, max_item) for _ in range(line)] for _ in range(line)]
print(*matrix, sep='\n')

min_column = matrix[0]
for itm in matrix:
    for i in range(len(itm)):
        if itm[i] < min_column[i]:
            min_column[i] = itm[i]

max_itm = min_column[0]
for itm in min_column:
    if itm > max_itm:
        max_itm = itm

print(f'Mаксимальный элемент среди минимальных элементов столбцов матрицы {max_itm}')
