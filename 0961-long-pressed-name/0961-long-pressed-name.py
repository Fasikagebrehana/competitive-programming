class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n, m = 0, 0
        if name[0] != typed[0] or name[len(name)-1] != typed[len(typed)-1]:
            return False
        while n < len(name) and m < len(typed):
            if name[n] == typed[m]:
                n += 1
                m += 1
            elif name[n] != typed[m] and n > 0 and typed[m] == name[n-1]:
                m += 1
            else:
                return False
        while m < len(typed) and typed[m] == name[n-1]:
            m += 1
        return n == len(name) and m == len(typed)