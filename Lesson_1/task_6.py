"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
ссылка на блок-схему
https://drive.google.com/open?id=1mF63TYg4UP-sBdyrc4nuAE71Km4-dj2E
"""
var = int(input('Введите номер буквы в алфавите :'))


# в латинском алфавите 26 букв
# ord('a') определяет начальную позицию кода для Юникод
a = ord('a') - 1

letter = chr(a + var)

print(f'Номеру {var} в латинском алфавите соответствует буква "{letter}"')
