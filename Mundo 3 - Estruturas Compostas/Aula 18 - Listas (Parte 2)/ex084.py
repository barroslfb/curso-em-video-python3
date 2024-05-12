pessoas = []
pessoa = []
count = 0
pesada = []
leve = []

while True:
    pessoa.append(str(input("Nome: ")))
    pessoa.append(float(input("Peso: ")))

    count += 1
    pessoas.append(pessoa[:])
    pessoa.clear()

    cont = input("Quer continuar? [S/N] ").upper()
    if cont == 'N':
        break

print(f"Ao todo, você cadastrou {count} pessoas.")

maiorPeso = menorPeso = pessoas[0][1]
for i in range(len(pessoas)):
    if pessoas[i][1] >maiorPeso:
        maiorPeso = pessoas[i][1]
    elif pessoas[i][1] < menorPeso:
        menorPeso = pessoas[i][1]

for j in range(len(pessoas)):
    if pessoas[j][1] == maiorPeso:
        pesada.append(pessoas[j][0])
    elif pessoas[j][1] == menorPeso:
        leve.append(pessoas[j][0])

print(f"O maior peso foi de {maiorPeso:.1f}Kg. Peso de {pesada}")
print(f"O menor peso foi de {menorPeso:.1f}Kg. Peso de {leve}")