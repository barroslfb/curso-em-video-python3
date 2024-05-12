numero = int(input("Digite um número inteiro: "))
seq = 0
ajuda = 0

print(f"Os {numero} primeiros termos de uma sequência de Fibonacci são:")
while numero != 0:
    print(seq, end=' -> ')
    if seq == 0:
        seq += 1
    else:
        seq = seq + ajuda
        ajuda = seq - ajuda
    numero -= 1

    