# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


novos_produtos = [
    {**copy.deepcopy(p), 'preco': round(p['preco'] * 1.1, 2)}
    for p in produtos
]
print('Produtos com aumento de 10%')
print(*novos_produtos, sep='\n')
print( )


copia_profunda = copy.deepcopy(produtos)
print('Cópia Profunda dos Produtos Originais')
print(*copia_profunda, sep='\n')
print( )

# Ordene os produtos por nome decrescente (do maior para menor)
print('Produtos ordenados por nome decrescente')
produtos_Z_A = sorted(
    copy.deepcopy(produtos), 
    key=lambda p: p['nome'], 
    reverse=True
)


print(*produtos_Z_A, sep='\n')
print( )

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
print('Produtos ordenados por nome por Deep Copy')
produtos_ordenados_por_nome_decrescente = sorted(
    copia_profunda, 
    key=lambda p: p['nome'], 
)
print(*produtos_ordenados_por_nome_decrescente, sep='\n')
print( )


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
print('Produtos ordenados por preco crescente')
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos), 
    key=lambda p: p['preco'], 
)

print(*produtos_ordenados_por_preco, sep='\n')
print( )



