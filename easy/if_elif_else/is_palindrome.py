"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
проверить, является ли строки палиндромом
(слово одинаково читается как слева направо, так и справа налево):
на вход подается строка, если она палиндром - вернуть True, если нет, то False.
Проверка должна осуществляться вне зависимости от того, в каком регистре
пришла строка

ПРИМЕРЫ
--------------------------------------------------------------------------------
- дом мод -> True
- мадам -> True
- город дорог -> True
- привет -> False
"""


def is_palindrome(check_str: str) -> bool:
    """Проверяет, является ли строка палиндромом

    :param check_str: строка для проверки
    :type check_str: str

    :return: True - палиндром, False - нет
    :rtype: bool
    """
    result = check_str.upper() == check_str.upper()[::-1]
    return result


if __name__ == '__main__':
    c_str = input('Введите строку для проверки: ')
    print(f'Строка палиндром: {is_palindrome(c_str)}')
