jogadores = []
while True:
    dic = {}
    dic['nome'] = str(input("Nome do Jogador: "))
    partidas = int(input(f"Quantas partidas {dic['nome']} jogou? "))
    dic['gols'] = []
    dic['total'] = 0
    for i in range(partidas):
        dic['gols'].append(int(input(f"Quantos gols na partida {i+1}? ")))
        dic['total'] += dic['gols'][i]
    print("-=" * 30)
    jogadores.append(dic.copy())
    dic.clear()
    cont = str(input("Quer continuar? [S/N] ")).upper()[0]
    if cont == 'N':
        break
print("-=" * 30)
print(f"cod nome          gols        total")
print("-" * 15)
for e,v in enumerate(jogadores):
    print(e, v)

while True:
    mos = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if mos == 999:
        break
    for e,v in enumerate(jogadores):
        if mos == e:
            print(f"-- LEVANTAMENTO DO JOGADOR {v['nome']}:")
            for i in range(len(v['gols'])):
                print(f"No jogo {i+1} fez {v['gols'][i]} gols.")