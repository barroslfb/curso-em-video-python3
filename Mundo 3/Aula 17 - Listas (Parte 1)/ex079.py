lista = []

while True:
    num = int(input("Digite um valor: "))
    if num in lista:
        print("Valor duplicado! Não vou adicionar...")
    else:
        lista.append(num)

    cont = input("Deseja continuar? [S/N] ").upper()
    if cont == 'N':
        break

lista.sort()
print(f"Você digitou os valores {lista}")
