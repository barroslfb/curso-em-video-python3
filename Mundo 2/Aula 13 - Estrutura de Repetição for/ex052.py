numero = int(input("Digite um número inteiro: "))

termo = 0
for i in range(2, numero):
    if (numero % i == 0):
        print(f"O número {numero} não é primo")
        termo = 1
        break
if termo == 0:
    print(f"O numéro {numero} é primo")