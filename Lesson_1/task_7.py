"""
 длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
 составленного из этих отрезков. Если такой треугольник существует, то определить,
 является ли он разносторонним, равнобедренным или равносторонним.
ссылка на блок-схему
https://drive.google.com/file/d/1atWiGM-fDCh3AfOGfYvsJKzIMpdEJZRB/view?usp=sharing
"""

line_1 = int(input('Введите велечину первого отрезка :'))
line_2 = int(input('Введите велечину второго отрезка :'))
line_3 = int(input('Введите велечину третьего отрезка :'))

if line_1 >= line_2 + line_3 or line_2 >= line_1 + line_3 or line_3 >= line_1 + line_2:
    print('Треугольник с заданными отрезками не существует')
elif line_3 == line_1 == line_2:
    print('Треугольник равносторонний')
elif line_3 == line_1 or line_1 == line_2 or line_2 == line_3:
    print('Треугольник равнобедренный')
else:
    print('Треугольник разносторонний')


