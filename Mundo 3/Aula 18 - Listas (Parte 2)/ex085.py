lista = [[], []]

for i in range(7):
    temp = int(input(f"Digite o {i + 1}° valor: "))
    if temp % 2 == 0:
        lista[0].append(temp)
    else:
        lista[1].append(temp)
lista[0].sort()
lista[1].sort()
print("-=" * 30)
print(f"Os valores pares digitados foram: {lista[0]}")
print(f"Os valores ímpares digitados foram: {lista[1]}")