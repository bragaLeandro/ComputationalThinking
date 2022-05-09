pessoas = 20
cont = 0
menor_nota = 71
maior_nota = 0
ate_20 = 0
entre_21a50 = 0
acima_50 = 0

while cont < pessoas:
    cont = cont+1
    nota = int(input("Informe a nota do {}° candidato: ".format(cont)))
    if nota < menor_nota:
        menor_nota = nota
    elif nota > maior_nota:
        maior_nota = nota

    if nota <= 20:
        ate_20 = ate_20 + 1
    elif nota >= 21 and nota <=50:
        entre_21a50 = entre_21a50 + 1
    else:
        acima_50 = acima_50 + 1


ate_20 = (ate_20/pessoas)*100
entre_21a50 = (entre_21a50/pessoas)*100
acima_50 = (acima_50/pessoas)*100

print("{}% das pessoas tiraram nota até 20".format(int(ate_20)))
print("{}% das pessoas tiraram nota entre 21 a 50".format(int(entre_21a50)))
print("{}% das pessoas tiraram nota até 20".format(int(acima_50)))
print("A maior nota foi {} e a menor nota foi {}".format(maior_nota, menor_nota))
