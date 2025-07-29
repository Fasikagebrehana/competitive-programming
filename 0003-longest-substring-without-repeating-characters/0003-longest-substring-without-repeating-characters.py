class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        longestSubstring = 0
        left, right = 0, 0
        while right < len(s):
            counter[s[right]] += 1
            while left < right and counter[s[right]] > 1:
                counter[s[left]] -= 1
                left += 1
            longestSubstring = max(longestSubstring, right - left + 1)
            right +=1
        return longestSubstring