from stack import Stack


def checking_balance_brackets(string: str) -> str:
    """
    Функция проверки сбалансированности скобок.
    Принимает строку со скобками.
    Возращает "Balanced" или "Unbalanced".
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
                return 'Unbalanced'

            top_element = stack.pop()
            # Если типы скобок не совпадают — баланс нарушен
            if pairs[char] != top_element:
                return 'Unbalanced'

    # Если после прохода по всей строке стек не пуст
    # — остались незакрытые скобки
    if not stack.is_empty():
        return 'Unbalanced'

    return 'Balanced'
