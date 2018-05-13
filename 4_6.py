#Escreva um programa  que pergunte a distância que um passageiro deseja
#percorrer em km. Calcule o preço da passagem, cobrado R$ 0,50 por km
#para viagem de até de 200km, e R$0,45 para viagens mais longas

distancia = float(input("Digite quantos km serão de viajem: "))

if distancia <= 200:
    print("O preço da passagem será de R${}".format(distancia*0.50))

else:
    print("O preço da passagem será de R${}".format(distancia*0.45))