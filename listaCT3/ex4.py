#Dado um numero inteiro positivo n e uma sequencia n de números reais, escreva um algoritmo que conta e imprime a quantidade de numeros positivos e a quantidade de numeros negativos

n_seq = float(input("Informe a quantidade de números da sequência: "))
cont = 0
num_pos = 0
num_neg = 0

while cont < n_seq:
    cont = cont + 1
    n_real = float(input("Informe o {}° número real da sequência: ".format(cont)))
    if n_real > 0:
        num_pos = num_pos + 1
    elif n_real < 0:
        num_neg = num_neg + 1

print("Existem {} números negativos e {} números positivos na sequência informada.".format(num_neg, num_pos))