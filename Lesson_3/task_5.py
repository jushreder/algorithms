'''
5.В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
 Это два абсолютно разных значения.
'''
import random
spam = 10
min_item = -100
max_item = 100

array = [random.randint(min_item, max_item) for _ in range(spam)]
print(array)

spm_min=0
spm_idx=0

for i in array:
    if i < spm_min:
        spm_min = i

for i, spm in enumerate(array):
    if spm<0:
        if spm>spm_min:
            spm_min=spm
            spm_idx=i

print(f'{spm_min} -> {spm_idx}')
