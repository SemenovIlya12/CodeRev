
class Node:
    '''класс, представляющий узел очереди'''

    def __init__(self, data):
        '''
        Инициализирует узел очереди

        :param data: данные, которые будут храниться
            в узле очереди
        '''

        # значение узла
        self.data = data
        # ссылка на следующий узел
        self.next = None


class Queue:
    '''класс, представляющий динамическую очередь'''

    def __init__(self):
        '''инициализация динамической очереди'''

        # начало очереди (A1)
        self.front = None
        # конец очереди (A2)
        self.rear = None

    def is_empty(self):
        '''
        проверяет, пуста ли очередь

        :return: True если очередь пуста, иначе - False
        :rtype: bool
        '''

        return self.front is None

    def enqueue(self, value):
        '''
        добавление элемента в конец очереди

        :param value: значение элемента,
            который будет добавлен в очередь
        :return:
        '''

        new_node = Node(value)
        if self.is_empty():
            # если очередь была пустой
            self.front = self.rear = new_node
        else:
            # привязываем новый узел к последнему
            self.rear.next = new_node
            # обновляем конец очереди
            self.rear = new_node

    def dequeue(self):
        '''
        удаляет элемент из начала очереди
        и возращает его знаение

        :return: значение удаленного элемента
        :raises IndexError: если очередь пуста
        '''

        if self.is_empty():
            raise IndexError("Очередь пуста")

        value = self.front.data
        # смещаем начало очереди
        self.front = self.front.next

        # если очередь стала пустой
        if self.front is None:
            self.rear = None

        return value

    def front(self):
        '''
        возвращает первый элемент очереди без удаления

        :return: первый элемент очереди
        :raises IndexError: если очередь пуста
        '''

        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.front.data

    def rear(self):
        '''
        возвращает последний элемент очереди без удаления

        :return: последний элемент очереди
        :raises IndexError: если очередь пуста
        '''

        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.rear.data

    def print_queue(self):
        '''
        вывод очереди (от начала к концу)

        :return:
        '''
        current = self.front
        print("очередь (начало -> конец):", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def print_queue_visual(self):
        '''
        красивый вывод очереди с стрелочками :)

        :return:
        '''

        current = self.front
        if self.is_empty():
            print("очередь пуста!")
            return
        output = []
        while current:
            output.append(f"[{current.data}]")
            current = current.next
        print(" → ".join(output))

# основной код
queue = Queue()

# ввод 10 чисел от пользователя
numbers = list(map(int,
                   input("введите 10 чисел через пробел: ")
                   .split()
                   ))

# добавляем числа в очередь
for num in numbers:
    queue.enqueue(num)

# вывод результатов
queue.print_queue_visual()

print(f"ссылка на начало (A1): {queue.front} "
      f"(значение: {queue.front()})")

print(f"ссылка на конец (A2): {queue.rear} "
      f"(значение: {queue.rear()})")