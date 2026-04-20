class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_distance = 0
        for i in range(len(colors)):
            for j in range(i+1, len(colors)):
                if colors[i] != colors[j]:
                    max_distance = max(max_distance, j - i)
        
        return max_distance