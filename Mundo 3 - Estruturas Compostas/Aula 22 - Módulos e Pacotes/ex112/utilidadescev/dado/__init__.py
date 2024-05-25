def leiaDinheiro(texto):
    while True:
        inp = input(texto).replace(',', '.').strip()
        try: 
            inp = float(inp)
            return inp
        except ValueError:
            print(f'ERRO: "{inp}" é um preço inválido!')