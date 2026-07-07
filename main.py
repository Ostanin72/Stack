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


def checking_balance_brackets(string: str) -> str:
    """
    Функция проверки сбалансированности скобок.
    Принимает строку со скобками.
    Возращает "Сбалансированно" или "Несбалансированно".
    """

    opening_brackets = "([{"
    closing_brackets = ")]}"
    # Словарь для сопоставления парных скобок
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = Stack()

    for char in string:
        # Добавляем в стек открывающие скобки
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            # Если встретилась закрывающая скобка, а стек пуст — баланс нарушен
            if stack.is_empty():
                return "Несбалансированно"

            top_element = stack.pop()
            # Если типы скобок не совпадают — баланс нарушен
            if pairs[char] != top_element:
                return "Несбалансированно"

    # Если после прохода по всей строке стек не пуст
    # — остались незакрытые скобки
    if not stack.is_empty():
        return "Несбалансированно"

    return "Сбалансированно"

if __name__ == '__main__':
    test_strings = [
        '(((([{}]))))',
        '[([])((([[[]]])))]{()}',
        '{{[()]}}',
        '}{}',
        '{{[(])]}}',
        '[[{())}]'
    ]

    for s in test_strings:
        result = checking_balance_brackets(s)
        print(f"'{s}' -> {result}\n")
