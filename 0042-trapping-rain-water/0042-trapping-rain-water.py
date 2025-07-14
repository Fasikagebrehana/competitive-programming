class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # what can we store at height[i] so we check the left side and then the right side 
        answer = 0
        if n == 1:
            return 0
        
        left, right = 0, n-1
        left_max = height[left]
        right_max = height[right]

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                answer += left_max - height[left]
            else:
                right -= 1
                right_max = max(height[right], right_max)
                answer += right_max - height[right]

        return answer