#altere o algoritmo anterior para, além da média, contar os alunos que tiraram entre 0 e 5 (0<=nota<=5) e acima de 5 (nota >=5)


quant_alunos = int(input("Informe a quantidade de alunos da turma de Algoritmos: "))
i = 0
total = 0
maior_que5 = 0
menor_que5 = 0
while i < quant_alunos:
    i=i+1
    nota = int(input("Informe a nota do {} aluno: ".format(i)))
    total = total + nota

    if nota >= 0 and nota <=5:
        menor_que5 = menor_que5 + 1
    elif nota > 5:
        maior_que5 = maior_que5 + 1

#calcular media
media = total/quant_alunos

print("A média das notas dessa turma é de {}".format(media))
print("{} alunos tiraram entre 0 e 5".format(menor_que5))
print("{} alunos tiraram nota acima de 5".format(maior_que5))