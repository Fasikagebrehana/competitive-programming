class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        ans = []
        for elements in cpdomains:
            lis = elements.split()
            s = ""
            for i in range(len(lis[1])-1, -1, -1):
                if lis[1][i] == ".":
                    dic[s[::-1]] = int(lis[0]) + dic.get(s[::-1], 0)
                s += lis[1][i]
            dic[s[::-1]] = int(lis[0]) + dic.get(s[::-1], 0)
        for key in dic:
            s = ""
            s += str(dic[key]) + " " + key
            ans.append(s)
        return ans