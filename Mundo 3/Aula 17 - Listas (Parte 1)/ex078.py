lista = []

for i in range(5):
    lista.append(int(input(f"Digite o valor para a Posição {i}: ")))

print(f"Você digitou os valores {lista}")
print(f"O maior valor digitado foi {max(lista)} nas posições ", end='')
for i in range(len(lista)):
    if lista[i] == max(lista):
        print(f"{i}...", end=' ')
print("")
        
print(f"O menor valor digitado foi {min(lista)} nas posições ", end='')
for i in range(len(lista)):
    if lista[i] == min(lista):
        print(f"{i}...", end=' ')
print("")
