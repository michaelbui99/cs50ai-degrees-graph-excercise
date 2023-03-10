from data_reader import DataReader
from data_structures import Node, Queue
from graph_algorithms import bfs
from sys import argv


def create_edges(data: DataReader, node: Node, visited: dict) -> Node:
    """
    Recursively adds an edge from node to every star that is directly connected to node through a movie 
    """
    # Base case
    if f'{node.data}' in visited:
        return

    visited[f'{node.data}'] = True

    # Get all movies that the person has been starred in
    rows = data.stars.query(f'person_id == {node.data}')
    movies = rows['movie_id'].values

    # Add an edge to all other persons starred in that movie if not already connected
    for movie in movies:
        rows = data.stars.query(f'movie_id == {movie}')
        persons_in_movie = rows['person_id'].values
        for person in persons_in_movie:
            if person not in visited:
                node.add_edge(cost=0, end=Node(person, []), action=movie)
                visited[f'{person}'] = True

    for edge in node.edges:
        create_edges(data=data, node=edge.end, visited=visited)


def create_graph(data: DataReader, source_id: int) -> Node:
    """
    Creates a graph from source to every other star that the source is connected to both directly and indirectly
    """
    visited = {}
    start_node = Node(source_id, [])
    create_edges(data, start_node, visited)
    return start_node


def do_bfs(start: Node, destination: int) -> tuple[int, Queue[int]]:
    hit = -1
    movies_map = {}
    movies_queue = Queue()

    def visit(node: Node) -> bool:
        nonlocal movies_map
        nonlocal hit
        nonlocal movies_queue

        if node.action and node.action not in movies_map:
            movies_map[node.action] = node.action
            movies_queue.enqueue(node.action)

        if int(node.data) == int(destination):
            hit = len(movies_map)
            return True
        return False

    bfs(start=start, on_visit=lambda node: visit(node))

    return hit, movies_queue


def main():
    # Loads dataset
    data = DataReader('large')

    # Source is 1. argument passed, desitnation is 2. argument passed
    source = argv[1]
    source_name = data.people.query(f'id == {source}')["name"].values[0]
    destination = argv[2]
    destination_name = data.people.query(f'id == {destination}')[
        "name"].values[0]

    # Create the graph with the source as entry
    start_node = create_graph(data, source)

    degrees, actions = do_bfs(start=start_node, destination=destination)

    if (degrees == -1):
        print("No connection found")
    else:
        print(
            f'{source_name} is connected to {destination_name} within {degrees} steps')
        print(f'Movie connection followed: ')
        while (not actions.empty()):
            action = actions.dequeue()
            movie_name = data.movies.query(f'id == {action}')[
                'title'].values[0]
            print(movie_name)


main()
