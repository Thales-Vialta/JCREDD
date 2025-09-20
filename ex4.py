def esta_ordenado(vetor):
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:
            return False
    return True

vetor = list(map(int, input("Digite os elementos do vetor separados por espaço: ").split()))

if esta_ordenado(vetor):
    print("ORDENADO")
else:
    print("NÃO ORDENADO")
