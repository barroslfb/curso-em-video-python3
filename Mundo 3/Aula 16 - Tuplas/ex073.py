tupla = ('Santos', 'Sport Recife', 'Chapecoense', 'Operário', 'Goiás',
         'América-MG', 'Coritiba', 'Brusque', 'Vila Nova', 'Novorizontino',
         'Botafogo-SP', 'Ceará', 'Amazonas', 'CRB', 'Paysandu', 'Ponte Preta',
         'Mirassol', 'Avaí', 'Guarani', 'Ituano')

# a) Cinco primeiros colocados
print(f"Os cinco primeiros colocados são: {tupla[:5]}")

# b) Zona de rebaixamento
print(f"Os times na zona de rebaixamento são: {tupla[-4:]}")

# c) Ordem alfabética
print(f"Times em ordem alfabética: {sorted(tupla)}")

# d) Posição da Chapecoense
print(f"A Chapecoense está em {tupla.index("Chapecoense") + 1}° lugar.")