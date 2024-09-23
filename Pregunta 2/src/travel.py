import math
import heapq
from src.dijkstra import heap_dijkstra, array_dijkstra

def travel(G,U):
    ''' Given a graph and a list of tuples in the format (u,v,l) returns how many util edges the graph contains 
 
        ## Params:
        
        G: Graph
        U: Tuple in form of (u,v,l), where u,v belongs to G and l is the wight of the path between u and v
        
        ## Returns:
        
        int: Number of util edges in the graph
    '''

    dijkstra = None

    # Chose wish Dijkstra algorithm are going to be used
    if G.EdgesCount * math.log(G.VerticesCount) < G.VerticesCount**2:
        dijkstra = heap_dijkstra
    else:
        dijkstra = array_dijkstra

    # Initialize distance
    distance = {}

    # Apply dijkstra for any vertex in U
    for u,v,l in U:
        if distance.get(u) is None:
            distance[u] = dijkstra(G,u)
        if distance.get(v) is None:
            distance[v] = dijkstra(G,v)

    # Find and count the util edges in the graph
    util_edge_count = 0
    for x, y, w in G.Edges:
        for u, v, l in U:
            if (distance[u][x] + distance[v][y] + w <= l or distance[u][y] + distance[v][x] + w <= l):
                util_edge_count += 1
                break
            
    return util_edge_count
