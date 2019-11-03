import hashlib

def str(item):
    if len(item)==1:
        return f'в < {item} > нет подстрок'
    elif len(item)==0:
        return 'введена пустая строка'
    spam=set()
    n=0
    while len(item)>n:
        for i in range(n,len(item)):
            if hashlib.sha1(item.encode('utf-8')).hexdigest() != hashlib.sha1(item[n:i+1].encode('utf-8')).hexdigest():
                spam.add(hashlib.sha1(item[n:i+1].encode('utf-8')).hexdigest())
        n+=1
    return f'В < {item} >  {len(spam)} подстрок, не включая пустую строку и строку целиком.'


item= input('Введите строку: ')
print(str(item))

