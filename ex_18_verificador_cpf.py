"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

contagem = 10

cpf = 0
soma = 0
soma_total = 0

cpf = input('Digite o CPF sem pontos e traços: ')



nove_primeiros = cpf[0:9]

for i in nove_primeiros:
    #print(f'{contagem} x {int(i)} = {contagem * int(i)}')
    soma = contagem * int(i)
    soma_total = soma_total + soma
    contagem -= 1
    

multiplica_por_10 = soma_total * 10

resto_da_divisao = multiplica_por_10 % 11

if resto_da_divisao > 9:
    primeiro_digito = 0
    print(f'Primeiro digíto = {resto_da_divisao}')
else:
    print(f'Primeiro digíto = {resto_da_divisao}')
    primeiro_digito = resto_da_divisao



soma_ = 0
contagem_11 = 11


dez_digitos_cpf = nove_primeiros + str(primeiro_digito)

for x in dez_digitos_cpf:
    #print(f'{contagem_11} x {int(x)} = {contagem_11 * int(x)}')
    soma_ += contagem_11 * int(x)
    contagem_11 -= 1
   

resto_da_divisao_ = (soma_ * 10) % 11

if resto_da_divisao_ > 9:
    segundo_digito = 0
    print(f'Segundo digíto = {resto_da_divisao_}')
else:
    print(f'Segundo digíto = {resto_da_divisao_}')
    segundo_digito = resto_da_divisao_


cpf_completo = dez_digitos_cpf + str(segundo_digito)

if cpf_completo == cpf:
    print(f'CPF {cpf_completo} é válido.')
else:
    print('CPF inválido.')








    


    
    


