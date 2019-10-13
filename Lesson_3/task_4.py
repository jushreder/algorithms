'''
4.Определить, какое число в массиве встречается чаще всего.
'''
import random

spam = 300
min_item = -100
max_item = 100

array = [random.randint(min_item, max_item) for _ in range(spam)]
print(array)

spam = set(array)
max_a = 0
itm_max = 0
for itm in spam:
    a = 0
    for i in array:
        if itm == i:
            a += 1
    if a > max_a:
        max_a = a
        itm_max = itm

print(f'{itm_max} -> {max_a}')
