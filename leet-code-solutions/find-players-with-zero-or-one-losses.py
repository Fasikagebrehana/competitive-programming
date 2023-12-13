class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic1 = {}
        dic2 = {}
        win , lose = [], []
        for w, l in matches:
            if w in dic1:
                dic1[w] += 1
            else:
                dic1[w] = 1
            if l in dic2:
                dic2[l] += 1
            else:
                dic2[l] = 1
        win = [p for p in dic1 if p not in dic2]
        lose = [i for i in dic2 if dic2[i] == 1]
        win.sort()
        lose.sort()
        return [win, lose]