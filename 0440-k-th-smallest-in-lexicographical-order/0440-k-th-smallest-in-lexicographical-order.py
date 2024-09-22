class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def counter(curr):
            nextCurr = curr + 1
            nums = 0
            while curr <= n:
                nums += min(n+1, nextCurr) - curr
                curr *= 10
                nextCurr *= 10
            return nums

        k -= 1
        curr = 1
        while k > 0:
            num = counter(curr)
            if num <= k:
                k -= num
                curr += 1
            else:
                curr *= 10
                k -= 1
        return curr