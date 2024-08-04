class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarrsum = []
        for i in range(len(nums)):
            summ = 0
            for j in range(i, len(nums)):
                summ += nums[j]
                subarrsum.append(summ)
        
        subarrsum.sort()
        return (sum(subarrsum[left-1:right])) % (10**9 + 7)