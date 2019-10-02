"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
ссылка на блок-схему
https://drive.google.com/open?id=1SDJ8ottzFMCKbFzHZ5XUIOrh8JImSgje
"""

var = int(input('Введите трехзначное число :'))

int1 = var%10
int2 = (var//10)%10
int3 = (var//100)%10


summ = int1 + int2 + int3
comp = int1 * int2 * int3

print(f'Сумма   цифр  числa {var}     равна: {summ},\n'
      f'произведение цифр числa {var} равнo: {comp}')
