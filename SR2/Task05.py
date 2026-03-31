import gc


class Node:
    '''класс узла с данными'''

    def __init__(self, data):
        '''
        инициализирует узел

        :param data: данные, которые будут храниться в узле
        '''
        # данные узла
        self.data = data
        # ссылка на следующий узел
        self.next = None
        # ссылка на предыдущий узел
        self.prev = None

    def dispose(self):
        '''
        Метод для удаления узла, убирает связи
        и запускает сборщик мусора
        '''

        print(f"Узел с удалёнными данными {self.data}")
        # убираем ссылку на следующий узел
        self.next = None
        # убираем ссылку на предыдущий узел
        self.prev = None
        # принудительно запускаем сборку мусора
        gc.collect()


class DoublyLinkedList:
    '''класс двусвязного списка'''

    def __init__(self):
        '''инициализирует двусвязный список'''
        # ссылка на первый элемент списка
        self.first = None
        # ссылка на последний элемент списка
        self.last = None

    def push(self, new_data):
        '''
        добавляет новый узел с заданным значением
        в начало списка

        :param new_data: значение, хранимое в новом узле
        '''

        # создаем новый узел
        new_node = Node(new_data)
        if self.first is None:
            # первый узел становится и первым, и последним
            self.first = self.last = new_node
        else:
            # у старого последнего узла обновляется next-ссылка
            self.last.next = new_node
            # новый узел ссылается назад на предыдущий
            new_node.prev = self.last
            # новый узел становится последним
            self.last = new_node

    def print_list(self, head, is_circular=False):
        '''
        печатает список в консоль

        :param head: начальный узел списка
        :param is_circular: флаг, является ли список цикличным
        '''

        if head is None:
            print("Empty list")
            return

        temp = head
        first_iteration = True
        while (first_iteration
               or (is_circular and temp != head)):
            first_iteration = False
            print(temp.data, end=" <-> ")
            temp = temp.next
            # обычный список, дошли до конца
            if temp is None and not is_circular:
                break

        print("(circular)" if is_circular else "None")

    def split_into_circular_lists(self):
        '''
        разделяет список на два циклических списка
        и возвращает ссылки на их головы, а также
        на два средних элемента исходного списка.

        :return:кортеж (c1, c2, a3, a4), где:
                c1 — голова первого циклического списка,
                c2 — голова второго циклического списка,
                a3 — первый средний элемент,
                a4 — второй средний элемент.
        '''
        if self.first is None or self.last is None:
            return None, None, None, None

        # используем два указателя для
        # нахождения середины списка
        slow = fast = self.first
        while fast and fast.next:
            # быстрый указатель движется в два раза быстрее
            fast = fast.next.next
            if fast:
                # медленный указатель движется по одному шагу
                slow = slow.next

        # определяем средние элементы
        # первый средний элемент
        a3 = slow
        # второй средний элемент
        a4 = slow.next

        # разделяем список на две половины
        first_half_head = self.first
        first_half_tail = a3

        second_half_head = a4
        second_half_tail = self.last

        # разрываем связи между половинами
        if first_half_tail:
            # Делаем первую половину циклической
            first_half_tail.next = first_half_head
            first_half_head.prev = first_half_tail

        if second_half_tail:
            # Делаем вторую половину циклической
            second_half_tail.next = second_half_head
            second_half_head.prev = second_half_tail

        return first_half_head, second_half_head, a3, a4

    def printLL(self):
        current_node = self.first
        while(current_node):
            print(current_node.data)
            current_node = current_node.next


# пример
# создаем двусвязный список с четным количеством элементов
dll = DoublyLinkedList()
# четное количество элементов (1, 2, 3, 4, 5, 6)
for i in range(1, 7):
    dll.push(i)

print("исходный список:")
dll.print_list(dll.first)
dll.printLL()

# разделяем на два циклических списка
C1, C2, A3, A4 = dll.split_into_circular_lists()

print("первый циклический список:")
dll.print_list(C1, is_circular=True)
print("второй циклический список:")
dll.print_list(C2, is_circular=True)

print("средние элементы исходного списка:")
print("A3:", A3.data if A3 else "null")
print("A4:", A4.data if A4 else "null")