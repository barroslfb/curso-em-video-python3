maiorPeso = 0
menorPeso = 0

for i in range(5):
    peso = float(input("Digite seu peso: "))
    if i == 0:
        maiorPeso = peso
        menorPeso = peso
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso
print(f"O maior peso foi de {maiorPeso} kg e o menor peso foi de {menorPeso} kg.")