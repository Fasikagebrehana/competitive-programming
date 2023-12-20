class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        countOne = nums.count(1)
        ans.append(countOne)
        
        count_one = 0
        count_one_left = 0
        count_zero = 0
        for i in range(n):
            if nums[i] == 0:
                count_zero += 1
                
            else:
                count_one_left += 1
                
            count_one = countOne - count_one_left
            ans.append(count_zero + count_one)
        res = []
        m = max(ans)
        for i in range(len(ans)):
            if ans[i] == m:
                res.append(i)
        return res