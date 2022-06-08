num_1 = int(input('Primeiro numero: '))
num_2 = int(input('Primeiro numero: '))

soma = 0

if num_1 < num_2:
    for x in range(num_1, num_2 + 1):
        soma += x
    print(soma)

else:
    for j in range(num_2, num_1 + 1):
        soma += j

    print(soma)
