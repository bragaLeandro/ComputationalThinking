#Faça um programa para ler dois números inteiros A e B e informar se A é divisível por B

num_a = int(input("Informe o número A: "))
num_b = int(input("Informe o número B: "))

resto = num_a%num_b

if resto == 0:
    print("O número", num_a, "é divisivel por", num_b, "pois o resto desta divisão é 0")
else:
    print("O número", num_a, "não é divisivel por", num_b, "pois o resto desta divisão é", resto)
    
    