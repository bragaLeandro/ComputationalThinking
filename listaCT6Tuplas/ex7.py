nomes = ("Ana", "Bia", "Celi", "Diana", "Eva", "Fabia")

def possiveisDuplas(nomes):
    for i in range(len(nomes)):
        for j in range(i+1, len(nomes)):
            print(nomes[i], nomes[j])

possiveisDuplas(nomes)