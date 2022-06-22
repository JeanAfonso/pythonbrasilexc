# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

num = int(input('Digite um numero: '))

for i in range(1, num + 1):
    tot = 0
    divisiveis = []
    for c in range(1, i + 1):
        if i % c == 0:
            print('\33[33m', end='')
            tot += 1
            divisiveis.append(c)
        else:
            print('\33[31m', end='')
        print(f'{c}', end='')
    print(f'\n\33[mO numero {i} foi divisivel {tot} vezes')

    if tot == 2:
        print(f'E por isso ele é PRIMO {divisiveis}')
    else:
        print(f'E por isso ele NÃO É PRIMO, ele é divisivel por {divisiveis}')