def moeda(num=0):
    form = f"R${num:.2f}".replace('.', ',')
    return form

def aumentar(num=0, porc=0, bool=False):
    aum = num * (1 + porc/100)
    return aum if bool is False else moeda(aum)

def diminuir(num=0, porc=0, bool=False):
    dim = num * (1 - porc/100)
    return dim if bool is False else moeda(dim)

def dobro(num=0, bool=False):
    dobro = num * 2
    return dobro if bool is False else moeda(dobro)

def metade(num=0, bool=False):
    metade = num / 2
    return metade if bool is False else moeda(metade)

def resumo(p=0, aum=0, red=0):
    print("-"*35)
    print('RESUMO DO VALOR'.center(35))
    print('-'*35)
    print(f"Preço analisado: \t{moeda(p)}")
    print(f"Dobro do preço: \t{dobro(p, True)}")
    print(f"Metade do preço: \t{metade(p, True)}")
    print(f"{aum}% de aumento: \t{aumentar(p, aum, True)}")
    print(f"{red}% de aumento: \t{diminuir(p, red, True)}")
    print("-"*35)