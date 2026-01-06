produtos_e_precos = {'arroz': 20.00, 'feijao': 10.00, 'macarrão': 16.00, 'uva':10.00}

try:
    produto = str(input('Digite o nome do produto para consultar o seu valor: ')).lower()
    print(f"Produto digitado: {produto} | Valor: R$ {produtos_e_precos[produto]}")
except KeyError:
    print('Produto não encontrado.')