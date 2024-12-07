class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums.sort()
        def checker(middle, op):
            needed = 0
            idx = bisect_right(nums, middle)
            if idx < len(nums):
                for i in range(idx, len(nums)):
                    needed += (math.ceil(nums[i]/middle) - 1)

            if needed > op:
                return False
            return True
        
        left, right = 1, max(nums)
        answer = inf
        while left <= right:
            middle = (left + right) // 2
            if checker(middle, maxOperations):
                answer = min(answer, middle)
                right = middle - 1
            else:
                left = middle + 1
        return answer