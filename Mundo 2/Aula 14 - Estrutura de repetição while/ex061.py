termo = int(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão da PA: '))

first = termo

while termo != first + 10 * razao:
    print(termo)
    termo += razao