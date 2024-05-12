while True:
    numero = int(input("Digite um número: "))
    if numero < 0:
        print("Programa encerrado!")
        break
    for i in range(1, 11):
        print(f"{i} x {numero} = {i * numero}")
