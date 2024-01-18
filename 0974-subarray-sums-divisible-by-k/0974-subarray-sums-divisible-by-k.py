class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        summ = 0
        subarray = 0
        counter = defaultdict(int)
        counter[0] = 1
        for i in range(len(nums)):
            summ += nums[i]
            if (summ % k) in counter:
                subarray += counter[summ % k]
            counter[summ % k] += 1
        return subarray
            