# Дан односвязный линейный список и указатель на голову списка P1.
# Необходимовывести указатель на шестой элемент этого списка P6. Известно, что в исходномспискенеменее 6 элементов

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # добавление элемента в начало списка:
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # BCTABKA В ЗАДАННУЮ ПОЗИЦИЮ
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while (current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    # ВСТАВКА B КОНЕЦ СПИСКА
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    # ИЗМЕНЕНИЕ ЗНАЧЕНИЯ УЗЛА В УКАЗАННОЙ ПОЗИЦИИ
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while (current_node != None and position != index):
                position = position + 1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.data = val
            else:
                print("Index not present")

    # УДАЛЕНИЕ УЗЛА — ПЕРВОГО ИЛИ ПОСЛЕДНЕГО
    def remove_first_node(self):
        if (self.head == None):
            return
        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return
        current_node = self.head
        while (current_node.next.next):
            current_node = current_node.next
        current_node.next = None

    ##    УДАЛЕНИЕ УЗЛА ПО ИНДЕКСУ
    def remove_at_index(self, index):
        if self.head == None:
            return
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while (current_node != None and position + l != index):
                position = position + 1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not рrеsеnt")

    # УДАЛЕНИЕ УЗЛА NO ЗНАЧЕНИЮ
    def remove_node(self, data):
        current_node = self.head
        if current_node.data == data:
            self.remove_first_node()
            return
        while (current_node != None and current_node.next.data != data):
            current_node = current_node.next
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

    ##    ОБХОД СПИСКА

    def printLL(self):
        current_node = self.head
        while (current_node):
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
d.insertAtBegin(node2)
d.printLL()