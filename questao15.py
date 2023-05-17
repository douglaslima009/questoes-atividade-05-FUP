for num in range(1000, 10000):
    d1 = num // 1000
    d2 = (num // 100) % 10
    d3 = (num // 10) % 10
    d4 = num % 10
    
    if (d1 + d2) ** 2 == num:
        print(num)
