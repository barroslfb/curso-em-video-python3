numero = int(input('Digite um número: '))
varia = numero
fatorial = 1

while varia != 0:
    fatorial = varia * fatorial
    varia -= 1
print(f'O fatorial de {numero} é {fatorial}.')