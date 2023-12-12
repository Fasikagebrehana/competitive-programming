class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ans = []
        invalid = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                invalid.add(fronts[i])
        for i in range(len(fronts)):
            if fronts[i] not in invalid:
                ans.append(fronts[i])
            if backs[i] not in invalid:
                ans.append(backs[i])
        if len(ans) == 0:
            return 0
        else:
            return min(ans)