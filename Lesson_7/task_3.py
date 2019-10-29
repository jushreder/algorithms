'''
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
'''
import random

item = 3
item_min = 0
item_max = 100
array = [random.randint(item_min, item_max) for _ in range(item * 2 + 1)]

print('Вариант 1')
print(array)


def Cocktail_sort(lst):
    left = 0
    rigth = len(lst) - 1

    while left <= rigth:
        for i in range(left, rigth, 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        rigth -= 1
        for i in range(rigth, left, -1):
            if lst[i - 1] > lst[i]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
        left += 1
    return lst


print(f'Медиана: {Cocktail_sort(array)[len(array) // 2]}')

array = [random.randint(item_min, item_max) for _ in range(item * 2 + 1)]

print('Вариант 2')
print(array)


def median(lst, k, support=random.choice):
    spam = support(lst)
    lows = [i for i in lst if i < spam]
    highs = [i for i in lst if i > spam]
    pivots = [i for i in lst if i == spam]

    if k < len(lows):
        return median(lows, k, support)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return median(highs, k - len(lows) - len(pivots), support)


print(f'Медиана: {median(array, len(array) // 2)}')
