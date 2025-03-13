class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        prefix = [0] * n

        for x, y in queries:
            prefix[x] -= 1
            if (y+1) < n:
                prefix[y+1] += 1
        summ = 0   
         
        for i in range(n):
            if i == 0:
                if nums[i] <= abs(prefix[i]):
                    nums[i] = 0
                continue
            prefix[i] += prefix[i-1]
            if nums[i] <= abs(prefix[i]):
                nums[i] = 0
        # print(nums, prefix)

        return True if sum(nums) == 0 else False