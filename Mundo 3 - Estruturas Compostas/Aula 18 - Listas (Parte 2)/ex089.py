alunos = []

while True:
    pessoa = ["", [0, 0]]
    pessoa[0] = str(input("Nome: "))
    pessoa[1][0] = float(input("Nota 1: "))
    pessoa[1][1] = float(input("Nota 2: "))

    alunos.append(pessoa[:])
    pessoa.clear()

    cont = str(input("Quer continuar? [S/N] ")).upper()
    if cont == 'N':
        break

print("-=" * 30)
print(f"{"No.":<4}{"NOME":<10}{"MÉDIA":>8}")
print("-" * 30)

for i in range(len(alunos)):
    media = (alunos[i][1][0] + alunos[i][1][1]) / 2
    print(f"{i:<4}{alunos[i][0]:<10}{media:>8.2f}")

print("-" * 30)    

while True:
    nota = str(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if nota == '999':
        break
    for i in range(len(alunos)):
        if nota == alunos[i][0]:
            print(f"Notas de {alunos[i][0]} são {alunos[i][1]}")