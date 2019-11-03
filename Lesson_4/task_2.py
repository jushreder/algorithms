'''
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
'''
# с помощью алгоритма «Решето Эратосфена»
import timeit
import cProfile


def eratos(item):
    sieve = [i for i in range(item * 20)]
    sieve[1] = 0
    check = 0
    i = 2
    while i <= item * 20:
        if sieve[i] != 0:
            check += 1
            if check == item:
                return sieve[i]

            for j in range(i, item * 20, i):
                sieve[j] = 0
        i += 1


s = '''
def eratos(item):
    sieve = [i for i in range(item * 20)]
    sieve[1] = 0
    check = 0
    i = 2
    while i <= item * 20:
        if sieve[i] != 0:
            check += 1
            if check == item:
                return sieve[i]

            for j in range(i, item * 20, i):
                sieve[j] = 0
        i += 1
eratos(1600)
'''


# print(timeit.timeit(s, number=1000))

# 0.44520931799999997 = 100
# 0.9560842460000001 = 200
# 2.0020079760000002 = 400
# 4.165446174 = 800
# 8.705279014 = 1600

# cProfile.run('eratos(100000)')
# =100
#         1    0.000    0.000    0.001    0.001 task_2.py:12(eratos)
#         1    0.000    0.000    0.000    0.000 task_2.py:13(<listcomp>)
# =1000
#         1    0.006    0.006    0.007    0.007 task_2.py:12(eratos)
#         1    0.002    0.002    0.002    0.002 task_2.py:13(<listcomp>)
# = 10000
#         1    0.061    0.061    0.079    0.079 task_2.py:12(eratos)
#         1    0.018    0.018    0.018    0.018 task_2.py:13(<listcomp>)
# = 100000
#         1    0.893    0.893    1.004    1.004 task_2.py:12(eratos)
#         1    0.112    0.112    0.112    0.112 task_2.py:13(<listcomp>)


# без использования «Решета Эратосфена».

def prim(num):
    for j in range(2, num):
        if num % j == 0:
            return 0
    return num


def prima_n(item):
    num = 2
    prima_ind = 0
    prima_num = 0
    while prima_ind != item:
        if prim(num) > 0:
            prima_ind += 1
            prima_num = num
        num += 1
    return prima_num


# print(prima_n(541))


s = '''
def prim(num):
    for j in range(2, num):
        if num % j == 0:
            return 0
    return num

def prima_n(item):
    num = 2
    prima_ind = 0
    prima_num = 0
    while prima_ind != item:
        if prim(num) > 0:
            prima_ind += 1
            prima_num = num
        num += 1
    return prima_num

prima_n(800)
'''

# print(timeit.timeit(s, number=1000))
# 1.753341966 = 100
# 8.179466199999998 = 200
# 40.032197986 = 400
# 185.399475801 = 800

# cProfile.run('prima_n(800)')
# = 100
#       540    0.005    0.000    0.005    0.000 task_2.py:72(prim)
#         1    0.000    0.000    0.005    0.005 task_2.py:78(prima_n)
# = 200
#      1222    0.011    0.000    0.011    0.000 task_2.py:72(prim)
#         1    0.001    0.001    0.012    0.012 task_2.py:78(prima_n)
# = 400
#      2740    0.046    0.000    0.046    0.000 task_2.py:72(prim)
#         1    0.001    0.001    0.047    0.047 task_2.py:78(prima_n)
# = 800
#      6132    0.287    0.000    0.287    0.000 task_2.py:72(prim)
#         1    0.003    0.003    0.289    0.289 task_2.py:78(prima_n)


'''
Вывод: алгоритм  с использованием «Решето Эратосфена» работает значительно быстрее (3-4) раза
'''
