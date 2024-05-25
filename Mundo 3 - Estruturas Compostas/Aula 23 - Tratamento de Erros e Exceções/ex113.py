def leiaInt(frase):
    while(1):
        try:
            numero = int(input(frase))
        except (ValueError, TypeError):
            print("ERRO: por favor, digite um número inteiro válido.")
        except (KeyboardInterrupt):
            print("\nEntrada de dados interrompida pelo usuário.")
            return 0
        else:
            return numero

def leiaFloat(frase):
    while(1):
        try:
            numero = float(input(frase))
        except (ValueError, TypeError):
            print("ERRO: por favor, digite um número real válido.")
        except (KeyboardInterrupt):
            print("\nEntrada de dados interrompida pelo usuário.")
            return 0
        else:
            return numero

#Programa principal
n = leiaInt("Digite um número inteiro: ")
r = leiaFloat("Digite um número real: ")
print(f"O valor inteiro digitado foi {n} e o real foi {r}")