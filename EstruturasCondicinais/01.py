# Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))

if n1 > n2:
    print(f'O numero {n1} é o maior numero!')
elif n2 > n1:
    print(f'O numero {n2} é o maior numero!')
else:
    print(f'Os numeros são iguais.')