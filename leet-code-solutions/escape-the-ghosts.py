class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
         
        # for i in range(len(target)):
        #     for j in range(len(ghosts)):
        #         if target in ghosts:
        #             return False
        #         if len(ghosts) == 1 and ghost[i][j]
        dis = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            distance = abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])
            if distance <= dis:
                return False
        return True