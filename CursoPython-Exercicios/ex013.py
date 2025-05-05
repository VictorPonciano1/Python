# EXC 13 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Qual o  seu salário? Digite-o: R$'))

# Operações
promocao = salario * 0.15
salarioFinal = salario + promocao

# Outro jeito de fazer esse calculo
# promocao = salario + (salario * (15 / 100)) -> Neste caso a variável "salarioFinal" é desnecessária

print('Valor do aumento (isolado): R${:.2f}'.format(promocao))
print('Salário após o aumento de 15%: R${:.2f}'.format(salarioFinal))
