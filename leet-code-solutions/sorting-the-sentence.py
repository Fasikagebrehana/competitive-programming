class Solution:
    def sortSentence(self, s: str) -> str:
        
        word = s.split()
        lis = {}
        for i in range(len(word)):
            x = word[i][-1]
            y = word[i][:len(word[i])-1]
            lis[x] = y
        sorted_lis = sorted(lis)
        ans = []
        for i in sorted_lis:
            ans.append(lis[i])
        res = ' '.join(ans)
        return res
        
        