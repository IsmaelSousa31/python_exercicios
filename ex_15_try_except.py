lista_de_frutas = ['Maça', 'Uva', 'Banana']

try:
    indice = int(input('Digite o número da fruta que você quer pegar de 0 a 2: '))
    print('A fruta que você escolheu foi: ', lista_de_frutas[indice])
except IndexError:
    print('Indice é inválido.')
except ValueError:
    print('Você precisa digitar um número.')