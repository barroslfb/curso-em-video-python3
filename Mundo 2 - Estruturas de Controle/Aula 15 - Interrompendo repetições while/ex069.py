maioridade = 0
homens = 0
mulherJovem = 0

while True:
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo [M/F]: ").upper()

    if idade > 18:
        maioridade += 1
    elif sexo == 'M':
        homens += 1
    elif idade < 20 and sexo == 'F':
        mulherJovem += 1
    
    conti = input("Deseja continuar [S/N]? ").upper()
    if conti == 'N':
        break
print(f"{maioridade} pessoas tem mais de 18 anos, {homens} homens foram cadastrados e temos {mulherJovem} mulheres com menos de 20 anos.")
