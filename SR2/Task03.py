#Дан односвязный линейный список и указатель на голову списка P1.
# Необходимо вывести указатель на второй элемент этого списка P2.
# Известно, что в исходном списке не менее 5 элементов.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_second_node(P1):
    return P1.next

P1 = Node(1)
P2 = Node(2)
P3 = Node(3)
P4 = Node(4)
P1.next = P2
P2.next = P3
P3.next = P4

second_node = get_second_node(P1)

print("Указатель на второй элемент (P2):", second_node.data)