#Nesse mês, João recebeu um aumento no salário, porém ele não sabe calcular o percentual de aumento. Você deverá escrever um algorítmo que recebe 2 números reais representando os salários antes e depois do aumento e deverá calcular e exibir o percentual de aumento que João obteve.

salario_antigo = float(input("Qual era o seu antigo salário?"))
salario_novo = float(input("Qual é o seu novo salário?"))

percentual= ((salario_novo-salario_antigo)/salario_antigo)*100

print("O seu salário teve uma variação de", percentual,"%")