from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if not container:
        return container

    max_val = max(container)
    count = [0] * (max_val + 1)

    for num in container:
        count[num] += 1

    sorted_container = []
    for num, freq in enumerate(count):
        sorted_container.extend([num] * freq)

    return sorted_container   # TODO реализовать алгоритм сортировки подсчетами



