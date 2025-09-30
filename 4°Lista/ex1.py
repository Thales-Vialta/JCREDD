class StackArray:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


def verifica_parentizacao_array(expr):
    pares = {')': '(', ']': '[', '}': '{'}
    pilha = StackArray()
    for ch in expr:
        if ch in "([{":
            pilha.push(ch)
        elif ch in ")]}":
            topo = pilha.pop()
            if topo != pares[ch]:
                return False
    return pilha.is_empty()

print(verifica_parentizacao_array("{[()]}"))   
print(verifica_parentizacao_array("{[(])}"))   
print(verifica_parentizacao_array("((()))"))   
