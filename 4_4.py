#Escreva um programa que pergunte o salário do funcionario e calcule
# o valor so aumento. Para salários superioresa R$1.250,00, calcule um
#aumento de 10%. Para os innferiores ou iguais, de 15%.

salario = float(input("Valo do salario: "))

if salario > 1250:
    print("O seu salario atual é de {}".format(salario*1.1))
else:
    print("O seu salrio atual é de{}".format(salario*1.15))