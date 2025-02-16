
# 3.	Назовем связным такой граф, в котором есть путь от любой вершины к любой другой вершине.
# Дан граф, состоящий из 2+ связных подграфов, которые не связаны между собой.
# Задача: посчитать число компонент связности графа, т.е. количество таких подграфов.
# A-B-C-D
# F-G
# E
# В графе на картинке – три подграфа, т.е. число компонент связности = 3.

from typing import Hashable
from collections import deque
import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable,  visited: set):
    """
    Функция выполняет обход в ширину, посещает все узлы в текущей компоненте, изменяет множество visited.

    :param g: Граф NetworkX
    :param start_node: Стартовый узел, откуда нужно начать обход
    :param visited: Множество посещённых узлов, которое будет изменяться
    :return: None
    """
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        current_node = queue.popleft()
        for neighbor in g[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def fun(g: nx.Graph) -> int:
    """
    Функция подсчитывает количество компонент (количество подграфов) в неориентированном графе.

    :param g: Граф NetworkX
    :return: Количество компонент связности
    """
    visited = set()
    count = 0


    for node in g.nodes:
        if node not in visited:
            bfs(g, node, visited)
            count += 1

    return count


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_edges_from([
        ('A', 'B'),
        ('B', 'C'),
        ('C', 'D'),
        ('F', 'G'),
    ])

    print(f"Число компонент связности графа (количество подграфов) {fun(graph)}")  # 3
