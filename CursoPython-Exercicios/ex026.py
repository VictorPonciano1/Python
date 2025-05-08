''' EXC 26 - Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A";
- Em que posição ela aparece a primeira vez;
- Em que posição ela aparece a última vez; '''

frase = str(input('Digite uma frase: ')).lower().strip()

print(f'Quantas vezes a letra \'a\' aparece: {frase.count('a')} vezes')

# find "normal": - começa sua procura do lado esquerdo de forma padrão -->
print(f'Sua primeira aparição foi na posição: {frase.find('a')+1}')

# rfind: right find - começa a procura do lado direito <--
print(f'Sua última aparição foi na posição: {frase.rfind('a')+1}')
