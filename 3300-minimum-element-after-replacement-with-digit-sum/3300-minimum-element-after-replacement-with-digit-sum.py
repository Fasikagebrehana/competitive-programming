class Solution:
    def minElement(self, nums: List[int]) -> int:
        minn = inf
        for num in nums:
            summ = 0
            while num > 0:
                summ += num % 10
                num //= 10
            minn = min(summ, minn)
        return minn