def fatorial(num):
    fat = 1
    for i in range(num, 0, -1):
        fat *= i
    return fat

num = int(input("Digite um valor: "))
fat = fatorial(num)
print(f"")