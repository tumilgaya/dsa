graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(queue):

    if not queue:
        return

    node = queue.pop(0)
    if node not in visited:
        print(node , end=' ')
        visited.add(node)
        for child in graph[node]:
            queue.append(child)
    bfs(queue)


visited = set()
queue = ['A']
bfs(queue)