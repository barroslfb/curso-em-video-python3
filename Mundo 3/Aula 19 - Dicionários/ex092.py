import datetime

dic = {}

dic['nome'] = str(input("Nome: "))
dic['idade'] = datetime.date.today().year - int(input("Ano de Nascimento: "))
dic['ctps'] = int(input("Carteira de Trabalho (0 não tem): "))
if dic['ctps'] != 0:
    dic['contratação'] = int(input("Ano de contratação: "))
    dic['salário'] = float(input("Salário: R$"))
    dic['aposentadoria'] = dic['idade'] + dic['contratação'] + 35 - datetime.date.today().year
print("-=" * 30)
for k, v in dic.items():
    print(f"{k} tem o valor {v}")