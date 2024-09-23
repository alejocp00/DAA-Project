import random
from src.graph import Graph

def generate():

    # Generate a random amount of vertices from 10 to 1000
    n = random.randint(10, 300)
    w_mu = 10
    w_sigma = 5
    l_mu = 6
    l_sigma = 2

    # Initialize edges dict
    edges = {}

    # Creating a main path and give randomness to it
    nodes = [i for i in range(n)]
    random.shuffle(nodes)

    # Generate a random amount of edges from 1 to n*(n-1)//2
    m = random.randint(n - 1, n * (n - 1) // 2 + 1)

    # Connecting the nodes of the main path and give randomness to the weights
    for i in range(n - 1):
        x = nodes[i]
        y = nodes[i + 1]
        if x > y:
            x, y = y, x
        w = max(int(random.gauss(w_mu, w_sigma)), 0)
        edges[(x, y)] = w

    # Connecting to the graph the remaining edges and give randomness to the weights
    for _ in range(m - (n - 1)):
        while True:
            x = random.choice(nodes)
            y = random.choice(nodes)
            if x > y:
                x, y = y, x
            if x != y and (x, y) not in edges:
                edges[(x, y)] = max(int(random.gauss(w_mu, w_sigma)), 0)
                break

    # Selecting random q pairs of nodes for poblate U
    U = []
    q = random.randint(0,m // 2)
    for _ in range(q):
        u = random.choice(nodes)
        v = random.choice(nodes)
        l = max(0, int(random.gauss(l_mu, l_sigma)))
        U.append((u, v, l))

    transformed_edges = [(x, y, edges[(x, y)]) for x, y in edges]

    return Graph(n, transformed_edges), U
