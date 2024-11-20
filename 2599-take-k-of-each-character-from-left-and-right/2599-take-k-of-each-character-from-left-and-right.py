class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = {'a': s.count('a'), 'b': s.count('b'), 'c': s.count('c')}
        left = 0
        if min(count.values()) < k:
            return -1

        answer = inf
        for right in range(len(s)):
            count[s[right]] -= 1
            while min(count.values()) < k:
                count[s[left]] += 1
                left += 1
            answer = min(answer, len(s) - (right - left + 1))
        return answer