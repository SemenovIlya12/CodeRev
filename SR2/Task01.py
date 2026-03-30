
class Node:
    '''узел стека'''

    def __init__(self, data):
        '''
        инициализация узла стека.

        :param data: данные для хранения в узле.
        '''
        self.data = data
        self.next = None

class Stack:
    '''класс, представляющий стек'''

    def __init__(self):
        '''инициализация пустого стека'''
        self.top = None

    def push(self, data):
        '''
        добавляет элемент в стек

        :param data: данные, которые будут добавлены в стек
        :return:
        '''
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def peek(self):
        '''
        возвращает ссылку на вершину стека.
        если стек пуст - возвращает None

        :return: вершина стека (Node) или None, если стек пуст.
        :rtype: Node | None
        '''
        return self.top

def create_stack():
    '''
    создает стек и заполняет его N числами,
    введенными пользователем, и возвращает ссылку
    на вершину стека

    :return: вершина созданного стека (Node)
    :rtype: Node | None
    '''
    N = int(input("Введите количество чисел (N > 0): "))
    stack = Stack()
    for _ in range(N):
        num = int(input())
        stack.push(num)
    return stack.peek()

top_node = create_stack()
print("Ссылка на вершину стека:", top_node)
print("Значение вершины стека:", top_node.data)