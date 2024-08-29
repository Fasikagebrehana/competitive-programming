class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        time = n + n - 2
        k %= time
        if k < n:
            return k
        else:
            return (n + n - 2 - k)