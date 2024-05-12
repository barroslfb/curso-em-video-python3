numero = 0
soma = 0
cont = 0

while numero != 999:
    numero = int(input("Digite um número inteiro: "))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f"{cont} números foram digitados e a soma entre eles é {soma}")
