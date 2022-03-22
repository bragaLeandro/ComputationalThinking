# O RM de um aluno da FIAP é composto por 5 dígitos. Sua tarefa é escrever um algoritmo que recebe um RM e retorna a somatória de todos os dígitos do RM. Por exemplo, suponha que o aluno tenha o RM 56395, seu algoritmo deverá imprimir como saída 28 = 5 + 6 + 3 + 9 + 5. Dica: realize várias divisões e restos de divisões por 10.

from zmq import ContextTerminated


rm = int(input("Digite o seu RM: "))

unidade = rm%10
conta_dezena = rm//10
dezena = conta_dezena%10
conta_centena = conta_dezena//10
centena = conta_centena%10
conta_milhar = conta_centena//10
milhar = conta_milhar%10
conta_dezena_milhar = conta_milhar//10
dezena_milhar = conta_dezena_milhar%10

soma_RM = (dezena_milhar + milhar + centena + dezena + unidade)
print("A soma dos 5 números do seu RM dá:", soma_RM)