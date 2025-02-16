def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if not isinstance(n, int):
        raise TypeError("Факториал вычисляется для целых чисел")
    if n < 0:
        raise ValueError("Факториал вычисляется для неотрицательных чисел")
    if n > 998:
        raise ValueError("Из-за ограничения глубины рекурсии функция вычисляется для чисел в диапазоне от 0 до 998")
    if n == 0:
        return 1
    return factorial_recursive(n-1) * n  # TODO реализовать рекурсивный алгоритм нахождения факториала