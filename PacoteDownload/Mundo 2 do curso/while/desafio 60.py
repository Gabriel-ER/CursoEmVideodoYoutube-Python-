#fatorial

n=int(input("número:"))
m=0
parcial = 1
while n > 0:
    parcial = parcial*n
    n -= 1

print(parcial)
