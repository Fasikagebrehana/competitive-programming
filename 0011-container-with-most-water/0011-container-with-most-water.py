class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            temp = height[left] if height[left] < height[right] else height[right]
            t = right - left
            r = t * temp
            max_water = max(max_water, r)
            print(max_water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water