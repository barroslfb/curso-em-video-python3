def leiaint(frase):
    while(1):
        numero = str(input(frase))
        if numero.isnumeric() == False:
            print("ERRO! Digite um número inteiro válido.")
        else:
            return int(numero)


#Programa principal
n = leiaint("Digite um número: ")
print(f"Você acabou de digitar o número {n}")