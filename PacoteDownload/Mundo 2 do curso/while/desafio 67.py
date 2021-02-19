while True:
    a = 0
    x = int(input("Número:"))
    if x < 0:
        print("Tabuada encerrada.")
        break
    while a < 11:
        print(f'{x} * {a} = {x*a}')
        a += 1