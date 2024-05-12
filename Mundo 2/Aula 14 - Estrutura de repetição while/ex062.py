termo = int(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão da PA: '))

first = termo
quant = 1
hist = 0

while quant != 0:
    quant = int(input('Quantos termos da PA você quer ver? '))
    hist += quant

    if quant == 0: 
        continue

    while termo != first + hist * razao:
        print(termo)
        termo += razao
