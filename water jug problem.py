# DT : 1/10/26
# EXP 8 : WATER JUG PROBLEM.

from collections import deque

# Function to solve water jug problem using DFS
def water_jug(capacity1, capacity2, target):
    visited = set()
    queue = deque()
    
    # Initial state: both jugs are empty
    queue.append((0, 0, []))

    while queue:
        jug1, jug2, path = queue.popleft()

        # Skip if the state has already been visited
        if (jug1,jug2) in visited:
            continue
        visited.add((jug1,jug2))

        # Add current state to the path
        path = path + [ ( jug1 , jug2 ) ]

        # Check if target is reached
        if jug1 == target or jug2 == target:
            return path
        # Generate all possible next states
        next_states = [
            # fill jug 1
            (capacity1 , jug2),
            # fill jug 2
            (jug1,capacity2),
            # empty jug1
            (0,jug2),
            # empty jug2
            (jug1,0),
            # pour jug1 -> jug2
            (
                jug1 - min(jug1,capacity2 - jug2),
                jug2 + min(jug1, capacity2 - jug2)
            )
            ]
        # Add unvisited states to the queue
        for state in next_states:
            if state not in visited :
                queue.append((state[0],state[1],path))

        # NO solution found
    return None

# MAin program
jug1 = int(input(" Enter capacity of jug1: "))
jug2 = int(input("Enter capactiy of jug2: "))
target = int(input("Enter target amount: "))
solution = water_jug(jug1,jug2,target)
if solution:
    print("\n steps to reach the target.")
    for step in solution:
        print(step)
else:
    print("No solution exists.")
