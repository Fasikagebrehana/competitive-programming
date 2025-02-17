class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = []
        def backtrack(arr):
            nonlocal ans
            if arr and arr not in ans:
                
                ans.append(arr[:])
                # return
            
            for idx in range(len(tiles)):
                if tiles[idx] not in arr or arr.count(tiles[idx]) < tiles.count(tiles[idx]):
                    arr.append(tiles[idx])
                    backtrack(arr)
                    arr.pop()
        backtrack([])

        return len(ans)