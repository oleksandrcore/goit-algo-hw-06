import networkx as nx


def print_table(distances, visited):
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)

    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)

        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\n")

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.nodes()}
    distances[start] = 0
    unvisited = list(graph.nodes())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)

        # Вивід таблиці після кожного кроку
        print_table(distances, visited)

    return distances

city_network = nx.Graph()
city_network.add_nodes_from(['Kyiv', 'Kharkiv', 'Dnipro', 'Lviv', 'Odessa', 'Poltava'])

city_network.add_weighted_edges_from([('Kyiv', 'Kharkiv', 520), ('Kyiv', 'Dnipro', 480), ('Kyiv', 'Lviv', 550), ('Kyiv', 'Odessa', 490),
    ('Kharkiv', 'Dnipro', 220), ('Dnipro', 'Odessa', 480), ('Dnipro', 'Lviv', 950), ('Lviv', 'Odessa', 800), ('Kyiv', 'Poltava', 350), 
    ('Kharkiv', 'Poltava',150), ('Dnipro', 'Poltava', 200)])


distances = dijkstra(city_network, 'Poltava')