matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        matriz[i][j] = (int(input(f"Digite o valor para [{i}, {j}]: ")))
print("-=" * 30)
for h in range(3):
    print(f"{matriz[h]}")