# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def numero(n):
    if n % 2 == 0: 
        return f'{n} é par'
    return f'{n} é impar'
    

print(numero(5))
print(numero(3))
print(numero(8))
print(numero(368))