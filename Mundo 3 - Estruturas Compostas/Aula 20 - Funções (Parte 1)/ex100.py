from random import randint
from time import sleep

def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end='')
    for i in range(5):
        números.append(randint(1, 10))
        print(números[i], end=' ')
        sleep(0.2)
    print("PRONTO!")

def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f"Somando os valores pares de {lista}, temos {soma}")

números = []
sorteia(números)
somaPar(números)