class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 
def insert(item, pos, head):
    new_node = Node(item)
    if pos <= 0 or head is None:
        new_node.next = head
        return new_node
    
    current = head
    index = 0
    while current.next and index < pos - 1:
        current = current.next
        index += 1
    new_node.next = current.next
    current.next = new_node
    return head
