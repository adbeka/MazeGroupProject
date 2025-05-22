# Students: Bekassyl Adenov, Rofig Ashumov
# Dijkstra Maze Solver
# Time Complexity: O((N*M)*log(N*M))
# Space Complexity: O(N*M)

import heapq

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

def dijkstra(maze):
    start, goal = find_positions(maze)
    heap = [(0, 0, start[0], start[1])]
    visited = {}

    while heap:
        steps, coins, r, c = heapq.heappop(heap)
        if (r, c) == goal:
            return coins
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] != 'X':
                new_coins = coins + int(maze[nr][nc]) if maze[nr][nc].isdigit() else coins
                if (nr, nc) not in visited or (steps + 1 < visited[(nr, nc)][0]) or \
                   (steps + 1 == visited[(nr, nc)][0] and new_coins < visited[(nr, nc)][1]):
                    visited[(nr, nc)] = (steps + 1, new_coins)
                    heapq.heappush(heap, (steps + 1, new_coins, nr, nc))
    return None

if __name__ == "__main__":
    maze_files = ["maze_11x11.txt", "maze_31x31.txt", "maze_101x101.txt"]
    results = []
    for f in maze_files:
        maze = read_maze(f)
        results.append(str(dijkstra(maze)))
    print(",".join(results))