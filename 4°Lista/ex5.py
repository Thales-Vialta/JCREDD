class QueueArray:
    def __init__(self, capacidade):
        self.items = [None] * capacidade
        self.inicio = 0
        self.fim = -1
        self.tamanho = 0
        self.capacidade = capacidade

    def enqueue(self, item):
        if self.tamanho == self.capacidade:
            raise Exception("Fila cheia")
        self.fim = (self.fim + 1) % self.capacidade
        self.items[self.fim] = item
        self.tamanho += 1

    def dequeue(self):
        if self.tamanho == 0:
            raise Exception("Fila vazia")
        item = self.items[self.inicio]
        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1
        return item

    def is_empty(self):
        return self.tamanho == 0

fila = QueueArray(5)
fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(30)
print(fila.dequeue()) 
print(fila.dequeue()) 
