"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if arr == []:
        raise ValueError("Последовательности не должна быть пустой ")
    min_ind = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_ind]:
            min_ind = i
    return min_ind
  # TODO реализовать итеративный линейный поиск