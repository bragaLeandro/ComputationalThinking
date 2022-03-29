#Usain Bolt é o recordista mundial dos 100 metros rasos com o tempo de 9,58 segundos. Escreva um algoritmo que calcula a velocidade média em m/s e em km/h de um corredor, seu algoritmo recebe como dados de entrada a distância em metros e o tempo em segundos

distancia_percorrida = float(input("Qual foi a distância percorrida?"))
tempo_percorrido = float(input("Em quantos segundos você percorreu a distância?"))

velocidade_media_ms = distancia_percorrida/tempo_percorrido
velocidade_media_kmh = velocidade_media_ms*3.6

print("Você percorreu", distancia_percorrida, "a uma velocidade de", velocidade_media_ms, "m/s", "o equivalente a", velocidade_media_kmh, "km/h" )