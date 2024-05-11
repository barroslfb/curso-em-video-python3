def area(a, b):
    print(f"A área de um terreno {a:.1f}x{b:.1f} é de {a*b:.1f}m².")


print(" Controle de Terrenos")
print("-" * 20)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
area(l, c)