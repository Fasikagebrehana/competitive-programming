class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # step 1
        # create a connected elements of the pairs
        parent = list(range(len(s)))
        # print(parent)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for a, b in pairs:
            parent[find(a)] = find(b)
        
        dic = defaultdict(list)
        for i in range(len(s)):
            dic[find(i)].append(s[i])
        
        for key in dic.keys():
            dic[key].sort(reverse = True)
        # print(dic)

        return "".join(dic[find(i)].pop() for i in range(len(s)))