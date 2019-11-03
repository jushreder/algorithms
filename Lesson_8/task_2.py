from collections import Counter, namedtuple


class My_Node:
    def __init__(self, l=None, r=None):
        self.l = l
        self.r = r

    def rez(self, code, stp):
        self.l.rez(code, stp + "0")
        self.r.rez(code, stp + "1")


class My_Leaf(namedtuple('Leaf', ['char'])):
    def rez(self, code, stp):
        code[self.char] = stp or '0'


def bubble(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j][0] < lst[j + 1][0]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def code_huffman(item):
    h = []
    for ch, freq in Counter(item).most_common():
        h.append((freq, My_Leaf(ch)))

    while len(h) > 1:
        lef = h.pop()
        rig = h.pop()
        h.append([lef[0] + rig[0], My_Node(lef[1], rig[1])])
        bubble(h)

    code = {}

    if h:
        [(spam, root)] = h
        root.rez(code, "")

    return code


def decode_huffman(dec, code):
    point = 0
    result = ''
    while point < len(dec):
        for spam in code.keys():
            if dec.startswith(code[spam], point):
                result += spam
                point += len(code[spam])
    return result


item = 'Спасибо за алгоритмы!'
# item= input('Введите строку: ')
code = code_huffman(item)
# for ch in code:
#     print(f'<{ch}>  {code[ch]}')

encode = ''.join(code[ch] for ch in item)
decode = decode_huffman(encode, code)

print(f'Строка: {item}\n Закодировали: <{encode}>\nРаскодировали: <{decode}>')
