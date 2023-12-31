class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for c in counter.values():
            if c % 2 != 0:
                return False
        return True