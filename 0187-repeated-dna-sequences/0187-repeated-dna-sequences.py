class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return
        dic = defaultdict(int)
        dic[s[:10]] += 1
        left = 1
        for right in range(10, len(s)):
            dic[s[left:right+1]] += 1
            left += 1
        ans = []
        for key, val in dic.items():
            if val > 1:
                ans.append(key)
        return ans