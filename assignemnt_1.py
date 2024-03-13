import networkx as nx
import matplotlib.pyplot as plt


city_network = nx.Graph()
city_network.add_nodes_from(['Kyiv', 'Kharkiv', 'Dnipro', 'Lviv', 'Odessa', 'Poltava'])

city_network.add_edges_from([('Kyiv', 'Kharkiv'), ('Kyiv', 'Dnipro'), ('Kyiv', 'Lviv'), ('Kyiv', 'Odessa'),
    ('Kharkiv', 'Dnipro'), ('Dnipro', 'Odessa'), ('Dnipro', 'Lviv'), ('Lviv', 'Odessa'), ('Kyiv', 'Poltava'), 
    ('Kharkiv', 'Poltava'), ('Dnipro', 'Poltava')])

nx.draw(city_network, with_labels=True, node_color='lightblue', node_size=1000, font_size=10, font_weight='bold')
plt.show()

num_nodes = city_network.number_of_nodes()
num_edges = city_network.number_of_edges()
degree_sequence = [degree for node, degree in city_network.degree()]

print("Кількість вершин: ", num_nodes)
print("Кількість ребер: ", num_edges)
print("Ступінь вершин: ", degree_sequence)