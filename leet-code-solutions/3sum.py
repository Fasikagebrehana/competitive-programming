class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        nums.sort()
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            j, k =  i + 1, len(nums)-1
            while j < k:
                if nums[j] + nums[k] == target:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        
                    while j < len(nums) and nums[j] == nums[j-1]:
                        j += 1
                    while k >= 0 and nums[k] == nums[k+1]:
                        k -= 1
                elif (nums[j] + nums[k]) > target:
                    k -= 1
                else:
                    j += 1
            
        return list(ans)