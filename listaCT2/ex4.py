# A jornada de trabalho diárioa de um entregador é de 8 horas. Caso o trabalhador tenha trabalhado além da jornada mensal exigida, ele terá direito a receber hora-extra. O vaor da hora-extra é o valor que ele recebe por hora acrescido de 50%. Supondo que ele trabalha apenas nos dias úteis, escreva um algoritmo que recebe:
#a) o total de dias úteis de um mês
#b) o total de horas trabalhadas pelo trabalhador
#c) quanto o trabalhador recebe por hora
#Calcula e mostra o valor recebido a título de hora-extra (se houver) e o salário final do trabalhador

dias_uteis = int(input("Quantos dias úteis tiveram no mês? "))
horas_trabalhadas = float(input("Quantas horas foram trabalhadas? "))
salario_hora = float(input("Quanto você recebe por hora? "))

horas_extra = horas_trabalhadas-(dias_uteis*8)
valor_extra = (salario_hora*1.5)*horas_extra
salario = (salario_hora*horas_trabalhadas)+valor_extra

if horas_trabalhadas > dias_uteis*8:
    print("Você recebeu", valor_extra, "reais de hora extra, e seu salário final foi:", salario)
else:
    print("Você não recebeu hora extra, e seu salário final foi:", salario, "reais.")
    
    