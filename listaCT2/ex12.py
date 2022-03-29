#Desenvolva um algoritmo que informe se uma data é válida ou não. O algoritmo deverá ler 2 números inteiros, que representem o dia e o mês e informar se é um dia do mês válido. Desconsidere os casos de ano bissexto, ou seja, fevereiro têm 28 dias.

meses_do_ano = [1 ,2 ,3 ,4 ,5, 6, 7, 8, 9, 10, 11, 12]
mes_ate_31 = [1, 3, 5, 6, 8, 10, 12]
mes_ate_30 = [4, 5, 9, 11]
mes_ate_28 = 2

dia  = int(input("Informe um dia do mês: "))
mes = int(input("Informe um mês (1 a 12): "))

