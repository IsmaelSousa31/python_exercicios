# Exercício 3: O Tradutor Simples (Verificação)

dicionario = {'dog': 'cachorro', 'cat': 'gato', 'book': 'livro'}

palavra = input('Digite uma palavra em inglês: ').lower()

if palavra in dicionario:
    print(dicionario[palavra])
else:
    print('Palavra não encontrada no dicionário.')


