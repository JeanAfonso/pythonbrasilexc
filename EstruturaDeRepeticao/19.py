# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

soma = 0
n = []
numeros = int(input('Digite um numero: '))
n.append(numeros)

while True:
    numeros = int(input('Digite um numero: '))

    if 0 < numeros <= 1000:
        n.append(numeros)
        soma += numeros

    else:
        print('Numero invalido!')
        break

n.sort()

print(n[0])
print(n[len(n)-1])
print(sum(n))