cod_barras = input("Informe o código de barras: ")

def verifica_digitos(cod_barras):
    i = 0 #utilizada no for para percorrer o código de barras e verifica se tem dígito nele
    c = 0 #utilizada no for para percorrer o código de barras e verifica se tem letra maíscula nele
    cont_letras = 0 #conta a quantidade de letras
    cont_dig = 0 #conta a quantidade de letras
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    digitos = "0123456789"

    for i in cod_barras: #percorre cod_barras para encontrar os dígitos
        if i in digitos:
            cont_dig = cont_dig + 1

    for c in cod_barras: #percorre o cod_barras para encontrar as letras maiusculas
        if c in letras:
            cont_letras = cont_letras + 1

    if cont_dig == 8 and cont_letras == 7:
        return True #Código de barras está correto  
    else:
        return False #Código de barras está incorreto
    
if verifica_digitos(cod_barras):
    print("O código de barras está correto!")
else:
    print("O código de barras está incorreto - Verifique novamente!")
