pessoas = []
totalPessoas = 0
idadeTotal = 0

while True:
    dic = {}
    dic['nome'] = str(input("Nome: "))
    dic['sexo'] = str(input("Sexo: [M/F] ")).upper()
    dic['idade'] = int(input("Idade: "))
    pessoas.append(dic.copy())
    totalPessoas += 1
    idadeTotal += dic['idade']
    cont = str(input("Quer continuar? [S/N] ")).upper()
    if cont == 'N':
        break
media = idadeTotal / totalPessoas
print("-=" * 30)
print(f"- O grupo tem {totalPessoas} pessoas.")
print(f"- A média de idade é de {media} anos.")
print(f"- Lista das mulheres:")
for i in range(len(pessoas)):
    if pessoas[i]['sexo'] == 'F':
        print(f"nome = {pessoas[i]['nome']};", end=' ')
        print(f"sexo = {pessoas[i]['sexo']};", end=' ')
        print(f"idade = {pessoas[i]['idade']};")
        print("")
print(f"- Lista das pessoas que estão acima da média:")
for i in range(len(pessoas)):
    if pessoas[i]['idade'] > media:
        print(f"nome = {pessoas[i]['nome']};", end=' ')
        print(f"sexo = {pessoas[i]['sexo']};", end=' ')
        print(f"idade = {pessoas[i]['idade']};")
        print("")
print("<<ENCERRADO>>")