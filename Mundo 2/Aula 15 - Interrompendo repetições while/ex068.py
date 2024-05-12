from random import randint

cont = 0
while True:
    parimpar = str(input("Par ou ímpar [P/I]? ")).upper()
    numero = int(input("Digite um número: "))
    comp = randint(0, 10)

    print(f"O número que a máquina escolheu foi {comp}")
    if (numero + comp) % 2 == 0 and parimpar == 'P':
        print("Você ganhou!")
        cont += 1
        continue
    elif (numero + comp) % 2 != 0 and parimpar == 'I':
        print("Você ganhou!")
        cont += 1
        continue
    else:
        print(f"Você perdeu! Ao total, foram {cont} vitórias suas.")
        break