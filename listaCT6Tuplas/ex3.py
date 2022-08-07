t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def imprimeMaiorElemento(t):
    maior = t[0]
    for i in t:
        if i > maior:
            maior = i
    return maior

print(imprimeMaiorElemento(t))