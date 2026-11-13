class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        fresh_count = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        minutes = 0
        while q and fresh_count > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(1,0), (0,1), (0,-1), (-1,0)]:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        q.append((nr,nc))

            minutes += 1
        return minutes if fresh_count == 0 else -1
                    






