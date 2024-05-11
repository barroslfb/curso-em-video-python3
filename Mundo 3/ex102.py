def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: Número a ser calculado o fatorial.
    :param show: Se verdadeiro, mostra o processo da conta.
    :return: O valor do fatorial do número num.
    """
    print("-" * 30)
    fatorial = 1
    for i in range(num, 0, -1):
        fatorial *= i
        if show:
            print(f"{i} x ", end='')
    if show:
        return f"= {fatorial}"
    else:
        return f"{fatorial}"


# Programa Principal
print(fatorial(5, True))