#usando uma flag
n = 0
s = 0
while True:
    n = int(input("Digite seu número:"))
    if n == 999:
        break #parte importante
    s += n
print(s)

#novo jeito de printar: f strings
fruta='maçã'
preco=10
print(f'A fruta é {fruta} e custa {preco}')