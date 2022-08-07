nomes = ("Ana", "Bia", "Celi", "Diana", "Eva", "Fabia")

def maiorString(nomes):
    maior = 0
    maiorNome = ""
    for i in range(len(nomes)):
        if len(nomes[i]) > maior:
            maior = len(nomes[i])
            maiorNome = nomes[i]
    return maiorNome

maiorString = maiorString(nomes)

print(maiorString)