# Exercício 2: Atualizando o Estoque (Modificação)

estoque = {'mouse':10, 'teclado':5, 'monitor':2}

print(f"Estoque atual: {estoque}")

print("Um cliente comprou 2 mouses. atualizando o estoque...")

estoque["mouse"] = 8
print(f"Estoque atual: {estoque}")

print("Chegou um produto novo: headset, quantidade: 3. Atualizndo o estoque")

estoque['headset'] = 3

print(f'Estoque final: {estoque}')

