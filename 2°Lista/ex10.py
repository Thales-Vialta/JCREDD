def soma(n):
    s = 0
    for i in range(0, n*n):      
        for j in range(1, 2*n):  
            s += 1
    return s
n = int(input("Digite o valor de n: "))
print("Resultado do cálculo (pior caso):", soma(n))
