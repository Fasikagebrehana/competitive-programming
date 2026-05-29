class Solution:
    def minElement(self, nums: List[int]) -> int:
        minn = inf
        for num in nums:
            summ = 0
            for digit in str(num):
                summ += int(digit)
            minn = min(minn, summ)
        return minn