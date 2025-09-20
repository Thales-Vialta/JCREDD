def busca_sequencial_ordenada(lista, alvo):
    for elem in lista:
        if elem == alvo:
            return True
        elif elem > alvo: 
            break
    return False
lista = list(map(int, input("Digite os elementos da lista ordenada separados por espaço: ").split()))
alvo = int(input("Digite o valor que deseja buscar: "))

if busca_sequencial_ordenada(lista, alvo):
    print("Elemento encontrado!")
else:
    print("Elemento NÃO encontrado!")
