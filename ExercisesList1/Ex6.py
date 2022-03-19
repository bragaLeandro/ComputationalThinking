## desenvolva um algoritmo que recebe um número inteiro de 0 a 99 e imprime o dígito das dezenas e o digito das unidades desse número

x = int(input("Escreva um número inteiro de 0 a 99: "))

if x<=99:

    print("A dezena de" , x ,  "é:" , x // 10 , "e a unidade é:" , x%10)

else:
    print("Número inválido")

    