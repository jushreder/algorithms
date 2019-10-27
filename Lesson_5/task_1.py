'''
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
 для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
 и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

'''
from collections import defaultdict

c = defaultdict(list)
profit = []
sum_profit = 0
above = []
below = []

hold_len = int(input('Введите количество предприятий в холдинге: '))

for i in range(hold_len):
    name = input(f'Введите название {i + 1} предприятия: ')

    for j in range(4):
        profit.append(int(input(f'Введите прибыль {name} за {j + 1} квартал: ')))
    sum_profit += sum(profit)
    profit.append(sum(profit))
    c[name] = profit.copy()
    profit.clear()

profit_abs = sum_profit / hold_len

for i in c:
    if sum_profit / hold_len > list(c[i])[4]:
        below.append(i)
    else:
        above.append(i)
print(f'Средняя прибыль предприятий в холдинге за год составила {sum_profit / hold_len}.')
print('На предприятии(ях):', *above, '-прибыль выше среднего.')
print('На предприятии(ях):', *below, '-прибыль ниже среднего.')
