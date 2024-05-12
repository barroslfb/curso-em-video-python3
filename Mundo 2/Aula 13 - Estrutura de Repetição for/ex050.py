soma = 0
for i in range(6):
    number = int(input("Digite um número inteiro: "))
    if (number % 2 == 0):
        soma += number
print(soma)