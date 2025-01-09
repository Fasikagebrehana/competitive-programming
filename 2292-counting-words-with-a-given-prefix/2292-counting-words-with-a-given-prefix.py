class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefix_count = 0
        for i in range(len(words)):
            if pref in words[i]:
                index = words[i].index(pref)
                if index == 0:
                    prefix_count += 1
        return prefix_count