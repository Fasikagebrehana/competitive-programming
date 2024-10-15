class Solution:
    def minimumSteps(self, s: str) -> int:
        steps = 0
        black, white = 0, 0
        for i in range(len(s)):
            if s[i] == '0':
                steps += black
            else:
                black += 1
        
        return steps