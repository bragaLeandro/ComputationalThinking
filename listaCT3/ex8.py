#Verificação de número primo

n = int(input("Informe o número que você deseja saber se é primo: "))
aux = 2
primo = True

while aux < n and aux >= 2:
    if n%aux == 0:
        primo = False
    aux = aux +1

if (primo):
    print("O numero {} é primo!".format(n))
else:
    print("O número {} não é primo!".format(n))