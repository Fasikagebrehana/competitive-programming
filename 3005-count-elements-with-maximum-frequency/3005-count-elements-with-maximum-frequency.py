class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = []
        for i in range(len(nums)):
            counter.append(nums.count(nums[i]))
        counter.sort(reverse=True)
        return counter.count(counter[0])