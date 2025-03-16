from collections import deque

def water_jug_bfs(capacity_x, capacity_y, target):
    visited = set()
    queue = deque([(0, 0)])  # Start with both jugs empty
    path = {}
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        if x == target or y == target:
            solution_path = []
            while (x, y) in path:
                solution_path.append((x, y))
                x, y = path[(x, y)] 
            solution_path.append((0, 0))
            return list(reversed(solution_path))
        
        # Possible next states
        states = [
            (capacity_x, y),  # Fill jug X
            (x, capacity_y),  # Fill jug Y
            (0, y),           # Empty jug X
            (x, 0),           # Empty jug Y
            (x - min(x, capacity_y - y), y + min(x, capacity_y - y)),  # Pour X -> Y
            (x + min(y, capacity_x - x), y - min(y, capacity_x - x))   # Pour Y -> X
        ]
        
        for new_state in states:
            if new_state not in visited:
                queue.append(new_state)
                path[new_state] = (x, y)
    
    return None  # No solution found

# Example usage
capacity_x = 3  # Capacity of first jug
capacity_y = 4 # Capacity of second jug
target = 2      # Desired amount

solution = water_jug_bfs(capacity_x, capacity_y, target)
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")
