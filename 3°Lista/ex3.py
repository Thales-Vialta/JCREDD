def pop(pos, head):
    if head is None:
        raise IndexError("Lista vazia")
    if pos == 0:
        return head.next, head.data
    current = head
    index = 0
    while current.next and index < pos - 1:
        current = current.next
        index += 1
    if current.next is None:
        raise IndexError("Posição fora da lista")
    removed = current.next
    current.next = removed.next
    return head, removed.data
