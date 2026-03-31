
class Node:
    '''класс, представляющий узел односвязного списка'''

    def __init__(self, data):
        '''
        инициализация узла односвязного списка

        :param data: Данные, которые будут храниться в узле
        '''

        self.data = data
        self.next = None


def get_second_node(P1):
    '''
    возвращает указатель на второй элемент списка

    :param P1: ссылка на первый элемент списка (голову)
    :return: указатель на второй элемент списка
    '''

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