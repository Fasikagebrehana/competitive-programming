class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        i = 0
        ans = []
        dic = defaultdict(str)
        for c in s:
            dic[c] = s.rfind(c)
        last = s.rfind(s[0])
        ans = []
        c = 0
        for i in range(len(s)):
            if i <= last:
                if dic[s[i]] > last:
                    last = dic[s[i]]
                c += 1
            else:
                ans.append(c)
                c = 1
                last = s.rfind(s[i])
        ans.append(c)
        return ans
        