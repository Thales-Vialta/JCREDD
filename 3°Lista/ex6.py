class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 
def cadastro_funcionarios():
    n = int(input("Quantos funcionários deseja cadastrar? "))
    head = None
    
    for _ in range(n):
        nome = input("Nome: ")
        salario = float(input("Salário: "))
        novo = Node((nome, salario))
        
        if head is None or salario > head.data[1]:
            novo.next = head
            head = novo
        else:
            current = head
            while current.next and current.next.data[1] > salario:
                current = current.next
            novo.next = current.next
            current.next = novo
    
    maior_salario = head.data[1]
    print("Funcionário(s) com maior salário:")
    current = head
    while current and current.data[1] == maior_salario:
        print(current.data[0])
        current = current.next
    
    soma = 0
    qtd = 0
    current = head
    while current:
        soma += current.data[1]
        qtd += 1
        current = current.next
    print(f"Média salarial: {soma/qtd:.2f}")
    
    limite = float(input("Digite um valor limite: "))
    count = 0
    current = head
    while current:
        if current.data[1] > limite:
            count += 1
        current = current.next
    if count > 0:
        print(f"{count} funcionário(s) com salário acima de {limite}")
    else:
        print("Nenhum funcionário com salário acima do valor informado.")
