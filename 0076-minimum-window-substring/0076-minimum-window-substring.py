class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        t_dict = {}
        s_dict = {}
        start, end = 0, 0
        min_win = float('inf')
        ans = ""

        for i in range(len(t)):
            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] += 1

        count = 0
        left = 0

        for right in range(len(s)):
            if s[right] in t_dict:
                if s[right] in s_dict:
                    s_dict[s[right]] += 1
                else:
                    s_dict[s[right]] = 1

                if s_dict[s[right]] <= t_dict[s[right]]:
                    count += 1

            while count == len(t):
                if (right - left + 1) < min_win:
                    start, end = left, right
                    min_win = right - left + 1

                if s[left] in s_dict:
                    s_dict[s[left]] -= 1

                    if s_dict[s[left]] < t_dict[s[left]]:
                        count -= 1

                left += 1

        return s[start:end+1] if min_win != float('inf') else ""
                    