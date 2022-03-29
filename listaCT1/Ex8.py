#Dados o preço de um produto e um percentual de desconto, escreva um algoritmo que calcula e mostra o valor do desconto e o novo preço do produto dado o percentual. E se, ao invés de um desconto, fosse um aumento. O que muda no seu algoritmo?
permitidos = ("aumento", "desconto")
preco_produto = float(input("Qual o preço do produto?"))
pergunta = input("É um aumento ou desconto? ")

while pergunta not in permitidos:
    print("Resposta inválida")
    quit()

if pergunta == "desconto":
    desconto = float(input("Qual a porcentagem de desconto? (Se for 10%, digite 0.10)"))
    
    while desconto>1:
        print("Valor inválido")
        quit()
    
    valor_desconto = preco_produto*desconto
    print("O valor do desconto é:", valor_desconto, "e o novo preço do produto é:", preco_produto-valor_desconto)
    
elif pergunta == "aumento":
    aumento = float(input("Qual a porcentagem de aumento? (Se for 10%, digite 0.10)"))

    while aumento>1:
        print("Valor inválido")
        quit()
    
    valor_aumento = preco_produto*aumento
    print("O valor do aumento é:", valor_aumento, "e o novo preço do produto é:", preco_produto+valor_aumento)