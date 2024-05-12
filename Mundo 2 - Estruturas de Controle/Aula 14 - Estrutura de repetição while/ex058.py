from random import randint
numero = randint(0, 10)
inp = 11
counter = 0

while inp != numero:
    inp = int(input('Adivinhe o número que pensei: '))
    counter += 1
    if inp != numero:
        print('Você errou! Tente novamente.')
    else:
        print(f'Parabéns! Você acertou em {counter} tentativas.')
