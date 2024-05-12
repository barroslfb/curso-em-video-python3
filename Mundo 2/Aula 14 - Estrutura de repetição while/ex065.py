soma = 0
counter = 0
maior = 0
menor = 0
digite = ''

while digite != 'N':
    digite = str(input('Deseja digitar um número [S/N]? ')).upper()
    if digite == 'S':
        numero = int(input('Digite um número inteiro: '))

        if maior == 0:
            maior = numero
        if menor == 0:
            menor = numero
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

        soma += numero
        counter += 1

print(f"A média entre todos os valores digitados é {soma / counter}, o maior número foi {maior} e o menor foi {menor}.")
