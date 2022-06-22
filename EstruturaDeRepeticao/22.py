# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo,
# por quais número ele é divisível.

    num = int(input('Digite um numero: '))
    tot = 0
    divisiveis = []

    for c in range(1, num + 1):
        if num % c == 0:
            print('\33[33m', end='')
            tot += 1
            divisiveis.append(c)
        else:
            print('\33[31m', end='')
        print(f'{c}', end='')
    print(f'\n\33[mO numero {num} foi divisivel {tot} vezes')

    if tot == 2:
        print(f'E por isso ele é PRIMO {divisiveis}')
    else:
        print(f'E por isso ele NÃO É PRIMO, ele é divisivel por {divisiveis}')