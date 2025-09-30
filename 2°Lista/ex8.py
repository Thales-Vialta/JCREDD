def multiplica_matrizes(A, B, n):
    mat = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mat[i][j] += A[i][k] * B[k][j]
    return mat
n = int(input("Digite a dimensão n da matriz quadrada: "))
print("Digite a matriz A:")
A = [list(map(int, input().split())) for _ in range(n)]
print("Digite a matriz B:")
B = [list(map(int, input().split())) for _ in range(n)]
resultado = multiplica_matrizes(A, B, n)
print("Matriz resultante:")
for linha in resultado:
    print(linha)
