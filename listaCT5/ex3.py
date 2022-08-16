def substitui(letra, palavra):
    i = 0
    letra = letra.lower()
    palavra = palavra.lower()
    aux = ""
    while i < len(palavra):
        if palavra[i] == letra:
            aux = aux + '*'
        else:   
            aux = aux + palavra[i]
        i = i+1
    print(aux)
    return aux

print(substitui('l', "Leandro"))