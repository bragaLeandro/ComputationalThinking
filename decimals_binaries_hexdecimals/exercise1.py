cpf = int(input("Digite o seu CPF:"))

cpf_abc = cpf//100000000
resto = cpf%100000000
print(cpf_abc)
print(resto)

cpf_def = resto//100000
resto = cpf%100000
print(cpf_def)
print(resto)

cpf_ghi = resto//100
resto = cpf%100
print(cpf_ghi)
print(resto)

cpf_formatado = (cpf_abc,'.',cpf_def,'.',cpf_ghi,'-',resto)

print(cpf_formatado)



