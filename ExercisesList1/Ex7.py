#Uma pessoa tem em seu guarda roupa x camisas, y calças e z pares de sapato. Escreva um algoritmo que calcula de quantas maneiras diferentes ele pode se vestir. Seu algoritmo deverá ler o número de camisas, o número de calças e o número de pares de sapato.

quant_camisas = int(input("Quantas camisas você possui? "))
quant_calcas = int(input("Quantas calças você possui? "))
quant_sapatos = int(input("Quantos pares de sapato você possui? "))

combinacao = (quant_camisas * quant_calcas * quant_sapatos)

print("Baseado em suas roupas, você pode se vestir de " + str(combinacao) + " maneiras diferentes")