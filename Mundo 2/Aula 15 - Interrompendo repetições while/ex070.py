total = 0
nomeBarato = ''
precoBarato = 0
milhar = 0

while True:
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    
    if total == 0:
        precoBarato = preco
        nomeBarato = nome
    total += preco
    if preco > 1000:
        milhar += 1
    if preco < precoBarato:
        precoBarato = preco
        nomeBarato = nome    

    cont = input("Deseja continuar? [S/N] ").upper()
    if cont == 'N':
        break
print(f"O total gasto na compra foi de R${total:.2f}, {milhar} produtos custam mais de R$1000.00 e o nome do produto mais barato é {nomeBarato}.")