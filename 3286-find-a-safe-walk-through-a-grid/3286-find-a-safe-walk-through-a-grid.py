class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inbounds(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        best = [[-1] * len(grid[0]) for _ in range(len(grid))]

        queue = deque([(0, 0, health)]) if grid[0][0] == 0 else deque([(0, 0, health-1)])
        
        best[0][0] = health - grid[0][0]

        while queue:
            r, c, curr_health = queue.popleft()
            if (r, c) == (len(grid)-1, len(grid[0])-1):
                if curr_health >= 1:
                    return True
                else:
                    return False
            for x, y in directions:
                nr, nc = r + x, c +y
                if inbounds(nr, nc):
                    if grid[nr][nc] == 1:
                        if (curr_health - 1) <=0:
                            continue
                    if (curr_health - grid[nr][nc]) > best[nr][nc]:
                        queue.append((nr, nc, (curr_health - grid[nr][nc])))
                        best[nr][nc] = (curr_health - grid[nr][nc])

        return False