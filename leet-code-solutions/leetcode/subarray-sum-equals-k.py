class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        summ = 0
        k_subarray = 0
        count[0] = 1
        for right in range(len(nums)):
            summ += nums[right]
            if (summ - k) in count:
                k_subarray += count[summ - k]
            count[summ] += 1
        return k_subarray