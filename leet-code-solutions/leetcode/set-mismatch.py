class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            if nums[i] - i == 1:
                i +=1
            else:
                if nums[nums[i]-1] == nums[i]:
                    i += 1
                else:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(len(nums)):
            if (i+1) != nums[i]:
                ans.append(nums[i])
                ans.append(i+1)
    
        return ans