class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        prev = curr = ['0']
        while n > 0:
            prev = curr[:]
            curr.append('1')
            temp = []
            for bit in prev:
                if bit == '0':
                    temp.append('1')
                else:
                    temp.append('0')
            curr += temp[::-1][:]
            n -= 1
        # print(curr)
        return curr[k-1]