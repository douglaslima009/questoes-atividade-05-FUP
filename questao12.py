def verificar_perfeito(numero):
    soma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            soma += divisor

    if soma == numero:
        return True
    else:
        return False

numero = int(input("Digite um número inteiro e positivo: "))
if verificar_perfeito(numero):
    print(numero, "é um número perfeito.")
else:
    print(numero, "não é um número perfeito.")