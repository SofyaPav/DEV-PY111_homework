from typing import Union
import networkx as nx  # pip install networkx


def build_graph(stairway: tuple) -> nx.DiGraph:
    """
    Создает граф лестницы, где узлы — это ступени, а рёбра (дуги) — возможные шаги с соответствующей стоимостью.

    :param stairway: Кортеж с ценами за каждую ступень.
    :return: Взвешенный ориентированный граф NetworkX.
    """
    graph = nx.DiGraph()
    num_steps = len(stairway)

    for i in range(num_steps):
        if i + 1 < num_steps:
            graph.add_edge(i, i + 1, weight=stairway[i + 1])
        if i + 2 < num_steps:
            graph.add_edge(i, i + 2, weight=stairway[i + 2])

    return graph


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитывает минимальную стоимость подъема на верхнюю ступень.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимость кратчайшего пути.
    :return: Минимальная стоимость подъема на верхнюю ступень.
    """
    start, end = 0, max(graph.nodes)
    return nx.shortest_path_length(graph, source=start, target=end, weight="weight")


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = build_graph(stairway)
    print(stairway_path(stairway_graph))
