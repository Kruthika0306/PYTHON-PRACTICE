import heapq

def prims_algorithm(graph, start):
    """
    graph: adjacency list representation
           { node: [(weight, neighbor), ...] }
    start: starting node
    """

    visited = set()
    min_heap = [(0, start)]  # (weight, node)
    total_cost = 0
    mst = []

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_cost += weight

        if weight != 0:
            mst.append((node, weight))

        for edge_weight, neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor))

    return total_cost, mst


# Example graph
graph = {
    'A': [(2, 'B'), (3, 'C')],
    'B': [(2, 'A'), (1, 'C'), (4, 'D')],
    'C': [(3, 'A'), (1, 'B'), (5, 'D')],
    'D': [(4, 'B'), (5, 'C')]
}

# Run Prim's Algorithm
cost, mst = prims_algorithm(graph, 'A')

print("Minimum Cost:", cost)
print("Edges in MST:")
for edge in mst:
    print(edge)