numero = 0
counter = 0
soma = 0

while numero != 999:
    numero = int(input('Digite um número inteiro: '))
    if numero == 999:
        continue
    soma += numero
    counter += 1
print(f"{counter} números foram digitados e a soma total entre eles é {soma}")