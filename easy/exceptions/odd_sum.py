"""
Написать функцию odd_sum, которая принимает список, который может состоять
из различных элементов.
Если все элементы списка целые числа, то функция должна посчитать сумму
нечетных чисел.
Если хотя бы один элемент не является целым числом, то выкинуть ошибку
TypeError с сообщением "Все элементы списка должны быть целыми числами"
Задачу стоит выполнить с помощью одного цикла

Написать блок if __name__ == '__main__', в котором
нужно описать обработку исключения try-except-else-finally
"""


def odd_sum(int_list: list) -> int:
    result = 0
    for val in int_list:
        if isinstance(val, int) and not isinstance(val, bool):
            result += val
        else:
            raise TypeError("Все элементы списка должны быть целыми числами")
    return result


if __name__ == '__main__':
    try:
        print(odd_sum([1, 2, 3, 4, 5, 6, 8, 9, 10]))
        print(odd_sum([1, True, 2, -1, "fff", 4, 6, [], (), -8]))
    except TypeError as e:
        print(e)
    else:
        print("Все прошло хорошо.")
    finally:
        print("Выполнение закончено.")