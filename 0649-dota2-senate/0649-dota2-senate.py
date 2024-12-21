class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        for i in range(len(senate)):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        n = len(senate)
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(n + r)
            else:
                dire.append(n + d)
        
        return "Radiant" if radiant else "Dire"