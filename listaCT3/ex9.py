d = float(input("Informe o montante inicial: "))
j = float(input("Informe a taxa de juros: "))
t = int(input("Informe a quantidade de meses: "))
aux = 0
j = j/100

while aux < t:
    d = (d*j) + d
    aux = aux+1

print("O montante final após o período informado é de {:.2f}".format(d))
