class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        sorted_height = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != sorted_height[i]:
                ans += 1

        return ans