idadeTotal = 0
homemVelhoIdade = 0
homemVelhoNome = ''
mulheresNovas = 0

for i in range(4):
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite qual o seu sexo: ")

    idadeTotal += idade

    if sexo == 'homem' and idade > homemVelhoIdade:
        homemVelhoIdade = idade
        homemVelhoNome = nome
    
    if sexo == 'mulher' and idade < 21:
        mulheresNovas += 1

print(f"A média de idade {idadeTotal / 4} anos.")
print(f"O homem mais velho é {homemVelhoNome}.")
print(f"{mulheresNovas} mulheres tem menos que 21 anos.")

