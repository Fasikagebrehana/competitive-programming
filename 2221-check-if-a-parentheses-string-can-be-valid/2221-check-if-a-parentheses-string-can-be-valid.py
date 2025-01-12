class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        open = 0
        unlocked = 0
        for i in range(len(s)):
            if locked[i] == '0':
                unlocked += 1
            elif s[i] == '(':
                open += 1
            elif s[i] == ')':
                if open > 0:
                    open -= 1
                elif unlocked > 0:
                    unlocked -= 1

                else:
                    return False
        # print(open, unlocked)
        counter = 0

        for i in range(len(s)-1, -1, -1):
            if locked[i] == '0':
                counter -= 1
                unlocked -= 1
            elif s[i] == '(':
                counter += 1
                open -= 1
            elif s[i] == ')':
                counter -= 1
            if counter > 0:
                return False
            if unlocked == 0 == open:
                break
        
        if open > 0:
            return False
        
        return True