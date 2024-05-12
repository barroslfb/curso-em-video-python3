frase = str(input("Digite uma frase: ")).upper()
fraseLista = []

for i in range(len(frase)):
    if frase[i] == ' ':
        continue
    fraseLista += frase[i]

termo = 0
for i in range(len(fraseLista)):
    if fraseLista[i] != fraseLista[len(fraseLista) - 1 - i]:
        print("A frase não é um palíndromo.")
        termo = 1
        break
if termo == 0:
    print("A frase é um palíndromo.")
        

