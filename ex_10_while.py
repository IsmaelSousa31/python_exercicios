palavra = str('corrida')
palavra_com_asterisco = str('') 
letra_do_usuario = str('') 
num_tentativas = 0
i = 0

while i < len(palavra):
    palavra_com_asterisco += '*'
    i += 1 

r = 1
while r:
    print(f'Palavra: {palavra_com_asterisco}')
    letra_do_usuario = str(input('Digite uma letra: '))
    num_tentativas += 1

    n = 0
    while n < len(palavra):
        if letra_do_usuario == palavra[n]:
            palavra_com_asterisco[n] = letra_do_usuario
            print(palavra_com_asterisco)
        n += 1
    else:
        print('Palavra errada, tente novamente. ')

        
    if palavra == palavra_com_asterisco:
        print(f'Parabéns você acertou a palavra {palavra}')
        print(f'Número de tentativas: {num_tentativas}')
        break

    r += 1
