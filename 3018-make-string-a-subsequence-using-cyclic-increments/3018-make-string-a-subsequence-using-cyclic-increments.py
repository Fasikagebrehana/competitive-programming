class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            return False
        i = j = 0
        count = 0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                i += 1
                j += 1
            else:
                if (ord(str2[j]) - ord(str1[i])) == 1 or str1[i] == 'z' and str2[j] == 'a':

                    count +=1
                    i += 1
                    j += 1
                else:
                    i += 1
        if j < len(str2):
            return False
        return True