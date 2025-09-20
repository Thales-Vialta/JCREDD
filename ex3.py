def expo(base, exp):
    resultado = 1
    while exp > 0:
        if exp % 2 == 1:   
            resultado *= base
        base *= base
        exp //= 2
    return resultado
base = int(input("Digite a base: "))
exp = int(input("Digite o expoente (não negativo): "))
print(f"{base}^{exp} = {expo(base, exp)}")
