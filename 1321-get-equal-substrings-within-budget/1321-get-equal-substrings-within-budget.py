class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = []
        for i in range(len(s)):
            diff.append(abs(ord(s[i]) - ord(t[i])))
        print(diff)
        max_length = 0
        left = 0
        curr = 0
        for right in range(len(diff)):
            curr += diff[right]
            while left <= right and curr > maxCost:
                max_length = max(max_length, right - left)
                curr -= diff[left]
                left += 1
        max_length = max(max_length, right - left + 1)
        return max_length