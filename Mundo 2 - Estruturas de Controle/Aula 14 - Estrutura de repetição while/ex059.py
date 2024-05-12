num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
menu = 0

while menu != 5:
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    menu = int(input('Digite o comando: '))
    
    if menu == 1:
        print(f'A soma de {num1} com {num2} é {num1 + num2}')
    elif menu == 2:
        print(f'O produto de {num1} com {num2} é {num1 * num2}')
    elif menu == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        elif num2 > num1:
            print(f'{num2} é maior que {num1}')
        else:
            print(f'{num1} e {num2} são iguais!')
    elif menu == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif menu == 5:
        continue
    else:
        print('Digite um comando válido.')
print('Você saiu do menu.')