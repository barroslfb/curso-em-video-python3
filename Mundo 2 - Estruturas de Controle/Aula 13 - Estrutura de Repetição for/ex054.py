from datetime import date

contador = 0
for i in range(7):
    ano = int(input("Digite o ano de nascimento: "))
    if ano > date.today().year - 21:
        contador += 1

print(f"{contador} são menores de idade")