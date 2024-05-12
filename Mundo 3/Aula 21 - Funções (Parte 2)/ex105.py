def notas(*n, sit=False):
    """
    -> Função para ler notas e analisar a situação da turma.
    :param n: notas dos alunos.
    :param sit: valor opcional, indica a situação da turma.
    :return: dicionário com as informações da turma.
    """
    turma = {}
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['média'] = sum(n)/len(n)
    if sit:
        if turma['média'] >= 7:
            turma['situação'] = 'BOA'
        elif turma['média'] < 5:
            turma['situação'] = 'RUIM'
        else:
            turma['média'] = 'RAZOÁVEL'
    return turma



#Programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)