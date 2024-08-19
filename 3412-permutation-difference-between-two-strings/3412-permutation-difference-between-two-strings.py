class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        letters = defaultdict(list)
        for i in range(len(s)):
            letters[s[i]].append(i)
            letters[t[i]].append(i)
        ans = 0
        for x, y in letters.values():
            ans += abs(x - y)

        return ans