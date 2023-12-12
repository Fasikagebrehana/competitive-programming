class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # a=0
        # b=0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] +nums[j] == target:
        #             a=i
        #             b=j
        # return [a,b]
        dic = {}
        ans = []
        for i in range(len(nums)):
            if target - nums[i] in dic:
                ans.append(i)
                ans.append(dic[target - nums[i]])
            dic[nums[i]] = i
        return ans