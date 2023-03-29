import collections

def numIslands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    islands = 0
    visit = set()

    def bfs(r, c):
        q = collections.deque()
        q.append((r, c))
        visit.add((r, c))

        while q:
            row, col = q.popleft()
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for nr, nc in directions:
                r, c = row + nr, col + nc
                if (r in range(rows) and c in range(cols) 
                    and (r, c) not in visit and grid[r][c] == "1"):
                    q.append((r, c))
                    visit.add((r, c))


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visit:
                bfs(r, c)
                islands += 1
    return islands



print(numIslands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
])) # 1
print(numIslands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
])) # 3
