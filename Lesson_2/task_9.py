'''
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
 Вывести на экран это число и сумму его цифр.

'''
int_max = 0
summa_max = 0

while True:
    summa_int = 0
    a = int(input('Введите натуральное число: '))
    if a > 0:
        b = a
        while a > 0:
            summa_int += a % 10
            a = a // 10
        if summa_int > summa_max:
            summa_max = summa_int
            int_max = b
    else:
        print('Ввод завершен.')
        print(f'максимальная сумм цифр {summa_max} у числа {int_max}')
        break
