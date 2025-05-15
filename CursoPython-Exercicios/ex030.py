# EXC 30 - Crie um programa que leia um número inteiro e exiba se ele é PAR ou ÍMPAR

from rich import print

n = int(input('Digite um número: '))

if (n % 2 == 0):
    print('[green]Número par[/green]')
else:
    print('[red]Número ímpar[/red]')
