class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = nums[i] + prefix[i-1]
        summ = sum(nums)
        if summ % p == 0:
            return 0
        if summ < p: 
            return -1
        ans = inf
        dic = {}
        dic[summ % p] = 0
        mod = summ % p
        for i in range(len(prefix)):
            pr = prefix[i] % p
            if pr in dic:
                ans = min(ans, ((i+1) - dic[pr]))
            temp = (mod + pr) % p
            dic[temp] = (i+1)
        if ans == len(nums):
            return -1
        return ans if ans != inf else -1