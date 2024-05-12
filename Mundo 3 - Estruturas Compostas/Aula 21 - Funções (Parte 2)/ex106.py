def escreva(txt):
    tam = len(txt) + 4
    print("~" * tam)
    print(f"  {txt}")
    print("~" * tam)

def pyhelp(nome):
    escreva(f"Acessando o manual do comando '{nome}'")
    help(nome)

escreva("SISTEMA DE AJUDA PyHELP")
while(1):
    fun = str(input("Função ou Biblioteca > ")).lower()
    if fun == 'fim':
        escreva("ATÉ LOGO!")
        break
    else:
        pyhelp(fun)