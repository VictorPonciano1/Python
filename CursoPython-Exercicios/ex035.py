# EXC 35 - Desenvolva um programa que leia o comprimento de três (3) retas e diga se elas podem formar um triângulo

reta1 = int(input('Digite o comprimento da reta 1: '))
reta2 = int(input('Digite o comprimento da reta 2: '))
reta3 = int(input('Digite o comprimento da reta 3: '))

# Fazendo a verificação
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Podemos ter triângulo')
else:
    print('impossível ter triângulo')
