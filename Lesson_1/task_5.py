'''
Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
ссылка на блок-схему
https://drive.google.com/open?id=1632eAd5ubwVAjD4mJez9Aks8ZkpMn3wy
'''

letter_1 = input('Введите первую букву :')

letter_2 = input('Введите вторую букву :')

poz_0 = ord("a") - 1

poz_1 = ord(letter_1) - poz_0
poz_2 = ord(letter_2) - poz_0

quantity = abs(poz_1 - poz_2) - 1

print(f"Буква '{letter_1}' занимает {poz_1} место, \n"
      f"Буква '{letter_2}' занимает {poz_2} место, \n"
      f"между ними находятся {quantity} букв.")
