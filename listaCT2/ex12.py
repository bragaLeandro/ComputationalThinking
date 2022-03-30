#Desenvolva um algoritmo que informe se uma data é válida ou não. O algoritmo deverá ler 2 números inteiros, que representem o dia e o mês e informar se é um dia do mês válido. Desconsidere os casos de ano bissexto, ou seja, fevereiro têm 28 dias.

dia  = int(input("Informe um dia do mês: "))
mes = int(input("Informe um mês (1 a 12): "))

if mes == 2 and dia <=28 and dia >=1:
    print("Data válida")

elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and dia <=31 and dia >=1:
    print("Data válida")

elif mes == 4 or mes == 6 or mes == 9 or mes == 1 and dia <=30 and dia >=1:
    print("Data válida")

else:
    print("Data inválida")