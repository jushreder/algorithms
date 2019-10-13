'''
7.В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
(оба являться минимальными), так и различаться.
'''
import random

spam = 20
min_item = 0
max_item = 100

array = [random.randint(min_item, max_item) for _ in range(spam)]

print(array)

min_itm1 = array[0]
min_itm2 = array[0]

for i in array:
    if min_itm2 > i:
        min_itm2 = i
        if min_itm2 < min_itm1:
            min_itm2, min_itm1 = min_itm1, min_itm2

print(min_itm1, min_itm2)
