
class Node:
    '''класс узла односвязного списка'''
    def __init__(self, data=None, next=None):
        '''
        инициализирует узел с данными
        и ссылкой на следующий узел.

        :param data: значение, хранимое в узле
        :param next: ссылка на следующий узел
        '''

        self.data = data
        self.next = next

    def __str__(self):
        '''возвращает строковое представление узла'''
        return str(self.data)


class LinkedList:
    '''класс односвязного линейного списка'''

    def __init__(self):
        '''инициализация односвязного  списка'''
        self.head = None

    def push(self, new_data):
        '''
        добавляет элемент в начало списка

        :param new_data: данные для добавления
        '''

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_begin(self, data):
        '''
        добавляет элемент в начало списка

        :param data: значение элемента
        '''

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_index(self, data, index : int):
        '''
        добавляет элемент на заданную позицию в списке

        :param data: данные для вставки
        :param index: индекс для вставки
        :raises IndexError: если индекс отрицателен или
            выходит за границы списка
        '''

        if index < 0:
            raise IndexError('индекс не может '
                             'быть отрицательным')
        if index == 0:
            self.insert_at_begin(data)
            return

        new_node = Node(data)
        current = self.head
        position = 0

        while current and position < index - 1:
            current = current.next
            position += 1

        if current is None:
            raise IndexError('индекс выходит '
                             'за границы списка')

        new_node.next = current.next
        current.next = new_node

    def insert_at_end(self, data):
        '''
        добавление элемента в конец списка

        :param data: значение элемента
        '''

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def update_node(self, value, index):
        '''
        изменяет значение узла на указанной позиции

        :param value: новое значение узла
        :param index: позиция узла, который необходимо изменить
        :raises IndexError: если индекс отрицателен или
            выходит за границы списка
        '''

        if index < 0:
            raise IndexError('индекс не может '
                             'быть отрицательным')

        current = self.head
        position = 0

        while current and position < index:
            current = current.next
            position += 1

        if current is None:
            raise IndexError('индекс выходит '
                             'за границы списка')

        current._data = value

    def remove_first_node(self):
        '''удаляет первый элемент списка'''

        if self.head is None:
            return
        self.head = self.head.next

    def remove_last_node(self):
        '''удаляет последний элемент списка'''

        if self.head is None:
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def remove_at_index(self, index):
        '''
        удаление элемента по индексу

        :param index: индекс элемента, который будет удален
        :raises IndexError: Если список пуст,
            индекс отрицателен
        или выходит за границы списка.
        '''
        if index < 0:
            raise IndexError('индекс не может '
                             'быть отрицательным')
        if self.head is None:
            raise IndexError('список пуст')
        if index == 0:
            self.remove_first_node()
            return

        current = self.head
        position = 0

        while current and position < index - 1:
            current = current.next
            position += 1

        if current is None or current.next is None:
            raise IndexError('индекс за границами списка')
        current.next = current.next.next

    def remove_node_by_value(self, data):
        '''
        Находит в списке элемент с данным значением
        и удаляет его

        :param data: значение, по которому
            нужно удалить элемент
        '''
        current_node = self.head
        if current_node.data == data:
            self.remove_first_node()
            return
        while (current_node is not None
               and current_node.next.data != data):
            current_node = current_node.next
        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next

    def print_list(self):
        '''выводит в консоль список'''

        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")

node1.next = node2
node2.next = node3
print(node1.next)

d = LinkedList()
d.push(node1)
d.insert_at_begin(node2)

d.print_list()