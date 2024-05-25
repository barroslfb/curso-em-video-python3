from utilidadescev import dado

def existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
        return True
    except FileNotFoundError:
        return False
    

def criar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
        print(f"Arquivo {nome} criado com sucesso!")
    except:
        print("Houve um ERRO na criação do arquivo!")


def ler(nome):
    try:
        a = open(nome, 'rt')
        dado.cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dad = linha.split(';')
            dad[1] = dad[1].replace('\n', '')
            print(f"{dad[0]:<30}{dad[1]:>3} anos")
        a.close()
    except:
        print("Erro ao ler o arquivo!")


def cadastrar(arq='cursoemvideo.txt', nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
        a.write(f'{nome};{idade}\n')
        print(f"Novo registro de {nome} adicionado.")
        a.close()
    except:
        print("Houve um ERRO!")
    