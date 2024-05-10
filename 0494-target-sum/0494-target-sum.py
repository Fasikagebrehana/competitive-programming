class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        store = {}
        count = 0
        def targets(i, summ):
            nonlocal count
            if i >= len(nums):
                if summ == target:
                    return 1
                return 0
            
            
            if (i, summ) not in store:
                store[(i, summ)] = targets(i+1, summ - nums[i] - nums[i]) + targets(i+1, summ)
            return store[(i, summ)]
        return targets(0, s)