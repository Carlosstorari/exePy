#Escreva um programa que pergunte a velocidade do carro de um usuário.
#Caso ultrapasse 80Km/h, exiba uma  menssagem dizendo que o usuário foi
#multado. Nesse caso, exiba o valor da multa, cobrado R$5 por Km acima de 80Km/h
velocidade = float(input("Valor da velocidade: "))

if velocidade > 80:
    print("Você foi multado")
    print("Sua multa é de R${}".format((velocidade-80)*5))
