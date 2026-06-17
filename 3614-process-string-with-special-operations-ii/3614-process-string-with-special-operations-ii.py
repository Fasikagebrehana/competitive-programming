class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0
        # first calculate what the result of s after the operations 
        for ch in s:
            if ch == '*':
                if length > 0:
                    length -= 1
            elif ch == '#':
                length *= 2
            elif ch.isalpha():
                length += 1
        
        if (k +1) > length:
            return '.'
        
        # traverse on reverse when the length is equal with k+1 we return that character
        s = s[::-1]
        for ch in s:
            if ch == '*':
                length += 1
            elif ch == '%':
                # k changes bc % reverses the string
                k = length - k -1
            elif ch =='#':
                # check if k+1 > length+1 // 2
                if (k + 1) > (length +1) // 2:
                    k -= (length // 2)
                length = (length+1) // 2
            else:
                # if its character 
                if k +1 == length:
                    return ch
                length -= 1
        return '.'