# Um numero inteiro pode ser par ou ímpar. Escreva um algoritmo que recebe um número inteiro e imprime na tela a informação sobre sua paridade

num = int(input("Digite um número: "))
resto = num%2

if resto == 0:
    print("O número", num, "é par")
else:
    print("O número", num, "é ímpar")

print("FIM")