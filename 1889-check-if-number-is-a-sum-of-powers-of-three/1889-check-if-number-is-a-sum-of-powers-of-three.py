class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        num = int(math.log(n, 3))
        summ = 0
        for i in range(num, -1, -1):
            if (3 ** i) + summ <= n:
                summ += (3 ** i)
        return summ == n