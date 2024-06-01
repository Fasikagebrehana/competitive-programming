class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums = set(nums)
        numss = set(nums)
        for num in nums:
            temp = int(str(num)[::-1])
            if temp not in nums:
                numss.add(temp)
        return len(numss)