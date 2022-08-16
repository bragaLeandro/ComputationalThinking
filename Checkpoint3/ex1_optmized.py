while quantidade >= 0:
    i = i + 1 #incrementação do contador implementado na linha 1
    produto = input("Informe o {}° produto: ".format(i)) #input do produto
    quantidade = int(input("Informe a quantidade do {}° produto: ".format(i))) #input da qtd
    preco = float(input("Informe o preço do {}° produto: ".format(i))) #input do preço
    
    capitalizacao = quantidade*preco #capitalização é o valor agregado que o exercício pede

    if capitalizacao > cap_bckp: #estrutura de decisão para salvar o produto com maior capitalização
        preco_bckp = preco
        prod_bckp = produto
        quant_bckp = quantidade
        cap_bckp = capitalizacao

    if quantidade > maior_quant: #estrutura de decisão para salvar o produto com maior quantidade
        maior_quant = quantidade
        maior_prod = produto

if maior_quant <= 0:
    print("Não existe produto com quantidade positiva!")
else:
    print("O produto com a maior quantidade de itens é: {}".format(maior_prod))

if cap_bckp <=0:
    print("Não existe produto com valor agregado positivo!")
else:
    print("O produto com o maior valor agregado é: {}".format(prod_bckp))