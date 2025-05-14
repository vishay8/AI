"""
Assignment 2: Water Jug Problem
Two jugs with capacities 4L and 3L, no markings.
Goal: Measure exactly 2L using these jugs.
"""

def water_jug_problem():
    # Track visited states to avoid cycles
    visited = set()
    # Queue for BFS
    queue = [(0, 0, [])]
    
    while queue:
        jug1, jug2, path = queue.pop(0)
        
        if jug1 == 2 or jug2 == 2:
            print("Solution found!")
            for step in path:
                print(step)
            print(f"Final state: ({jug1}, {jug2})")
            return
        
        if (jug1, jug2) in visited:
            continue
        
        visited.add((jug1, jug2))
        
        # Try all possible actions
        actions = [
            (4, jug2, path + [f"Fill 4L jug: ({4}, {jug2})"]),
            (jug1, 3, path + [f"Fill 3L jug: ({jug1}, {3})"]),
            (0, jug2, path + [f"Empty 4L jug: ({0}, {jug2})"]),
            (jug1, 0, path + [f"Empty 3L jug: ({jug1}, {0})"]),
        ]
        
        # Pour from 4L to 3L
        amount = min(jug1, 3 - jug2)
        actions.append((jug1 - amount, jug2 + amount, 
                      path + [f"Pour 4L to 3L: ({jug1 - amount}, {jug2 + amount})"]))
        
        # Pour from 3L to 4L
        amount = min(jug2, 4 - jug1)
        actions.append((jug1 + amount, jug2 - amount, 
                      path + [f"Pour 3L to 4L: ({jug1 + amount}, {jug2 - amount})"]))
        
        queue.extend([(j1, j2, p) for j1, j2, p in actions if (j1, j2) not in visited])
    
    print("No solution found")

if __name__ == "__main__":
    water_jug_problem()