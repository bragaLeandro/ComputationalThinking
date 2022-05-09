#Dados o número n de alunos de uma turma de algoritmos e suas notas da primeira prova, determinar a média das notas dessa turma. Considere que o usuário digite as informações corretamente.

quant_alunos = int(input("Informe a quantidade de alunos da turma de Algoritmos: "))
i = 0
total = 0

while i < quant_alunos:
    i=i+1
    nota = int(input("Informe a nota do {} aluno: ".format(i)))
    total = total + nota

#calcular media
media = total/quant_alunos

print("A média das notas dessa turma é de {}".format(media))
