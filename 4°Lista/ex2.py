class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, item):
        novo = Node(item)
        novo.next = self.top
        self.top = novo

    def pop(self):
        if self.top is None:
            return None
        item = self.top.data
        self.top = self.top.next
        return item

    def is_empty(self):
        return self.top is None


def verifica_parentizacao_lista(expr):
    pares = {')': '(', ']': '[', '}': '{'}
    pilha = StackLinkedList()
    for ch in expr:
        if ch in "([{":
            pilha.push(ch)
        elif ch in ")]}":
            topo = pilha.pop()
            if topo != pares[ch]:
                return False
    return pilha.is_empty()


print(verifica_parentizacao_lista("{[()]}"))  
print(verifica_parentizacao_lista("{[}]"))   
print(verifica_parentizacao_lista("(()[])"))  
