from typing import Any

class Stack:
    def __init__(self):

        self._stack = []

    def push(self, elem: Any) -> None:
        """
        Добавление элемента в вершину стека
        """
        self._stack.append(elem)

    def pop(self) -> Any:
        """
        Извлечение элемента из вершины стека
        :raise: IndexError - Ошибка, если стек пуст
        :return: Извлеченный элемент
        """
        if not self._stack:
            raise IndexError("Извлечение из пустого стека невозможно")
        return self._stack.pop()

    def __len__(self):
        """Количество элементов в стеке"""
        return len(self._stack)


def check_brackets(brackets_row: str) -> bool:
    """
    Проверка, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """

    st = Stack()


    for char in brackets_row:
        if char == '(':
            st.push(char)
        elif char == ')':
            if len(st) == 0:
                return False
            st.pop()

    return len(st) == 0# TODO реализовать проверку скобочной группы


