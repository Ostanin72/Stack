from utils import checking_balance_brackets

allowed_chars = {'(', ')', '{', '}', '[', ']'}

while True:
    string = input('Введите строку скобок: ')

    # Убеждаемся, что строка не пустая и состоит из скобок
    if not string:
        print('Ошибка: Вы не ввели стрoку\n')
    elif not set(string).issubset(allowed_chars):
        print('Ошибка: Строка должна содержать только символы (), {}, [].\n')
    else:
        break


if __name__ == '__main__':
    result = checking_balance_brackets(string)
    print(result)
