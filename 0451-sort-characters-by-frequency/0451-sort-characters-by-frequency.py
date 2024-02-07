class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        s_counter = sorted(counter.keys(), key=lambda x: counter[x], reverse = True)
        ans = []
        for i in range(len(s)):
            ans = ''.join([key * counter[key] for key in s_counter])
        return ans