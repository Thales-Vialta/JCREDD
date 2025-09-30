def reverse(lista):
    i, j = 0, len(lista) - 1
    while i < j:
        lista[i], lista[j] = lista[j], lista[i]
        i += 1
        j -= 1
    return lista

# Entrada
lista = list(map(int, input("Digite os elementos da lista separados por espaço: ").split()))
print("Lista invertida:", reverse(lista))
