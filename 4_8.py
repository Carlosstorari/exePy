#Escreva que leia dois números e que pergunte qual operação você deseja
#realizar. Você deve poder calcular a soma (+), subtração(-), multiplicação(*),
# e divisão (/). Exiba o resultado da operação solicitada.

n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
opc = str(input("Digite a operação que deseja, +, -, /, * : "))

if opc == '+':
    print("{} + {} = {}".format(n1, n2, (n1+n2)))
elif opc == '-':
    print("{} - {} = {}".format(n1, n2, (n1 - n2)))
elif opc == '*':
    print("{} * {} = {}".format(n1, n2, (n1 * n2)))
elif opc == '/':
    print("{} / {} = {}".format(n1, n2, (n1 / n2)))