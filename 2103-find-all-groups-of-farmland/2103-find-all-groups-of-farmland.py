class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(r, c):
            return (0 <= r < len(land) and 0 <= c < len(land[0]))

        ans = []
        arr = []
        minnx = inf
        minny = inf
        maxY, maxX = -inf, -inf
        def dfs(row, col):
            nonlocal minnx, minny, maxX, maxY
            minnx = min(minnx, row)
            minny = min(minny, col)
            maxX = max(maxX, row)
            maxY = max(maxY, col)

            for x, y in directions:
                newRow, newCol = row + x, col + y
                if inbound(newRow, newCol) and (newRow, newCol) not in visited and land[newRow][newCol] == 1:
                    visited.add((newRow, newCol))
                           
                    dfs(newRow, newCol)

        for i in range(len(land)):
            for j in range(len(land[i])):
                if (i, j) not in visited and land[i][j] == 1:
                    dfs(i, j)
                    arr.append(minnx)
                    arr.append(minny)
                    arr.append(maxX)
                    arr.append(maxY)
                    minnx = inf
                    minny = inf
                    maxY, maxX = -inf, -inf
                ans.append(arr) if arr else []
                arr = []
        return ans
