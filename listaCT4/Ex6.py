def contadigitos(numero, d):
    contador = 0
    while numero != 0:
        resto = numero % 10
        if resto == d:
            contador = contador + 1
        
        numero = numero // 10

    return contador

resp = contadigitos(283940282, 8)
print(resp)


