class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dic = {}
        set_num = set(nums)
        left = 0
        complete_subarray = 0
        for right in range(len(nums)):
            if nums[right] in dic:
                dic[nums[right]] += 1
            else:
                dic[nums[right]] = 1
            while len(set_num) == len(dic):
                dic[nums[left]] -= 1
                if dic[nums[left]] == 0:
                    del dic[nums[left]]
                left += 1
            complete_subarray += left
        return complete_subarray