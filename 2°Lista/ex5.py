def inserir_ordenado(vetor, num):
    i = len(vetor) - 1
    vetor.append(num)  # aumenta o tamanho
    while i >= 0 and vetor[i] > num:
        vetor[i + 1] = vetor[i]  # desloca
        i -= 1
    vetor[i + 1] = num
    return vetor

vetor = list(map(int, input("Digite os elementos do vetor ordenado separados por espaço: ").split()))
num = int(input("Digite o número a ser inserido: "))

print("Novo vetor:", inserir_ordenado(vetor, num))
