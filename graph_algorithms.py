from typing import Callable
from data_structures import Node, Edge, Queue


def bfs(start: Node, on_visit: Callable[[Node], bool]):
    q: Queue[Node] = Queue()
    q.enqueue(start)
    visited = {}
    finished = False

    while not q.empty() and not finished:
        current_node = q.dequeue()
        for edge in current_node.edges:
            edge.end.action = edge.action
            if f'{edge.end}' not in visited:
                q.enqueue(edge.end)
        if f'{current_node}' not in visited:
            visited[f'{current_node}'] = True
            finished = on_visit(current_node)
