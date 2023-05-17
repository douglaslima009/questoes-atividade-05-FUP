def calcular_potencia(x, n):
    resultado = 1
    for _ in range(n):
        resultado *= x
    return resultado

x = int(input("Digite o valor de x: "))
n = int(input("Digite o valor de n (inteiro não-negativo): "))

resultado = calcular_potencia(x, n)

print(f"{x} elevado a {n} é igual a {resultado}")