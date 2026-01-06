lista = []


while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()

    if opcao == 'i':
        valor = input('Insira um valor para adicionar a lista: ')
        lista.append(valor)
        print(f'Valor {valor} adicionado com sucesso a lista.')
        
    elif opcao == 'a':
        try:
            valor = int(input('Insira o índice que deseja apagar: '))
        
            lista.pop(valor)
            print(f'índice {valor} apagado com sucesso.')

        except IndexError:
            print('Índice não existe na lista.')
        except ValueError:
            print('Não foi possivel apagar esse índice.')
        except Exception:
            print('Erro desconhecido.')
            
    elif opcao == 'l':
        if lista == []:
            print('Lista vazia')
        else:
            n = 0

            for i in lista:
                print(n, '-', i)
                n = n + 1

    elif opcao == 's':
        print('Saindo...')
        break

   
        
    
        



    
    