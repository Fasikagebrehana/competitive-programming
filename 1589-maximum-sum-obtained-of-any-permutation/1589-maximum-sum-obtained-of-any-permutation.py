class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freq = [0] * len(nums)
        for start, end in requests:
            freq[start] += 1
            if end+1 < len(nums):
                freq[end+1] -= 1
        for i in range(1, len(freq)):
            freq[i] += freq[i-1]
        freq.sort(reverse = True)
        nums.sort(reverse = True)
        summ = 0
        for i in range(len(nums)):
            summ += (nums[i] * freq[i])
        modulo = 10**9 + 7
        return summ % modulo