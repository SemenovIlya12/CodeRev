"""
Даны ссылки A1 и A2 на первый и последний элементы непустого двусвязного списка, содержащего четное количество элементов.
 Преобразовать список в два циклических списка ( записав в свойство Next последнего элемента списка ссылку на его первый
 элемент, а в свойство Prev первого элемента — ссылку на последний элемент.), первый из которых содержит первую половину элементов
 исходного списка, а второй —вторую половину. Вывести ссылки A3 и A4 на два средних элемента исходного списка (элемент A3
  должен входить в первый циклический список, а элемент A4 — во второй). Новые объекты типа Node не создавать.
"""

import gc


class Node:
    """Класс узла двусвязного списка"""

    def __init__(self, data):
        self.data = data  # Данные узла
        self.next = None  # Ссылка на следующий узел
        self.prev = None  # Ссылка на предыдущий узел

    def Dispose(self):
        """Метод для удаления узла: очищает связи и вызывает сборщик мусора"""
        print(f"Узел с удалёнными данными {self.data}")
        self.next = None  # Убираем ссылку на следующий узел
        self.prev = None  # Убираем ссылку на предыдущий узел
        gc.collect()  # Принудительно запускаем сборку мусора


class DoublyLinkedList:
    """Класс двусвязного списка"""

    def __init__(self):
        self.first = None  # Ссылка на первый элемент списка
        self.last = None  # Ссылка на последний элемент списка

    def push(self, new_data):
        """Добавляет новый узел в конец списка"""
        new_node = Node(new_data)  # Создаем новый узел
        if self.first is None:
            self.first = self.last = new_node  # Первый узел становится и первым, и последним
        else:
            self.last.next = new_node  # У старого последнего узла обновляется next-ссылка
            new_node.prev = self.last  # Новый узел ссылается назад на предыдущий
            self.last = new_node  # Новый узел становится последним

    def print_list(self, head, is_circular=False):
        """Выводит список в консоль, поддерживает как обычный, так и циклический вывод"""
        if head is None:
            print("Empty list")
            return

        temp = head
        first_iteration = True
        while first_iteration or (is_circular and temp != head):
            first_iteration = False
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp is None and not is_circular:  # Обычный список, дошли до конца
                break

        print("(circular)" if is_circular else "None")

    def split_into_circular_lists(self):
        """Разделяет список на два циклических списка и находит средние элементы"""
        if self.first is None or self.last is None:
            return None, None, None, None

        # Используем два указателя для нахождения середины списка
        slow = fast = self.first
        while fast and fast.next:
            fast = fast.next.next  # Быстрый указатель движется в два раза быстрее
            if fast:
                slow = slow.next  # Медленный указатель движется по одному шагу

        # Определяем средние элементы
        A3 = slow  # Первый средний элемент
        A4 = slow.next  # Второй средний элемент

        # Разделяем список на две половины
        first_half_head = self.first
        first_half_tail = A3

        second_half_head = A4
        second_half_tail = self.last

        # Разрываем связи между половинами
        if first_half_tail:
            first_half_tail.next = first_half_head  # Делаем первую половину циклической
            first_half_head.prev = first_half_tail

        if second_half_tail:
            second_half_tail.next = second_half_head  # Делаем вторую половину циклической
            second_half_head.prev = second_half_tail

        return first_half_head, second_half_head, A3, A4

    def printLL(self):
        current_node = self.first
        while(current_node):
            print(current_node.data)
            current_node = current_node.next


# Пример

# Создаем двусвязный список с четным количеством элементов
dll = DoublyLinkedList()
for i in range(1, 7):  # Четное количество элементов (1, 2, 3, 4, 5, 6)
    dll.push(i)

print("Исходный список:")
dll.print_list(dll.first)
dll.printLL()

# Разделяем на два циклических списка
C1, C2, A3, A4 = dll.split_into_circular_lists()

print("Первый циклический список:")
dll.print_list(C1, is_circular=True)
print("Второй циклический список:")
dll.print_list(C2, is_circular=True)

print("Средние элементы исходного списка:")
print("A3:", A3.data if A3 else "null")
print("A4:", A4.data if A4 else "null")