def calcular_coeficiente_binomial(n, k):
    if k > n:
        return "Erro: k deve ser menor ou igual a n."
    
    coeficiente = 1

    for i in range(1, k + 1):
        coeficiente *= (n - i + 1)
        coeficiente //= i

    return coeficiente

n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

coeficiente = calcular_coeficiente_binomial(n, k)
print(f"O coeficiente binomial ({n} / {k}) é: {coeficiente}")
