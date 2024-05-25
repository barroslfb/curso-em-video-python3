def linha(tam = 42):
    return "-" * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(txt, n1, n2):
    while True:
        inp = input(txt)
        try: 
            inp = int(inp)
            if n1 <= inp <= n2:
                return inp
            else:
                print("Valor inválido, digite uma das opções acima.")
        except ValueError:
            print(f'ERRO: "{inp}" é um valor inválido!')