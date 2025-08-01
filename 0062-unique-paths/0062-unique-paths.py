class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # totallly to reach m-1, n-1 we have 2 options right and down
        # which means starting from 0, 0 robot moves m-1 and n-1
        # we can take the combination using the sum of these 2 which is 
        # m-1 + n-1 = m +n -2

        nominator = m +n - 2
        r = math.factorial(n-1)
        denominator = r * math.factorial(m-1)
        combination = math.factorial(nominator) // denominator
        return combination