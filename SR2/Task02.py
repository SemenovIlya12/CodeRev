"""Дан набор из 10 чисел. Создать очередь, содержащую данные числа в
указанном порядке (первое число будет размещаться в  начале очереди,
последнее — в конце), и вывести ссылки A1 и A2 на начало и конец очереди."""


class Node:
    """Класс узла очереди"""

    def __init__(self, data):
        self.data = data  # Значение узла
        self.next = None  # Ссылка на следующий узел


class Queue:
    """Класс динамической очереди"""

    def __init__(self):
        self.front = None  # Начало очереди (A1)
        self.rear = None  # Конец очереди (A2)

    def IsEmpty(self):
        """Проверка, пустая ли очередь"""
        return self.front is None

    def Enqueue(self, value):
        """Добавление элемента в конец очереди"""
        new_node = Node(value)
        if self.IsEmpty():
            self.front = self.rear = new_node  # Если очередь была пустой
        else:
            self.rear.next = new_node  # Привязываем новый узел к последнему
            self.rear = new_node  # Обновляем конец очереди

    def Dequeue(self):
        """Удаление элемента из начала очереди"""
        if self.IsEmpty():
            raise IndexError("Очередь пуста")

        value = self.front.data
        self.front = self.front.next  # Смещаем начало очереди

        if self.front is None:  # Если очередь стала пустой
            self.rear = None

        return value

    def Front(self):
        """Возвращает первый элемент очереди без удаления"""
        if self.IsEmpty():
            raise IndexError("Очередь пуста")
        return self.front.data

    def Rear(self):
        """Возвращает последний элемент очереди без удаления"""
        if self.IsEmpty():
            raise IndexError("Очередь пуста")
        return self.rear.data

    def PrintQueue(self):
        """Вывод очереди (от начала к концу)"""
        current = self.front
        print("Очередь (начало -> конец):", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def PrintQueueVisual(self):
        """Красивый вывод очереди в виде стрелочек"""
        current = self.front
        if self.IsEmpty():
            print("Очередь пуста!")
            return
        output = []
        while current:
            output.append(f"[{current.data}]")
            current = current.next
        print(" → ".join(output))


# === ОСНОВНОЙ КОД ===
queue = Queue()

# Ввод 10 чисел от пользователя
numbers = list(map(int, input("Введите 10 чисел через пробел: ").split()))

# Добавляем числа в очередь
for num in numbers:
    queue.Enqueue(num)

# Вывод результатов
queue.PrintQueueVisual()
print(f"Ссылка на начало (A1): {queue.front} (значение: {queue.Front()})")
print(f"Ссылка на конец (A2): {queue.rear} (значение: {queue.Rear()})")