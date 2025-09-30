class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def makeTwoWay(head):
    if head is None:
        return None
    new_head = DoubleNode(head.data)
    current_single = head.next
    current_double = new_head
    while current_single:
        new_node = DoubleNode(current_single.data)
        current_double.next = new_node
        new_node.prev = current_double
        current_double = new_node
        current_single = current_single.next
    return new_head
