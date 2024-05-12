primeiroTermo = float(input("Digite o primeiro termo da PA: "))
razao = float(input("Digite a razão da PA: "))

for i in range(10):
    if i == 0:
        print(primeiroTermo)
        continue
    print(primeiroTermo + razao)
    primeiroTermo += razao