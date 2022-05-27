nota = int(input('Digite um valor entre 0 a 10: '))

while True:
    if 0 <= nota <= 10:
        break
    else:
        print('Digite um valor valido')
        nota = int(input('Digite um valor entre 0 a 10: '))
