class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        dic = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            dic[sorted_s].append(s)
        return dic.values()