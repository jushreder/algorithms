import itertools
from collections import deque
from collections import defaultdict

dict_16 = defaultdict()
spam = [str(i) for i in range(10)] + [chr(i) for i in range(97, 103, 1)]
spam_l = list(itertools.combinations_with_replacement(spam, 2))
for i in spam_l: dict_16[''.join(i)] = hex(int(i[0], 16) + int(i[1], 16))[2:]

itm_1 = input('Введите первое шестнадцатеричное число: ')
itm_2 = input('Введите второе шестнадцатеричное число: ')

a = deque(itm_1)
b = deque(itm_2)


def sum16_(a, b):
    if len(a) > len(b):
        for i in range(abs(len(a) - len(b))):
            b.appendleft('0')
    else:
        for i in range(abs(len(a) - len(b))):
            a.appendleft('0')
    d = deque('0' for _ in range(len(a)))

    def sum16(a, b):
        if a > b: a, b = b, a
        return dict_16[a + b]

    for i in range(-1, -len(a) - 1, -1):
        if len(sum16(a[i], b[i])) > 1:
            if i == -len(a): d.appendleft('0')
            d[i] = sum16(d[i], sum16(a[i], b[i])[-1])[-1]
            d[i - 1] = '1'

        else:
            if len(sum16(sum16(a[i], b[i]), d[i])) > 1:
                if i == -len(a): d.appendleft('0')
                d[i] = sum16(sum16(a[i], b[i]), d[i])[-1]
                d[i - 1] = '1'
            else:
                d[i] = sum16(sum16(a[i], b[i]), d[i])
    return d


def umn(a, b):
    h = deque()
    for i in range(-1, -len(a) - 1, -1):
        # print(i)
        d = deque('0')
        for y in range(int(a[i], 16)):
            d = sum16_(d, b)
        h.append(list(d))
    for i in range(len(h)):
        for y in range(i):
            h[i].append('0')
    spam = deque()
    for i in h:
        spam = sum16_(spam, i)
    return spam


d = sum16_(a, b)
z = umn(deque(itm_1), deque(itm_2))

print(f'{list(deque(itm_1))} + {list(list(deque(itm_2)))} = {list(d)}')
print(f'{list(deque(itm_1))} * {list(list(deque(itm_2)))} = {list(z)}')
