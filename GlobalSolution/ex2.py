maior_avaliacao = 0
maior_produto = ""
maiores = ""

produto = input("Informe o nome do produto: ")
avaliacao = float(input("Informe a avaliação do produto: "))

while avaliacao > 0:
    if avaliacao > maior_avaliacao:
        maior_avaliacao = avaliacao
        maior_produto = produto
    elif avaliacao == maior_avaliacao:
        maior_avaliacao = avaliacao
        maior_produto = produto + ", " + maior_produto
    
    produto = input("Informe o nome do produto: ")
    avaliacao = float(input("Informe a avaliação do produto: "))

print("A maior avaliação da loja foi: {}".format(maior_avaliacao))
if maior_avaliacao == 0:
    print("Não houve produto com nota maior que 0")
else:
    print("O(s) produto(s) mais bem avaliado(s) foram: {}".format(maior_produto))