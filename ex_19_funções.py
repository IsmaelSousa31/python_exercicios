# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplicar(x, y, *args):
    total = 1
    for numero in args:
        total *= numero

    return total
    
variavel = multiplicar(10, 20, 10, 4, 2)

print(variavel)