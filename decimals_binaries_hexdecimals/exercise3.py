cpf = 457150898
backup_cpf = cpf
mult = 2
soma = 0

while cpf!=0:
    resto = cpf % 10
    cpf = cpf//10
    soma = soma + resto * mult
    mult = mult + 1

resto = soma % 11

if resto < 2:
    print(0)
else:
    print(11-resto)