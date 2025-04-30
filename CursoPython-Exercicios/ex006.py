# EXC 6 - Crie um algoritmo que leia um número e mostre seu dobro, seu triplo e sua raiz quadrada

# Importante biblioteca externa
import math

number = int(input('Digite um número: '))

# Exibir o resultado diretamente sem criar outras variáveis "auxiliares" para isso
print('Seu dobro: {}\nSeu triplo: {}'.format((number*2),(number*3)))

# Jeito 1 de fazer uma raiz quadrada
print('Sua raiz quadrada: {}'.format(number**(1/2)))

# Jeito 2 de fazer uma raiz quadrada
print('Sua raiz quadrada (jeito 2): {}'.format(math.sqrt(number)))

# Jeito 3 de fazer uma raiz quadrada
print('Sua raiz quadrada (jeito 3): {}'.format(pow(number,(1/2))))
