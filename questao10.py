def calcular_mdc(a, b):
    if a <= 0 or b <= 0:
        return "Os números devem ser inteiros positivos."

    mdc = min(a, b)

    for i in range(mdc, 0, -1):
        if a % i == 0 and b % i == 0:
            mdc = i
            break
    
    return mdc

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = calcular_mdc(num1, num2)

print("O Máximo Divisor Comum (MDC) de", num1, "e", num2, "é:", resultado)
