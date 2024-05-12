lista = []
listaPar = []
listaImpar = []

while True:
    lista.append(int(input("Digite um valor: ")))

    cont = input("Deseja continuar? [S/N] ").upper()
    if cont == 'N':
        break

for i in lista:
    if i % 2 == 0:
        listaPar.append(i)
    else:
        listaImpar.append(i)

print(f"A lista completa é {lista}")
print(f"A lista de pares é {listaPar}")
print(f"A lista de ímpares é {listaImpar}")