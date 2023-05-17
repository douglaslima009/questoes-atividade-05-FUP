def calcular_numero_binomial(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return calcular_numero_binomial(n-1, k-1) + calcular_numero_binomial(n-1, k)

def exibir_triangulo_pascal(num_linhas):
    for linha in range(num_linhas):
        for coluna in range(linha + 1):
            coeficiente = calcular_numero_binomial(linha, coluna)
            print(coeficiente, end=" ")
        print()

num_linhas = int(input("Digite o número de linhas do Triângulo de Pascal: "))
exibir_triangulo_pascal(num_linhas)