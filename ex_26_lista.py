"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""

l1 = [1, 2, 3, 3, 2, 1]
l2 = [1, 2, 3, 4, 5, 6] 
l3 = [1, 4, 9, 8, 9, 4, 8]

def verificar(n1):

    lista_vazia = []
    for n in (n1):
        if n in lista_vazia:
            return n
        else:
            lista_vazia.append(n)

    
    return -1 


print(verificar(l1))
print(verificar(l2))
print(verificar(l3))
        







