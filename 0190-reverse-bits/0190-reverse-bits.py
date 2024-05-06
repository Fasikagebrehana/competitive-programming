class Solution:
    def reverseBits(self, n: int) -> int:
        # res = bin(n)[2:]
        # res = res[::-1]
        return int("{:032b}".format(n)[::-1], 2)
