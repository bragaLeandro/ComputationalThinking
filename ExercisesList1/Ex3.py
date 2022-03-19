#Escreva um algoritmo m Python que recebe dois números inteiros e exibe: a soma desses dois números, a multiplicação, a divisão inteira e o resto da divisão inteira

x = int(input("Digite um número:"))
y = int(input("Digite outro número"))

soma = x+y
print("A soma entre" , x , "e" , y , "é: " , soma)

multiplicacao = x*y
print("A multiplicação entre" , x , "e" , y , "é: " , multiplicacao)

divisao = x/y
print("A divisão entre" , x , "e" , y , "é: " , divisao)

resto = x%y
print("O resto da divisão entre" , x , "e" , y , "é: " , resto)