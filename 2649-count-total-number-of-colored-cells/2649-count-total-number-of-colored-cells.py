class Solution:
    def coloredCells(self, n: int) -> int:
        curr = n ** 2
        prev = (n-1) ** 2
        # print(curr, prev)
        return (curr + prev)