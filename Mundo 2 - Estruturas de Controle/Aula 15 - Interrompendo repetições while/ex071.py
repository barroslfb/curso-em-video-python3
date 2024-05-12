valor = int(input("Digite o valor a ser sacado: "))
const = valor
ced50 = 0
ced20 = 0
ced10 = 0
ced1 = 0

while True:
    if valor >= 50:
        ced50 = valor // 50
        valor = valor % 50
    elif valor >= 20:
        ced20 = valor // 20
        valor = valor % 20
    elif valor >= 10:
        ced10 = valor // 10
        valor = valor % 10
    elif valor >= 1:
        ced1 = valor
    break
print(f"Você vai receber R${const:.2f} em:")
print(f"{ced50} cédulas de 50 reais;")
print(f"{ced20} cédulas de 20 reais;")
print(f"{ced10} cédulas de 10 reais;")
print(f"{ced1} cédulas de 1 reais;")