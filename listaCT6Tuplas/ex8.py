cabecalho = ("Salário contribuição", "Alíquota/Valor")
linha1 = ("até R$ 1.903,98", "8,00%")
linha2 = ("até R$ 4.838,60", "9,00%")
linha3 = ("até R$ 6.368,60", "11,00%")
linha4 = ("até R$ 8.654,80", "12,00%")

def juntaTuplas(cabecalho, linha1, linha2, linha3, linha4):
    total = (cabecalho, linha1, linha2, linha3, linha4)
    return total

print(juntaTuplas(cabecalho, linha1, linha2, linha3, linha4))



