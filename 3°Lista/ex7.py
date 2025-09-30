class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def cadastro_alunos():
    n = int(input("Quantos alunos deseja cadastrar? "))
    head = None
    tail = None
    
    for _ in range(n):
        nome = input("Nome: ")
        nota = float(input("Nota final: "))
        novo = DoubleNode((nome, nota))
        if head is None:
            head = tail = novo
        else:
            tail.next = novo
            novo.prev = tail
            tail = novo
    
    aprovados = []
    current = head
    while current:
        if current.data[1] >= 7:
            aprovados.append(current.data[0])
        current = current.next
    
    if aprovados:
        print("Alunos aprovados:", ", ".join(aprovados))
    else:
        print("Nenhum aluno aprovado.")
