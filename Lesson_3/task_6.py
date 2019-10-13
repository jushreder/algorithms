'''
6.B одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''
import random

spam = 10
min_item = 0
max_item = 100

array = [random.randint(min_item, max_item) for _ in range(spam)]
print(array)

spam_max = array[0]
spam_min = array[0]
max_ind = 0
min_ind = 0

for i, item in enumerate(array):
    if item > spam_max:
        spam_max = item
        max_ind = i
    if item < spam_min:
        spam_min = item
        min_ind = i

spam_sum = 0
if min_ind > max_ind:
    min_ind, max_ind = max_ind, min_ind
if max_ind - min_ind != 1:
    for i in range(min_ind + 1, max_ind):
        spam_sum += array[i]

print(spam_sum)
