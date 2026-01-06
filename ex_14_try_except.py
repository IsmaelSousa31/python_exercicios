try:
    idade = int(input("Digite a sua idade: "))
    
    print(f"A sua idade é: {idade}")

except ValueError:
    print("Por favor, digite apenas números inteiros.")