#Escreva um programa para calcular a redução do tempo de tempo de vida de um fumante.
#Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
#Considere que o fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias
#de vida um fumante perderá. Exiba o total em dias.

cigarroPDia = int(input("Digite a quantidade de cigarro que fuma por dia: "))
anos = int(input("Digite a quantos anos já fuma: "))

dias = anos * 365
totalCigarro = dias*cigarroPDia
minutos = totalCigarro * 10

print("Dias a menos {}".format((minutos/24)))