import math
import heapq

def heap_dijkstra(G, u):
    """Dijkstra algorithm using binary heap"""

    distances = [math.inf] * G.VerticesCount
    distances[u] = 0
    heap = [(0, u)]
    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in G.Vertices[current_node]:
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances


def array_dijkstra(G, u):
    """Dijkstra algorithm using array"""

    dist = [math.inf] * G.VerticesCount
    dist[u] = 0
    visited = [False] * G.VerticesCount

    for _ in range(G.VerticesCount):
        min_dist = math.inf
        min_index = None
        for i in range(G.VerticesCount):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_index = i

        if min_index is None:
            break

        # Marca el nodo como visitado
        visited[min_index] = True

        # Actualiza las distancias de los nodos adyacentes
        for neighbor, weight in G.Vertices[min_index]:
            if weight > 0 and not visited[neighbor]:
                distance = dist[min_index] + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance

    return dist
