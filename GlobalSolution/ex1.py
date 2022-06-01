n = int(input("Informe a quantidade de meses: "))
i = 0
acum = 0

while i < n:
    i = i + 1
    fatur = float(input("Informe o faturamento do {}° mês: ".format(i)))
    acum = acum + fatur

def calcula_media(acum, n):
    return acum / n

media = calcula_media(acum, n)

print("A média do faturamento é da empresa é de {} reais".format(media))