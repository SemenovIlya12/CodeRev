

class Node:
    '''класс узла двусвязного списка'''
    def __init__(self, value=None):
        '''инициализация списка'''
        # значение узла
        self.value = value
        # ссылка на следующий узел
        self.next = None
        # ссылка на предыдущий узел
        self.prev = None


class IntListB:
    '''класс двусвязного списка с барьерным элементом'''
    def __init__(self, aBarrier, aCurrent):
        '''
        инициализация списка

        :param aBarrier: барьерный элемент
        :param aCurrent: текущий элемент
        '''

        # барьерный элемент
        self.barrier = aBarrier
        # текущий элемент
        self.current = aCurrent

    def insert_last(self, data):
        '''
        вставляет элемент в конец списка

        :param data: значение для вставки
        :return:
        '''

        # cоздаём новый узел
        new_node = Node(data)
        # последний элемент перед барьером
        last = self.barrier.prev
        # предыдущий последний элемент указывает на новый
        last.next = new_node
        # новый узел указывает на последний элемент
        new_node.prev = last
        # новый узел указывает на барьер
        new_node.next = self.barrier
        # барьер указывает на новый последний элемент
        self.barrier.prev = new_node
        # новый элемент становится текущим
        self.current = new_node

    def Put(self):
        '''выводит текущий элемент'''
        print(f"Текущий элемент: {self.current.value}")


# создание барьерного элемента
# барьерный элемент имеет произвольное значение (например, 0)
barrier = Node(0)
# Барьер указывает сам на себя
barrier.next = barrier
# Барьер указывает сам на себя
barrier.prev = barrier

# создание текущего элемента,
# который будет равен барьеру в начале
current = barrier

# создание списка с барьером и текущим элементом
dllb = IntListB(barrier, current)

dllb.insert_last(10)
dllb.insert_last(20)
dllb.insert_last(30)
dllb.insert_last(40)
dllb.insert_last(50)

# вывод текущего элемента после вставки всех элементов
dllb.Put()  # 50
