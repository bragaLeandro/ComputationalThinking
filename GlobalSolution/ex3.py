cod_barras = input("Informe o código de barras: ")

def digitos(cod_barras):
    i = 0
    cont = 0
    while i < len(cod_barras):
        if cod_barras[i] == '0' or cod_barras[i] == '1' or cod_barras[i]== '2' or cod_barras[i]== '3' or cod_barras[i]== '4' or cod_barras[i]== '5' or cod_barras[i]== '6' or cod_barras[i]== '7' or cod_barras[i]== '8' or cod_barras[i]== '9':
            cont = cont + 1
        i = i + 1
    return cont

quant = digitos(cod_barras)

print("A quantiade de dígitos no código de barras é de: {}".format(quant))