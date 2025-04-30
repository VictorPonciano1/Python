# EXC 4 - Faça um programa que leia algo digitado pelo usuário mostre na tela seu tipo primitivo e todas as informações possíveis sobre esse algo

algo = input('Digite algo: ')

tamanho = len(algo) # Função adicional

print('O tipo primitivo do que você digitou é {}'.format(type(algo)))
print('É numérico? {}'.format(algo.isnumeric()))
print('Tamanho desse algo digitado: {}'.format(tamanho))
print('É um valor alfabético (apenas caracteres)? {}'.format(algo.isalpha()))
print('É alphanumérico? {}'.format(algo.isalnum()))
print('Está totalmente em Minúsculo?', algo.islower())
print('Está totalmente em Maiúsculo?', algo.isupper())
print('É um campo com somente \"espaços\"?', algo.isspace())
print('Está capitalizada?', algo.istitle())
