class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        store =defaultdict(list)
        for s in strs:
            temp =  str(sorted(s))
            store[temp].append(s)
        # print(store)
        answer = []
        for key, val in store.items():
            answer.append(val)
        return answer