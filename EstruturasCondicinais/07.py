# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))
lista = [n1, n2, n3]

maior = max(lista)
menor = min(lista)

print(f'O maior numero é {maior}')
print(f'O menor numero é {menor}')