class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = defaultdict(int)
        
        l, r = 0, 0
        n = len(s)
        count = 0
        while r < n:
            freq[s[r]] += 1
            while l < r and len(freq) == 3:
                count += (n- r)
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            r += 1
        
        # print(count) 
        return count