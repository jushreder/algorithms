'''
Подсчитать, сколько было выделено памяти под переменные
в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее
эффективным использованием памяти.
'''

import sys

import random


def spam():
    #  начало кода

    # Вариант 1
    # spam = 10
    # min_item = 0
    # max_item = 100
    #
    # array = [random.randint(min_item, max_item) for _ in range(spam)]
    #
    # print(array)
    #
    # spam_max = array[0]
    # spam_min = array[0]
    # max_ind = 0
    # min_ind = 0
    #
    # for i, item in enumerate(array):
    #     if item > spam_max:
    #         spam_max = item
    #         max_ind = i
    #     if item < spam_min:
    #         spam_min = item
    #         min_ind = i
    #
    # array[max_ind], array[min_ind] = array[min_ind], array[max_ind]
    #
    # print(array)

    # Вариант 2
    N = 10
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(N)]
    print(array)

    idx_min = 0
    idx_max = 0
    for i in range(len(array)):
        if array[i] < array[idx_min]:
            idx_min = i
        elif array[i] > array[idx_max]:
            idx_max = i

    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    print(array)

    # Вариант 3
    # N = 10
    # MIN_ITEM = 0
    # MAX_ITEM = 100
    # array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(N)]
    # print(array)
    #
    # min_num = min(array)
    # max_num = max(array)
    # idx_min = array.index(min_num)
    # idx_max = array.index(max_num)
    # array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    # print(array)

    # конец кода

    item = locals()

    def show_size(x):
        nonlocal total
        total += sys.getsizeof(x)
        # print(f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
        if hasattr(x, '__iter__'):
            if hasattr(x, 'items'):
                for key, value in x.items():
                    show_size(key)
                    show_size(value)
            elif not isinstance(x, str):

                for item in x:
                    show_size(item)

    dict_v = item.values()

    total_s = 0
    while len(item) > 0:
        total = 0
        spm = item.popitem()[-1]
        show_size(spm)
        total_s += total
    print(f'Занятая память - {total_s}')


spam()

# Результаты замера
# Вариант 1    720
# Вариант 2    636
# Вариант 3    664

# Система macOS Catalina ver.10.15 64 разрядная Python 3.7
# По результатам замеров по количеству занятой памяти лучше 2 вариант.
