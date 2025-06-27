class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
        def inbound(r, c):
            return 0 <= r < len(image) and 0 <= c < len(image[0])
        changed = []
        visited = set()
        def dfs(r, c):

            for x, y in directions:
                newRow, newCol = x + r, y + c
                if inbound(newRow, newCol) and (newRow, newCol) not in visited and image[newRow][newCol] == image[r][c]:
                    visited.add((newRow, newCol))
                    changed.append((newRow, newCol))
                    dfs(newRow, newCol)
        dfs(sr, sc)
        # print(changed)
        image[sr][sc] = color
        for x, y in changed:
            image[x][y] = color
        # print(image)


        return image