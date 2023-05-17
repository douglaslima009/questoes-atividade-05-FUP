def calcular_mmc(num1, num2):
    # Encontrando o máximo entre os dois números
    maior = max(num1, num2)
    
    while True:
        if maior % num1 == 0 and maior % num2 == 0:
            mmc = maior
            break
        maior += 1
    
    return mmc

# Solicitar entrada do usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Chamar a função calcular_mmc e imprimir o resultado
resultado = calcular_mmc(num1, num2)
print("O mínimo múltiplo comum de", num1, "e", num2, "é", resultado)