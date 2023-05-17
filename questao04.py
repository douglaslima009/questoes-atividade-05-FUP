n = int(input("Quantos números deseja inserir? "))
numbers = []

for i in range(n):
    number = int(input("Digite o número {}: ".format(i + 1)))
    numbers.append(number)

maior = numbers[0]
menor = numbers[0]

for number in numbers:
    if number > maior:
        maior = number
    if number < menor:
        menor = number
        
print("Maior número: ", maior)
print("Menor número: ", menor)