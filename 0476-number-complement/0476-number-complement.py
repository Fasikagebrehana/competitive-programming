class Solution:
    def findComplement(self, num: int) -> int:
        s = ""
        while num > 0:
            s += str(num % 2)
            num //= 2
        s = s[::-1]
        temp = ""
        for i in s:
            if i == '1':
                temp += '0'
            else:
                temp += '1'
        res = int(temp, 2)
        return res