class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        if k <= numOnes:
            ans += k
            return ans
        elif k > numOnes:
            ans += numOnes
            if k > (ans + numZeros):
                ans += numZeros
                temp = k - ans
                ans -= temp
                return numOnes - temp
            else:
                return ans