# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes
# e limitando o fatorial a números inteiros positivos e menores que 16.

while True:
    cont = int(input('digite um numero: '))
    lista = []
    calcular = 0

    if 0 < cont <= 16:
        for i in range(0, cont):

            if not lista:
                lista.append(cont)
                print(cont)

            else:
                contador = i - 1
                calcular = lista[contador] * (cont - i)
                lista.append(calcular)
                print(lista[contador], 'x', cont - i, '=', calcular)
    else:
        print('Numero invalido')
        break
