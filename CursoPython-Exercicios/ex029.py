""" EXC 29 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mesnagem dizendo que ele foi multado. A multa vai custar R$7,00 para cada km acima do limite """

from rich import print # A biblioteca rich tem o papel de colorir textos

vel = int(input('Digite a velocidade de seu carro no radar: '))

if vel > 80:
    multa = vel - 80
    print(f"[red]Você foi multado! O valor da multa é: R${multa * 7},00[/red]")
# Esse else é desnecessário (basta só exibir a multa - pelo menos na minha visão)
else:
    print('[green]Estava dentro do limite. Lembre-se de dirigir com segurança![/green]')
