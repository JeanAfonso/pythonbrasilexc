# Supondo que a população de um país A seja da ordem de 80000 habitantes
# com uma taxa anual de crescimento de 3% e que a população de B
# seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população
# do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

PAIS_A = 80000
PAIS_B = 200000
TAXA_A = 3
TAXA_B = 1.5

ano = 0

while PAIS_A < PAIS_B:
    PAIS_A += (PAIS_A * TAXA_A) / 100
    PAIS_B += (PAIS_B * TAXA_B) / 100
    ano += 1
print(f'A populacao do pais A {PAIS_A:.0f} vai demorar {ano} '
      f'anos para ultrapassar ou igualar a populacao do pais B {PAIS_B:.0f}')