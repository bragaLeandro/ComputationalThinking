#Agora, vamos acrescentar uma verificação de data os casos de ano bissexto, ou seja, o ano que fevereiro tem 29 dias. Um ano bissexto se:
#a) o ano for divisível por 4
#b) anos múltiplos de 100, não são bissextos
#c) quando o ano for divisível por 400 ele é bissexto
#d) as últimas regras prevalecem sobre as primeiras

dia  = int(input("Informe um dia do mês: "))
mes = int(input("Informe um mês (1 a 12): "))
ano = int(input("Informe um ano (ex: 2002): "))

if mes == 2 and dia <=28 and dia >=1:
    print("Data válida")
    
elif ano%4 == 0 or ano%400 == 0 and mes == 2 and dia <=29 and dia >=1:
    print("Data válida")

elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and dia <=31 and dia >=1:
    print("Data válida")

elif mes == 4 or mes == 6 or mes == 9 or mes == 1 and dia <=30 and dia >=1:
    print("Data válida")

else:
    print("Data inválida")
