""" EXC 28 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5  e peçapara o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu """

import random
from time import sleep

print('Eu, o SUPER COMPUTADOR, pensei em um número!')

pc = random.randint(0, 5)

numero = int(input('Em qual número eu estava pensando? Digite-o e teste sua sorte: '))
print('---PROCESSANDO---')
sleep(3) # Faz com que o código tenha uma espécie de delay

if numero == pc:
    print('Parabéns, você me venceu')
else:
    print('Hahaha, você errou! Tente na próxima.')
