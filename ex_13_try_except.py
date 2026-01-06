try:
    numerador = float(input("Digite o numerador: "))
    denominador = float(input("Digite o denominador: "))
    
    resultado = numerador / denominador
    print(f"O resultado é: {resultado}")

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")