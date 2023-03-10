import json
from typing import Generic, TypeVar
from collections import deque

T = TypeVar('T')


class EmptyCollectionException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.elements: deque[T] = deque([])

    def enqueue(self, element: T) -> None:
        self.elements.appendleft(element)

    def dequeue(self) -> T:
        if self.empty():
            raise EmptyCollectionException("Queue is empty")
        return self.elements.pop()

    def peek(self) -> T:
        if self.empty():
            raise EmptyCollectionException("Queue is empty")
        return self.elements[-1]

    def empty(self) -> bool:
        return len(self.elements) == 0


class Stack(Generic[T]):
    def __init__(self):
        self.elements: list[T] = []

    def pop(self) -> T:
        if self.empty():
            raise EmptyCollectionException("Stack is empty")
        elm = self.elements[-1]
        self.elements = self.elements[:-1]
        return elm

    def push(self, element: T) -> None:
        self.elements.append(element)

    def peek(self) -> T:
        if self.empty():
            raise EmptyCollectionException("Queue is empty")
        return self.elements[-1]

    def empty(self) -> bool:
        return len(self.elements) == 0


class Node(Generic[T]):
    def __init__(self, data: T, edges: list):
        self.action = None
        self.data = data
        self.edges = edges
        if len(edges) == 0:
            self.edges = []

    def add_edge(self, cost, end, action):
        end.action = action
        self.edges.append(Edge(cost=cost, end=end, start=self, action=action))

    def __str__(self):
        return f'data: {self.data}, edges: {self.edges}'


class Edge(Generic[T]):
    def __init__(self, cost, start: Node, end: Node, action):
        self.cost = cost
        if not cost:
            self.cost = 0
        self.start = start
        self.end = end
        self.action = action
