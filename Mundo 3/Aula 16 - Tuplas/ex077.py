palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for i in palavras:
    print(f"Na palavra {i.upper()} temos ", end='')
    for j in i.upper():
        if j in 'AEIOU':
            print(j, end=' ')
    print("")