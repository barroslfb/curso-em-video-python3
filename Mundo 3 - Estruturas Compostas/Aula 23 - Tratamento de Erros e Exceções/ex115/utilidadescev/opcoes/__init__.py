from utilidadescev import dado, arquivo

def op1(nome):
    arquivo.ler(nome)

def op2():
    dado.cabecalho("NOVO CADASTRO")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    arquivo.cadastrar(nome=nome, idade=idade)
def op3():
    dado.cabecalho("Saindo do sistema... Até logo!")