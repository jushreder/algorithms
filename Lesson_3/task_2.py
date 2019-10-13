'''
2.Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
'''
import random

spam = 20
min_item = 0
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(spam)]
print(array)

spam_list = list()

for i, item in enumerate(array):
    if item % 2 == 0:
        spam_list.append(i)
print(spam_list)
