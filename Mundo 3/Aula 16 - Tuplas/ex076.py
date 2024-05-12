tupla = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
         'Estojo', 25, 'Transferidor', 4.2, 'Compasso',
         9.99, 'Mochila', 120.32, 'Canetas', 22.3,
         'Livro', 34.9)

print("-" * 40)
print(" " * 11, "LISTAGEM DE PREÇOS", " " * 11)
print("-" * 40)

for i in range(0, len(tupla), 2):
    print(f"{tupla[i]:.<30}", end='')
    print(f"R${tupla[i + 1]:>7.2f}")

print("-" * 40)

    