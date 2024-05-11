from random import randint
from time import sleep
from operator import itemgetter

dicio = {}
print("Valores sorteados:")
sleep(1)
for i in range(4):
    dicio[f'jogador{i+1}'] = randint(1, 6)
    print(f"    O jogador{i+1} tirou {dicio[f'jogador{i+1}']}")
    sleep(1)
ranking = []
ranking = sorted(dicio.items(), key=itemgetter(1), reverse=True)
print("-=" * 30)
print("  == RANKING DOS JOGADORES ==")
for i,v in enumerate(ranking):
    sleep(1)
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}.')