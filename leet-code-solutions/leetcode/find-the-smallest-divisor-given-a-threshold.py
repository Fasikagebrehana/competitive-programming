class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        temp = 0
        high, low = max(nums), 1
        def helper(middle):
            div_sum = 0
            for num in nums:
                div_sum += math.ceil(num / middle)
            if div_sum > threshold:
                return False
            return True
        
        while high >= low:
            middle = (high + low) // 2
            if helper(middle):
                high = middle - 1
            else:
                low = middle + 1
        return low