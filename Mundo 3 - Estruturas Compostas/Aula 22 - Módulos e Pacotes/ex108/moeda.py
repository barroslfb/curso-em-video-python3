def aumentar(num, porc):
    aum = num * (1 + porc/100)
    return aum

def diminuir(num, porc):
    dim = num * (1 - porc/100)
    return dim

def dobro(num):
    dobro = num * 2
    return dobro

def metade(num):
    metade = num / 2
    return metade

def moeda(num=0):
    form = f"R${num:.2f}".replace('.', ',')
    return form