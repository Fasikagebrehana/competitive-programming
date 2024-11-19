class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        summ = 0
        max_subarray_sum = 0
        dic = {}
        left = 0

        for right in range(len(nums)):
            summ += nums[right]
            if nums[right] not in dic:
                dic[nums[right]] = 1
            else:
                dic[nums[right]] += 1
            
            while dic[nums[right]] > 1 and left <= right:
                dic[nums[left]] -= 1
                summ -= nums[left]
                left += 1
            
            if right - left + 1 == k:
                max_subarray_sum = max(max_subarray_sum, summ)
                dic[nums[left]] -= 1
                summ -= nums[left]
                left += 1
        if right - left == k:
                max_subarray_sum = max(max_subarray_sum, summ)
                
        return max_subarray_sum