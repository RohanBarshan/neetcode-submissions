class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()

        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
                    
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                neighbors = [[0,1], [1,0], [0,-1], [-1,0]]

                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc

                    if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or 
                        grid[nr][nc] != 1):
                        continue
                    
                    grid[nr][nc] = 2
                    queue.append((nr, nc))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1