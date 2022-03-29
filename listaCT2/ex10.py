#Escreva um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida para efetuar o cálculo adequado.
#codigo: 1 | condição de pagamento: A vista em dinheiro ou cheque, recebe 10% de desconto.
#codigo: 2 | condição de pagamento: A vista no cartão de crédito, recebe 5% de desconto.
#codigo: 3 | condição de pagamento: Em duas vezes, preço normal de etiqueta sem juros.
#codigo: 4 | condição de pagamento: Em quatro vezes, preço normal de etiqueta mais juros de 7%.
permitidos = (1, 2, 3, 4)

preco_produto = float(input("Informe o valor do produto: "))
codigo_pagamento = int(input("Qual a condição de pagamento? (1 a 4)"))

while codigo_pagamento > 4 or codigo_pagamento < 1:
    print("Resposta inválida")
    codigo_pagamento = int(input("Qual a condição de pagamento? (1 a 4)"))

if codigo_pagamento == 1:
    valor_total = preco_produto - (preco_produto*0.1)
    print("O valor total do produto é: {}".format(valor_total))
elif codigo_pagamento == 2:
     valor_total = preco_produto - (preco_produto*0.05)
     print("O valor total do produto é:", valor_total)
elif codigo_pagamento == 3:
     valor_total = preco_produto
     print("O valor total do produto é:", valor_total)
elif codigo_pagamento == 4:
    valor_total = preco_produto + (preco_produto*0.07)
    print("O valor total do produto é:", valor_total)
