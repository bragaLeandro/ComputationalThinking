#Escreva um algoritmo que recebe dois números e um caractere (representando uma das operações matemáticas) e calcula o valor da operação, ou seja, se a entrada for 5, * e 6 então seu programa deverá mostrar 30

num_a = float(input("Digite um número: "))
num_b = float(input("Digite outro número: "))
operacao = input("Digite operador (+/-*)")

if operacao == '+':
    print("resultado: ", num_a + num_b)
elif operacao == '-':
    print("resultado:", num_a - num_b)
elif operacao == '/':
    print("resultado:", num_a / num_b)
elif operacao == '*':
    print("resultado:", num_a * num_b)
else:
    print("Operador inválido")
        