# EXC 7 - Desenvolve um programa que leia as duas notas de um aluno, então calcule e mostre sua média

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

# Imprimindo com 1 casa decimal já trabalhando com as regras de arredondamento
print('Notas no aluno: {:.1f} e {:.1f}'.format(nota1, nota2))
print('Média do aluno: {:.1f}'.format(media))
