# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

#meu código

numero =  int(input('Digite um numero: '))

def multiplicar(n):
    return 2 * n

def triplicar(n):
    return 3 * n

def quadruplicar(n):
    return 4 * n

print(multiplicar(numero))
print(triplicar(numero))
print(quadruplicar(numero))

#código do professor

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
