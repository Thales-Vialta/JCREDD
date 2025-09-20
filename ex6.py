def tem_duplicacao(array, n):
    acho = False
    for i in range(n):
        val = array[i]
        for j in range(i + 1, n):
            if array[j] == val:
                acho = True 
    return acho
n = int(input("Digite o tamanho do array: "))
array = list(map(int, input("Digite os elementos separados por espaço: ").split()))

print("Tem duplicação?", tem_duplicacao(array, n))
