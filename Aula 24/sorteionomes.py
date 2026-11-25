import random

pessoas = []

num_participantes = int(input('Numero de particpantes: '))

while len(pessoas) < num_participantes:
    pessoas.append(input('Nome do participante: '))

sorteado = random.choice(pessoas)

print('Sorteado: ', sorteado)