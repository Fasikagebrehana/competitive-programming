class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(start, end,  turn):
            if start == end:
                if turn:
                    return [nums[start], 0]
                else:
                    return [0, nums[start]]
            if turn:
                leftScore = helper(start + 1, end, not turn)
                rightScore = helper(start, end - 1, not turn)
                leftScore[0] += nums[start]
                rightScore[0] += nums[end]
                if leftScore[0] > rightScore[0]:
                    return leftScore
                else:
                    return rightScore
            else:
                leftScore = helper(start + 1, end, not turn)
                rightScore = helper(start, end - 1, not turn)
                leftScore[1] += nums[start]
                rightScore[1] += nums[end]
                if leftScore[1] > rightScore[1]:
                    return leftScore
                else:
                    return rightScore
        p1, p2 = helper(0, len(nums) - 1, True)
        return p1 >= p2