class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = defaultdict(int)
        summ = 0
        subarray_count = 0
        counter[0] = 1
        for right in range(len(nums)):
            summ += nums[right]
            if (summ - goal) in counter:
                subarray_count += counter[summ - goal]
            counter[summ] += 1
        return subarray_count