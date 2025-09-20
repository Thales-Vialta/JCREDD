def compara_vetor(V, n):
    for i in range(0, n, 2):       
        for j in range(n, -1, -1):
            if V[i] < V[j]:
                print(i)
n = int(input("Digite o tamanho do vetor: "))
V = list(map(int, input("Digite os elementos do vetor separados por espaço: ").split()))
compara_vetor(V, n)
