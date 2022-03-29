##Faça um algoritmo que leia as médias semestrais obtidas por um aluno na disciplina de Computational Thinking, o número de aulas ministradas e número de aulas assistidas por este aluno nesta disciplina. Calcule e mostre a média final deste aluno e diga se ele foi aprovado ou reprovado ou está de exame. Lembrando que a média do primeiro semestre tem peso 4 e a do segundo peso 6, além disso, o aluno tem que ter frequentando mais de 70% das aulas.

aulas_ministradas = int(input("Informe a quantidade de aulas ministradas nesta disciplina: "))
aulas_assistidas = int(input("Informe a quantidade de aulas assistidas nesta disciplina: "))
media_1sem = float(input("Informe a média do primeiro semestre: "))
media_2sem = float(input("Informe a média do segundo semestre: "))

peso_media_1sem = media_1sem*0.4
peso_media_2sem = media_2sem*0.6
media_anual = (peso_media_1sem + peso_media_2sem)
frequencia = (aulas_assistidas/aulas_ministradas)*100

if media_anual >= 6 and frequencia >= 70:
    print("A média final do aluno é", media_anual, "e ele cumpriu o curso com a frequência de:", frequencia,"%", ". Contudo a situação é: Aprovado")
elif media_anual < 6 or frequencia < 70:
    print("A média final do aluno é", media_anual, "e ele cumpriu o curso com a frequência de:", frequencia,"%", ". Contudo a situação é: Reprovado")

