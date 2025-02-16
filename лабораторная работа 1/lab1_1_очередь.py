"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):

        """
        Очередь с помощью python list

        Начало очереди - первый элемент списка (индекс 0),
        конец очереди - последний элемент списка.
        TODO Описать где начало и конец очереди
        """
        self._queue = []  # TODO инициализировать список

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self._queue.append(elem)  # TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if not self._queue:
            raise IndexError("Извлечение из пустой очереди невозможно")
        return self._queue.pop(0)
        # TODO реализовать метод dequeue

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Индекс должен быть целочисленным")

        if not 0 <= ind < len(self._queue):
            raise IndexError("Индекс вне границ очереди")

        return self._queue[ind]  # TODO реализовать метод peek

    def clear(self) -> None:
        """ Очистка очереди. """
        self._queue.clear()    # TODO реализовать метод clear

    def __len__(self):
        """ Количество элементов в очереди. """
        return len(self._queue)  # TODO реализовать метод __len__


