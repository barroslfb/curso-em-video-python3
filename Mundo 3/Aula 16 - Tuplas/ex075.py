tupla = (int(input("Digite um número: ")), 
         int(input("Digite um número: ")), 
         int(input("Digite um número: ")), 
         int(input("Digite um número: ")))

# a) Quantas vezes apareceu o 9
print(f"O 9 apareceu {tupla.count(9)} vezes")

# b) Em que posição foi digitado o primeiro valor 3
if 3 in tupla:
    print(f"O 3 apareceu a primeira vez na {tupla.index(3) + 1}ª posição.")
else:
    print("O valor 3 não foi digitado.")

# c) Quais foram os números pares
print(f"Os valores pares são: ", end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')