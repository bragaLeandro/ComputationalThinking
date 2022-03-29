#No exercício da calculadora, visto em sala de aula, temos um problema com a operação de divisão. Sua tarefa exibir uma mensagem informando que é impossível fazer uma divisão por 0. Note que, essa mensagem só deverá aparecer quando o usuário quiser fazer tal operação.

x = int(input("Digite um número:"))
y = int(input("Digite outro número"))

divisao = x/y

if y == 0:
    print("Não é possível realizar a divisão de um número por 0")
else:
    print("A divisão entre" , x , "e" , y , "é: " , divisao)