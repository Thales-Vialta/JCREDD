def triplo_loop(n):
    s = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            for k in range(1, j):
                s += 1
    return s
n = int(input("Digite o valor de n: "))
print("Resultado do cálculo (pior caso):", triplo_loop(n))
