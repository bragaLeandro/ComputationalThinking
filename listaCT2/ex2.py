#Escrever um algoritmo que leia dois vlores inteiro distintos e informe qual é o maior ou se houve empate

num_a = int(input("Informe um número: "))
num_b = int(input("Informe outro número"))

if num_a > num_b:
    print("O número", num_a, "é maior que o número", num_b)
elif num_a < num_b:
    print("O número", num_b, "é maior que o número", num_a)
elif num_a == num_b:
    print("Os números informados são iguais.")

