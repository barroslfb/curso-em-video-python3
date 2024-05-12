matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior = somaPar = terceira = 0

for i in range(3):
    for j in range(3):
        matriz[i][j] = (int(input(f"Digite o valor para [{i}, {j}]: ")))
        if matriz[i][j] % 2 == 0:
            somaPar += matriz[i][j]

        if j == 2:
            terceira += matriz[i][j]
            
        if i == 1:
            if j == 0 or matriz[i][j] > maior:
                maior = matriz[i][j]

print("-=" * 30)

for h in range(3):
    print(f"{matriz[h]}")
print("-=" * 30)
print(f"A soma dos valores pares é {somaPar}.")
print(f"A soma dos valores da terceira coluna é {terceira}.")
print(f"O maior valor da segunda linha é {maior}.")