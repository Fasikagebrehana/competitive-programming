class Solution:
    def balancedString(self, s: str) -> int:
        counter = {'Q':0, 'R':0, 'W':0, 'E':0}
        for c in s:
            if c not  in counter:
                counter[c] = 1
            else:
                counter[c] += 1
        occur = math.ceil(len(s)/4)
        min_length = len(s)
        left = 0
        print(counter)
        for right in range(len(s)):
            counter[s[right]] -= 1
            while left < len(s) and counter['Q'] <= occur and counter['E'] <= occur and counter['R'] <= occur and counter['W'] <= occur:
                min_length = min(min_length, right-left+1)
                counter[s[left]] += 1
                left += 1
        return min_length