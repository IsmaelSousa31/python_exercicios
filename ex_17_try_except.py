try:
    primeiro_numero = float(input('Digite o primeiro número: '))
    segundo_numero = float(input('Digite o segundo número: '))

    resultado = primeiro_numero / segundo_numero

    print(f'O resultado da divisão de {primeiro_numero} / {segundo_numero} = {resultado} ')

except ValueError:
    print("Por favor, digite apenas números.")
except ZeroDivisionError:
    print("Erro: Você digitou zero no segundo número ")