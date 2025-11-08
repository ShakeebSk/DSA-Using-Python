def maze_solver(maze, x, y, visited=None):
    if visited is None:
        visited = set()
    rows, cols = len(maze), len(maze[0])
    if (x < 0 or x >= rows or y < 0 or y >= cols or maze[x][y] == '+' or (x,y) in visited):
        return False
    if maze[x][y] == 'G':
        return [(x,y)]
    visited.add((x,y))
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        path = maze_solver(maze, x+dx, y+dy, visited)
        if path:
            return [(x,y)] + path
    return False

# Test
maze = [
['+','+','+','+','G','+'],
['+',' ','+',' ',' ','+'],
['+',' ',' ',' ','+','+'],
['+',' ','+','+',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+']
]
assert maze_solver(maze, 4, 4)
print("Maze path:", maze_solver(maze, 4, 4))[web:28][web:34][web:40]
