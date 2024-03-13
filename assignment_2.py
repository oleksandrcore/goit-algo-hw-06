import networkx as nx


city_network = nx.Graph()
city_network.add_nodes_from(['Kyiv', 'Kharkiv', 'Dnipro', 'Lviv', 'Odessa', 'Poltava'])

city_network.add_edges_from([('Kyiv', 'Kharkiv'), ('Kyiv', 'Dnipro'), ('Kyiv', 'Lviv'), ('Kyiv', 'Odessa'),
    ('Kharkiv', 'Dnipro'), ('Dnipro', 'Odessa'), ('Dnipro', 'Lviv'), ('Lviv', 'Odessa'), ('Kyiv', 'Poltava'), 
    ('Kharkiv', 'Poltava'), ('Dnipro', 'Poltava')])

dfs_path = list(nx.dfs_edges(city_network, source="Poltava"))
bfs_path = list(nx.bfs_edges(city_network, source="Poltava"))

if dfs_path == bfs_path:
    print("Шляхи DFS і BFS однакові")
else:
    print("Шляхи DFS і BFS відрізняються")

print("Шлях DFS:", dfs_path)
print("Шлях BFS:", bfs_path)