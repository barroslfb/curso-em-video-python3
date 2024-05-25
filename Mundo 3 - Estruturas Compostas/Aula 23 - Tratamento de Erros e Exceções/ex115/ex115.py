from utilidadescev import dado, opcoes, arquivo

while True:
    arq = 'cursoemvideo.txt'

    if not arquivo.existe(arq):
        arquivo.criar(arq)

    dado.cabecalho("MENU PRINCIPAL")
    print("1 - Ver pessoas cadastradas\n"
          "2 - Cadastrar nova Pessoa\n"
          "3 - Sair do Sistema")
    print(dado.linha())
    opc = dado.leiaInt("Sua Opção: ", 1, 3)

    if opc == 1:
        opcoes.op1(arq)
    elif opc == 2:
        opcoes.op2()
    elif opc == 3:
        opcoes.op3()
        break