# Students: Bekassyl Adenov, Rofig Ashumov
# BFS Maze Solver
# Time Complexity: O(N*M)
# Space Complexity: O(N*M)

from collections import deque

def read_maze(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f]

def find_positions(maze):
    start = goal = None
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'G':
                goal = (i, j)
    return start, goal

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)]

def bfs(maze):
    start, goal = find_positions(maze)
    q = deque()
    q.append((start[0], start[1], 0, 0))
    visited = {}

    while q:
        r, c, steps, coins = q.popleft()
        if (r, c) == goal:
            return coins
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] != 'X':
                new_coins = coins + int(maze[nr][nc]) if maze[nr][nc].isdigit() else coins
                if (nr, nc) not in visited or (steps + 1 < visited[(nr, nc)][0]) or \
                   (steps + 1 == visited[(nr, nc)][0] and new_coins < visited[(nr, nc)][1]):
                    visited[(nr, nc)] = (steps + 1, new_coins)
                    q.append((nr, nc, steps + 1, new_coins))
    return None

if __name__ == "__main__":
    maze_files = ["maze_11x11.txt", "maze_31x31.txt", "maze_101x101.txt"]
    results = []
    for f in maze_files:
        maze = read_maze(f)
        results.append(str(bfs(maze)))
    print(",".join(results))
