lista = []

for i in range(5):
    num = int(input("Digite um valor: "))

    if i == 0:
        lista.append(num)
        print("Adicionado ao final da lista...")
    else:
        t = 0
        for h in range(len(lista)):
            if num < lista[h]:
                lista.insert(h, num)
                t = 1
                break
        if t == 0:
            lista.append(num)

        if lista.index(num) + 1 == len(lista):
            print("Adicionado ao final da lista...")
        else:
            print(f"Adicionado na posição {lista.index(num)} da lista...")

print(f"Os valores digitados em ordem foram {lista}")
    