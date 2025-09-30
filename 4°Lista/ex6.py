def percorrer_pilha_recursivo(no):
    if no is None:
        return
    print(no.data)
    percorrer_pilha_recursivo(no.next)
    
def percorrer_fila_recursivo(no):
    if no is None:
        return
    print(no.data)
    percorrer_fila_recursivo(no.next)
