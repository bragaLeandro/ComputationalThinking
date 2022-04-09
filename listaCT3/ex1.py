#Escreva um programa que dado um numero inteiro n positivo calcula e imprime a soma de todos os números inteiros entre 1 e n. Exemplo, se n=10 então: 1+2+3+4+5+6+7+8+9+10 = 55

n = int(input("Informe o número inteiro positivo n: "))
i = 1
soma = 0
while n < 0:
    n = int(input("Resposta inválida, informe o número inteiro positivo n: "))

while i <= n:
    print(i)
    i = i+1 