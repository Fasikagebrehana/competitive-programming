class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        store = defaultdict(int)
        left = right = 0
        n = len(s)
        total_substrings = 0
        # def helper()

        while right < n:
            store[s[right]] += 1

            while left < right and len(store) >= 3:
                total_substrings += (n - right)
                store[s[left]] -= 1
                if store[s[left]] == 0:
                    del store[s[left]]
                left += 1
            right += 1
        # print(total_substrings)
        return total_substrings