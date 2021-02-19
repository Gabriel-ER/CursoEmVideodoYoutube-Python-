termo1 = float(input('Priemiro Termo:'))
razao= float(input('Razão'))
elemento=0
for i in range(0,10):
    elemento=termo1+i*razao
    print('{}:'.format(i+1),elemento)

