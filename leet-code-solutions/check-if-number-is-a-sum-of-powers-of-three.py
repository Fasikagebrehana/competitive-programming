import math
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ex = int(math.log(n, 3))
        expSum = 0
        for i in range(ex, -1, -1):
            if 3**i + expSum <= n:
                expSum += 3**i
        return expSum == n