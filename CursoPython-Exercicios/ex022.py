''' EXC 22 - Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome de com todas as letras maiúsculas;
- O nome com todas as letras minúsculas;
- Quantas letras ao todo (sem considerar espaços);
- Quantas letras tem o primeiro nome; '''

nome = str(input('Digite seu nome completo: ')).strip()

print('Impressão de todas as operações:')
print(f'Nome com letras inteiramente maiúsculas: {nome.upper()}')
print(f'Nome inteiramente em minúsculas: {nome.lower()}')
print(f'Total de letras (sem espaços): {len(nome)-nome.count(' ')}')

lista = nome.split()

print(f'Letras do primeiro nome: {len(lista[0])}')
