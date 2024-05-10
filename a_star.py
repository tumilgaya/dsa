# Define a graph as an adjacency list with edge costs
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 6, 'E': 8},
    'C': {'F': 7},
    'D': {'G': 9},
    'E': {'G': 7},
    'F': {'G': 4},
    'G': {}
}

# Heuristic function (for simplicity, it's a dictionary that stores heuristic values for each node)
heuristics = {
    'A': 10,
    'B': 7,
    'C': 8,
    'D': 6,
    'E': 4,
    'F': 3,
    'G': 0
}

# Function to perform A* search
def astar(start, goal):
    open_list = [(0, start)]  # Priority queue (cost, node)
    came_from = {}  # Keep track of the parent node for each node
    while open_list:
        open_list.sort()
        current_cost, current_node = open_list.pop(0)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph[current_node].items():
            total_cost = current_cost + cost
            open_list.append((total_cost + heuristics[neighbor], neighbor))
            came_from[neighbor] = current_node

    
    return None  # If no path found

# Example usage
start_node = 'A'
goal_node = 'G'
path = astar(start_node, goal_node)
if path:
    print(f"Path from {start_node} to {goal_node}: {' -> '.join(path)}")
else:
    print("No path found.")
