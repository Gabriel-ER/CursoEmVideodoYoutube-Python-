numero = int(input('numero:'))
primeiro_anterior=0
segundo_anterior=0
n=0
a0=0
a1=1
a2=1
a3=0
print(a0)
print(a1)
print(a2)
while n < numero:
    a3=a1+a2
    a1=a2
    a2=a3
    n += 1
    print(a3)