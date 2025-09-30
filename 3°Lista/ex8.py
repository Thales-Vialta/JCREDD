class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 
class DoubleNode: 
    def __init__(self, value):
        self.value = value 
        self.prev = None
        self.next = None
def separar_pares_impares():
    n = int(input("Quantos números deseja cadastrar? "))
    pares = None
    impares = None
    
    for _ in range(n):
        num = int(input("Número: "))
        novo = Node(num)
        if num % 2 == 0:
            novo.next = pares
            pares = novo
        else:
            novo.next = impares
            impares = novo
    
    lista = []
    current = pares
    while current:
        lista.append(current.data)
        current = current.next
    current = impares
    while current:
        lista.append(current.data)
        current = current.next
    
    lista.sort()
    head = None
    tail = None
    for num in lista:
        novo = DoubleNode(num)
        if head is None:
            head = tail = novo
        else:
            tail.next = novo
            novo.prev = tail
            tail = novo
    
    print("Ordem crescente:")
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print("\nOrdem decrescente:")
    current = tail
    while current:
        print(current.data, end=" ")
        current = current.prev
