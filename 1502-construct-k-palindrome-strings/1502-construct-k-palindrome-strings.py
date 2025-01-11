class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        counter = Counter(s)
        # print(counter)
        count_odd = 0
        for key, val in counter.items():
            if val % 2 == 1:
                count_odd += 1
        if count_odd > k:
            return False
        return True