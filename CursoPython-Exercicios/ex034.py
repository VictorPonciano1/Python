""" EXC 34 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumentpo. Para salários superiores R$1250,00 basta calcular um aumento de 10%. Para salários inferiores ou iguais, basta calcular um aumento de 15% """

salario = float(input('Digite seu salario: '))

if salario > 1250:
    aumento = salario * 0.10 # Também possível: (salario * 10) / 100
    salario += aumento
    print(f'Valor do aumento: {aumento}\nSalário pós aumento de 10%: R${salario}')
else:
    aumento = salario * 0.15 # Também possível: (salario * 15) /100
    salario += aumento
    print(f'Valor do aumento: {aumento}\nSalário pós aumento: R${salario}')
