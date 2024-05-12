from time import sleep

def contador(inicio, fim, passo):
    n = 1
    if inicio > fim and passo > 0:
        passo = -1 * passo
    elif passo == 0 and inicio > fim: 
        passo = -1
    elif passo == 0 and fim < inicio:
        passo = 1
    if fim <= 0:
        n = -1
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    for i in range(inicio, fim + n, passo):
        sleep(0.5)
        print(i, end=' ')
    sleep(0.5)
    print("FIM!")
    sleep(0.5)


print("-=" * 20)
contador(1, 10, 1)
print("-=" * 20)
contador(10, 0, -2)
print("-=" * 20)

print("Agora é sua vez de personalizar a contagem!")
init = int(input("Início: "))
fim = int(input("Fim:    "))
passo = int(input("Passo:  "))
contador(init, fim, passo)