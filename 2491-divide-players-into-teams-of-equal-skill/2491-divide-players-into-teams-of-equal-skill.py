class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        che = 0
        summ = set()
        l, r = 0, len(skill) - 1
        while l < r:
            summ.add(skill[l] + skill[r])
            l += 1
            r -= 1
        a, b = 0, len(skill) - 1
        if len(summ) == 1:
            while a < b:
                che += (skill[a] * skill[b])
                a += 1
                b -= 1
            return che
        else:
            return -1