class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        subarray_sum = 0
        max_score = 0
        count = {}
        for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right], 0) + 1
            subarray_sum += nums[right]
            while count[nums[right]] > 1:
                subarray_sum -= nums[left]
                count[nums[left]] -= 1
                left += 1
            max_score = max(max_score, subarray_sum)
        return max_score
            