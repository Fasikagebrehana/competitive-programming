class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        whole_length = n + n - 2
        time = time % whole_length
        if time < n:
            return time + 1
        else:
            return (n + n - 1 - time)