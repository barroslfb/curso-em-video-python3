def ficha(nome='<desconhecido>', gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


jog = str(input("Nome do Jogador: "))
if len(jog) == 0:
    jog = '<desconhecido>'
gol = str(input("Número de Gols: "))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
ficha(jog, gol)