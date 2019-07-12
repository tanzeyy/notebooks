import networkx as nx
import random
from utils import PriorityQueue
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
for edge in G.edges():
    G[edge[0]][edge[1]]['weight'] = random.randint(1, 10)

source = 2
goal = 3


ref_nodes = PriorityQueue()
ref_nodes.put(source, 0)
dist_so_far = {}
came_from = {}
dist_so_far[source] = 0

while not ref_nodes.empty():
    current = ref_nodes.get()

    if current == goal:
        break
    
    for next_node in G.neighbors(current):
        new_dist = dist_so_far[current] + G[current][next_node]['weight']
        if next_node not in dist_so_far or new_dist < dist_so_far[next_node]:
            dist_so_far[next_node] = new_dist
            ref_nodes.put(next_node, new_dist)
            came_from[next_node] = current

print(came_from)
print(dist_so_far)
