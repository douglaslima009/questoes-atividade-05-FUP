def calcular_fatorial(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

n = int(input("Digite um número inteiro não negativo: "))

if n >= 0:
    resultado = calcular_fatorial(n)
    print(f"O fatorial de {n} é {resultado}")
else:
    print("O número precisa ser não negativo.")