class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        oddsum, evensum = 1, 2
        odd = 1
        even = 2
        while n > 1:
            odd += 2
            oddsum += odd
            even += 2
            evensum += even
            n -= 1
        # print(oddsum, evensum)
        return math.gcd(oddsum, evensum)