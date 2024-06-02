class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = [-1] * len(nums)
        median = nums[len(nums) // 2]
        less = []
        for i in range(len(nums) // 2):
            less.append(nums[i])
        greater = []
        for i in range(len(nums) // 2, len(nums)):
            greater.append(nums[i])
        greater = greater[::-1]
        l = 0
        i = 0
        while i < len(ans) and l < len(less):
            ans[i] = less[l]
            l += 1
            i += 2
        
        r = 0
        i = 0
        while i < len(ans) and r < len(greater):
            if ans[i] == -1:
                ans[i] = greater[r]
                r += 1
            i += 1
        return ans
        