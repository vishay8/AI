"""
Assignment 3: Breadth-First Search Implementation
"""

def bfs(graph, start, goal):
    visited = set()
    queue = [[start]]
    
    if start == goal:
        return [start]
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in visited:
            neighbors = graph[node]
            
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
                if neighbor == goal:
                    return new_path
            
            visited.add(node)
    
    return None

if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    # Test BFS from node A to node F
    start_node = 'A'
    goal_node = 'F'
    result = bfs(graph, start_node, goal_node)
    
    if result:
        print(f"BFS path from {start_node} to {goal_node}: {' -> '.join(result)}")
    else:
        print(f"No path found from {start_node} to {goal_node}")