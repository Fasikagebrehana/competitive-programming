class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i, len(nums)):
                n = i * j
                if i<j and nums[i] == nums[j] and n % k == 0:
                    count += 1
        return count