PAIS_A = int(input('População do Pais A: '))
PAIS_B = int(input('População do Pais b: '))
TAXA_A = float(input('Taxa de crescimento pais A: '))
TAXA_B = float(input('Taxa de crescimento pais B: '))

ano = 0

while PAIS_A < PAIS_B:
    PAIS_A += (PAIS_A * TAXA_A) / 100
    PAIS_B += (PAIS_B * TAXA_B) / 100
    ano += 1

print(f'A populacao do pais A {PAIS_A:.0f} vai demorar {ano} '
      f'anos para ultrapassar ou igualar a populacao do pais B {PAIS_B:.0f}')