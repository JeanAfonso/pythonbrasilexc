# Faça um programa que, dado um conjunto de N números,
# determine o menor valor, o maior valor e a soma dos valores.

n = [10, 2, 7, 9, 15]
soma = 0

for i in n:
    soma += i

n.sort()

print(n[0])
print(n[len(n)-1])
print(sum(n))