class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        store = defaultdict(list)
        for s in strs:
            ss = sorted(s)
            store[''.join(ss)].append(s)
        
        for key, val in store.items():
            ans.append(val)
        return ans