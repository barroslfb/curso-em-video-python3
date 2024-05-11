dic = {}
dic['nome'] = str(input("Nome do Jogador: "))
partidas = int(input(f"Quantas partidas {dic['nome']} jogou? "))
dic['gols'] = []
dic['total'] = 0
for i in range(partidas):
    dic['gols'].append(int(input(f"Quantos gols na partida {i+1}? ")))
    dic['total'] += dic['gols'][i]
print("-=" * 30)
print(dic)
print("-=" * 30)
for k,v in dic.items():
    print(f"O campo {k} tem o valor {v}.")
print("-=" * 30)
print(f"O jogador {dic['nome']} jogou {partidas} partidas.")
for i,v in enumerate(dic['gols']):
    print(f"    => Na partida {i+1}, fez {v} gols.")
print(f"Foi um total de {dic['total']} gols.")