'''Дано число N (> 0) и набор из N чисел.
Создать стек, содержащий исходные числа(последнее число будет вершиной стека),
и вывести ссылку на его вершину.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        """Добавляет элемент в стек."""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def peek(self):
        """Возвращает ссылку на вершину стека (верхний элемент) или None, если стек пуст."""
        return self.top

def create_stack():
    N = int(input("Введите количество чисел (N > 0): "))
    stack = Stack()
    for _ in range(N):
        num = int(input())
        stack.push(num)
    return stack.peek()

top_node = create_stack()
print("Ссылка на вершину стека:", top_node)
print("Значение вершины стека:", top_node.data)