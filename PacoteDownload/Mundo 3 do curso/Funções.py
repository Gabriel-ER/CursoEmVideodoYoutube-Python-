"""def soma(a,b):
    print(f'A = {a} e B = {b}')
    print(a+b)


soma(b=4,a=5)
soma(4,5)"""

# empacotamento de parâmetros
'''def contador(*num):
    # È uma tupla:
    print(num)


contador(2,3,4)
contador(1,2)'''

'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)


lista = [1, 2, 3, 4]
dobra(lista)'''

def soma(*num):
    s = 0
    for n in num:
        s += n
    print(s)

soma(2,3)
soma(2,5,6)

