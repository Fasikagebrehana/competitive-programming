class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        l, r = 0, len(nums)-1
        while l < r:
            if (nums[l] + nums[r]) == k:
                count += 1
                l += 1
                r -= 1
            elif (nums[l] + nums[r]) < k:
                l += 1
            else:
                r -= 1
        return count