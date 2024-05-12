exp = input("Digite a expressão: ")
count1 = 0
count2 = 0

for i in exp:
    if i == '(':
        count1 += 1
    elif i == ')':
        count2 += 1

if count1 == count2:
    print("Sua expressão está certa!")
else:
    print("Sua expressão está errada!")


