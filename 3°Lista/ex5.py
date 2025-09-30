class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 
        
def cadastro_produtos():
    n = int(input("Quantos produtos deseja cadastrar? "))
    head = None
    
    for _ in range(n):
        codigo = input("Código: ")
        preco = float(input("Preço: "))
        qtd = int(input("Quantidade: "))
        novo = Node((codigo, preco, qtd))
        novo.next = head
        head = novo
    
    desconto = float(input("Digite a taxa de desconto (%): "))
    desconto = desconto / 100
    
    current = head
    qtd_maior_500 = 0
    while current:
        codigo, preco, qtd = current.data
        preco_desc = preco * (1 - desconto)
        current.data = (codigo, preco_desc, qtd)
        print(f"Código: {codigo}, Novo preço: {preco_desc:.2f}")
        if qtd > 500:
            qtd_maior_500 += 1
        current = current.next
    
    print(f"Quantidade de produtos com estoque > 500: {qtd_maior_500}")
