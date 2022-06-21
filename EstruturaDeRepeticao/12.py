numero = int(input('digite um numero: '))

if 0 < numero <= 10:
    for i in range(1, 11):
       print(f"{numero} x {i} = {numero * i}")

else:
    print('Numero invalido!')
