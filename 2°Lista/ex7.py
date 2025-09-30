def ache_min(array, n):
    mini = array[0]
    for i in range(n):
        if array[i] < mini:
            mini = array[i]
    return mini

n = int(input("Digite o tamanho do array: "))
array = list(map(int, input("Digite os elementos separados por espaço: ").split()))

print("Mínimo encontrado:", ache_min(array, n))
