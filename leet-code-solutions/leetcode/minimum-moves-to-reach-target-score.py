class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        min_moves = 0
        while target > 1:
            if maxDoubles > 0 and target % 2 == 0:
                target = (target // 2)
                min_moves += 1
                maxDoubles -= 1
            elif target % 2 != 0 and maxDoubles > 0:
                target = target - 1
                min_moves += 1
                
                
            else:
                min_moves += (target - 1)
                break
        return min_moves