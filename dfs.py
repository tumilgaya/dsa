graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = set()
def dfs(node):
    if node not in visited:
        print(node , end='')
        visited.add(node)
        for child in graph[node]:
            dfs(child)




dfs("A")