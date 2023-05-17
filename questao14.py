num_casas = 64 
graos_total = 0 

for casa in range(num_casas):
    graos_casa = 2 ** casa
    graos_total += graos_casa
    
print("A quantidade total de grãos de trigo a ser paga à Rainha é:", graos_total)
