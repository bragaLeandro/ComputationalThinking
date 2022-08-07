valores = (10000,30000,90000,30000)


def calcula_media(valores):
    aux = 0
    for i in valores:
        aux = aux + i
    return aux/len(valores)

def desvioPadrao(valores):
    aux = 0
    for i in valores:
        aux = aux + (i - calcula_media(valores))**2
    return (aux/len(valores))**(1/2)

