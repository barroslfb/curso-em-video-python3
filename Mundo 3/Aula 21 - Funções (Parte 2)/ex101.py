from datetime import date

def voto(idade):
    if 16 <= idade < 18 or idade >= 65:
        return "VOTO OPCIONAL"
    elif 18 <= idade < 75:
        return "VOTO OBRIGATÓRIO"
    else:
        return "VOTO NEGADO"
    

print("-" * 30)
nasc = int(input("Em que ano você nasceu? "))
anos = date.today().year - nasc
print(f"Com {anos} anos: {voto(anos)}.")