def obter_quociente(dividendo, divisor):
    quociente = 0

    for i in range(dividendo, 0, -divisor):
        quociente += 1

    return quociente

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

resultado = obter_quociente(dividendo, divisor)
print("Quociente:", resultado)