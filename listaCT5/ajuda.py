def maximo(n1, n2, lim):
    aux = 0
    if n1 > lim:
        aux = aux + 1
    if n2 > lim:
        aux = aux + 1
    else:
        aux = 0
    return aux


print(maximo(1,2,1))