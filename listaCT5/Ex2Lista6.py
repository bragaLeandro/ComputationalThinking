def insere_branco(palavra):
    nova = ""
    i = 0
    while i < len(palavra):
        nova = nova + palavra[i] + " "
        i = i + 1
    return nova

resp = insere_branco('Melancia')
print(resp)