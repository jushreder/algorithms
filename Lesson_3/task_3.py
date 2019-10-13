'''
3.В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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

array[max_ind], array[min_ind] = array[min_ind], array[max_ind]

print(array)
