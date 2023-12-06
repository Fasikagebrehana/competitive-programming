class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        i = len(s) - 1
        summ = 0
        while i >= 0: 
            if i > 0 and s[i-1:i+1] in num:
                summ += num[s[i-1:i+1]]
                i -= 2
            else:
                summ += dic[s[i]]
                i -= 1
        return summ