class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        s = sum(n for n in nums if n % 2 == 0)
        for i in range(len(queries)):
            x, y = queries[i]
            if nums[y] % 2 == 0:
                s -= nums[y]
            nums[y] = nums[y] + x
            if nums[y] % 2 == 0:
                s += nums[y]    
            ans.append(s)

            
        return ans