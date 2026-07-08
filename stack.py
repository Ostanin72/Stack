class Stack:
    """
    Класс Стек.
    """
    def __init__(self):
        self.items = []


    # проверка стека на пустоту. Метод возвращает True или False
    def is_empty(self) -> bool:
        return len(self.items) == 0


    # добавляет новый элемент на вершину стека. Метод ничего не возвращает
    def push(self, item) -> None:
        self.items.append(item)


    # удаляет верхний элемент стека. Стек изменяется.
    # Метод возвращает верхний элемент стека
    def pop(self) -> str:
        return self.items.pop()


    # возвращает верхний элемент стека, но не удаляет его.
    # Стек не меняется
    def peek(self) -> str:
        return self.items[len(self.items) - 1]


    # возвращает количество элементов в стеке
    def size(self) -> int:
        return len(self.items)
