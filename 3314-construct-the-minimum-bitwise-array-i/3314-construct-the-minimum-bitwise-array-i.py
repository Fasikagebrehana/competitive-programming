class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for num in nums:
            found = False
            for i in range(1, num):
                if (i | i+1) == num:
                    ans.append(i)
                    break
            else:
                ans.append(-1)
        return ans