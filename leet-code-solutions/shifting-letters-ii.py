class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
            ascii_s = []
            for c in s:
                ascii_s.append(ord(c))
            temp = [0] * len(s)
            for start, end, direction in shifts:                
                if direction == 0:
                    temp[start] += -1
                    if (end + 1) < len(s):
                        temp[end+1] += 1
                else:
                    temp[start] += 1
                    if (end + 1) < len(s):
                        temp[end+1] += -1
            
            for i in range(1, len(temp)):
                temp[i] += temp[i-1]
                
                
            
            for j in range(len(s)):
                ascii_s[j] = (ascii_s[j] - 97 + temp[j]) % 26 + 97
        
            ans = "".join(chr(c) for c in ascii_s)
            return ans