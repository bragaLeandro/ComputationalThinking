#Escreva um algoritmo que recebe a idade de um nadador e mostra sua categoria conforme a tabela a seguir

idade_nadador = int(input("Digite a idade do nadador: "))

if idade_nadador>=5 and idade_nadador<=7:
    print("A categoria do nadador é: Infantil")
elif idade_nadador>=8 and idade_nadador<=10:
    print("A categoria do nadador é: Juvenil")
elif idade_nadador>=11 and idade_nadador<=15:
    print("A categoria do nadador é: Adolescente")
elif idade_nadador>=16 and idade_nadador<=30:
    print("A categoria do nadador é: Adulto")
elif idade_nadador>30:
    print("A categoria do nadador é: Senior")
