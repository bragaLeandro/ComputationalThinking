#Dados o preço de um produto e um percentual de desconto, escreva um algoritmo que calcula e mostra o valor do desconto e o novo preço do produto dado o percentual. E se, ao invés de um desconto, fosse um aumento. O que muda no seu algoritmo?
permitidos = ("aumento", "desconto")

def calcula_novo_preco(preco_produto, percentual, tipo):
    if tipo == "desconto":
        return preco_produto - (preco_produto*percentual)/100
    else:
        return preco_produto + (preco_produto*percentual)/100

def calcula_diferenca(preco_produto , percentual):
     return (preco_produto*percentual)/100

tipo = input("É um aumento ou desconto? ")

while tipo not in permitidos:
    print("Resposta inválida")
    tipo = input("É um aumento ou desconto? ")
    
preco_produto = float(input("Qual o preço do produto?"))
percentual = float(input("Qual a porcentagem de " + tipo + "?"))

valor_total = calcula_novo_preco(preco_produto, percentual, tipo)
diferenca = calcula_diferenca(preco_produto, percentual)

print("O valor total do produto é:" , valor_total, "e o valor do", tipo, "é", diferenca)