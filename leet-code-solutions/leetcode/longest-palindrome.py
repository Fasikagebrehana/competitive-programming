class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(set(s)) == 1:
            return len(s)
        flag = False
        ans = 0
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        
        for key in dic:
            if dic[key] > 1 and dic[key] % 2 == 0:
                ans += dic[key]
            elif dic[key] > 1 and dic[key] % 2 != 0:
                ans += (dic[key] - 1)
                flag = True
        if 1 in dic.values() or flag:
            return ans + 1
        else:
            return ans
        