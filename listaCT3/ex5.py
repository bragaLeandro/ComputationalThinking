#Escreva um algoritmo que, dados um número inteiro positivo n imprime na tela a contagem de todos os divisores positivos de n

n = int(input("Informe um número inteiro positivo: "))
cont = 1
list = []
while cont in range(n):
    if n % cont == 0:
        list.append(cont)
    cont=cont+1

print(list)