from time import sleep
from random import randint

lista = []
jogos = int(input("Quantos jogos você quer que eu sorteie? "))

for i in range(jogos):
    jogo = []
    for j in range(6):
        while True:
            num = randint(1, 60)
            if num not in jogo:
                jogo.append(num)
                break
    jogo.sort()
    lista.append(jogo[:])
    sleep(1)
    print(f"Jogo {i + 1}: {jogo}")
    jogo.clear()