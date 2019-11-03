'''
 Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
 на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''
import random

item = 21
item_min = 0
item_max = 50
array = [random.uniform(item_min, item_max - 1) for _ in range(item)]  # uniform

print(array)


def merg_sort(lst):
    if len(lst) < 2:
        return lst

    left = merg_sort(lst[:len(lst) // 2])
    right = merg_sort(lst[len(lst) // 2:len(lst)])

    i = j = 0

    result = []
    while i < len(left) or j < len(right):
        if not i < len(left):
            result.append(right[j])
            j += 1
        elif not j < len(right):
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result


print('*' * 80)
print(merg_sort(array))
