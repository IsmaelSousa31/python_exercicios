'''
Criar as duas listas abaixo no seu programa:
lista_sexta = ["Ana", "Bruno", "Caio", "Ana", "Daniela"]
lista_sabado = ["Caio", "Fábio", "Beatriz", "Daniela", "Fábio"]
Criar um único conjunto que contenha todos os convidados de ambos os dias, mas sem nenhuma repetição.
Exibir o nome de cada convidado da lista final, um por linha, em ordem alfabética.
'''
lista_sexta = ["Ana", "Bruno", "Caio", "Ana", "Daniela"]
lista_sabado = ["Caio", "Fábio", "Beatriz", "Daniela", "Fábio"]
l_sexta = set(lista_sexta)
l_sabado = set(lista_sabado)

lista_uniao = l_sexta | l_sabado 

for pessoa in sorted(lista_uniao):
    print(pessoa)