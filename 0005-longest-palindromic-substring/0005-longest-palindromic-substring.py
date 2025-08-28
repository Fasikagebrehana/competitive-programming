class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s
        
        answer = ""
        l, r = 0, 1
        for i in range(len(s)):
             # since its even the center(middle) are 2 letters so we starting from the two by moving to the left and right we check palindrome

            l = i
            r = l+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(answer) < (r - l +1):
                    answer = s[l:r+1]
                l -= 1
                r += 1
            # trying or odd palindrome starting from that index which means the current i is a center then we are checking the previous and the next i+1 if the are equal or not
            if i == 0:
                continue
            middle = i
            l, r = middle - 1, middle + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(answer) < (r - l +1):
                    answer = s[l:r+1]
                l -= 1
                r += 1
        # print(answer)
                
        return answer if answer != "" else s[0]