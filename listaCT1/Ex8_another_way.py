#Dados o preço de um produto e um percentual de desconto, escreva um algoritmo que calcula e mostra o valor do desconto e o novo preço do produto dado o percentual. E se, ao invés de um desconto, fosse um aumento. O que muda no seu algoritmo?

preco_produto = float(input("Digite o valor do produto: "))
percentual = float(input("Digite (em %) o valor de desconto ou aumento: "))

decimal = percentual/100
valor_desconto = preco_produto*decimal
preco_desconto = preco_produto-valor_desconto

print("O valor de desconto é:", valor_desconto, "e o novo preço do produto é:", preco_desconto)

valor_aumento = preco_produto*decimal
preco_aumento = preco_produto+valor_aumento

print("O valor do aumento é:", valor_aumento, "e o novo preço do produto é:", preco_aumento)



