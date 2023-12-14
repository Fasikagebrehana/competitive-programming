class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i  in range(len(paths)):
            p = paths[i].split()
            d = p[0]
            for j in range(1,len(p)):
                file, content = p[j].split('(')
                dic[content].append(f"{d}/{file}")
        ans = []
        for cont in dic.values():
            if len(cont) > 1:
                ans.append(cont)
        return ans
                
                    