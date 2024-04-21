class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            d = heights[i+1] - heights[i]
            if d <= 0:
                continue
            heappush(heap, -d)
            bricks -= d
            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                bricks += -(heappop(heap))
        
        return len(heights) - 1