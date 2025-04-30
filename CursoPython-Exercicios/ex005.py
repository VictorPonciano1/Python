# EXC 5 - Faça um programa que leia um número inteiro e mostre seu sucessor e antecessor

number = int(input('Digite um número: '))

# Jeito 1 de imprimir os valores
print('Número digitado: {}\nAntecessor: {}\nSucessor: {}'.format(number, number-1, number+1))

# Espaçamento
print('')

# Jeito 2 de imprimir os valores - Declarando variáveis
antecessor = number-1
sucessor = number+1

print('Número: {}\nAntecessor: {}\nSucessor: {}'.format(number, antecessor, sucessor))
