# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade
# da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem,
# adulta ou idosa, conforme a média calculada.

# 0 a 25 - jovem
# 26 a 60 - adulta
# 60 > idoso

from time import sleep

grupo = []

while True:
    idade = int(input('Digite a idade: '))
    if idade >= 0:
        grupo.append(idade)
    else:
        print("calculando a media...")
        sleep(1)
        break

print(grupo)
media = sum(grupo) / len(grupo)

if 0 <= media <= 25:
    print(f'A média de idade do grupo é de {int(media)} anos, então são Jovens!')

if 26 <= media <= 60:
    print(f'A média de idade do grupo é de {int(media)} anos, então são Adultos!')

else:
    print(f'A média de idade do grupo é de {int(media)} anos, então são idosos!')
