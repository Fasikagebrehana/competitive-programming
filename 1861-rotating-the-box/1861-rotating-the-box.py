class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # * is obstacle
        for ind in range(len(boxGrid)):
            j = len(boxGrid[0]) - 1
            for i in range(len(boxGrid[0])-1, -1, -1):
                if boxGrid[ind][i] == '*':
                    j = i -1
                elif boxGrid[ind][i] == '#':
                    boxGrid[ind][i] = '.'
                    boxGrid[ind][j] = '#'
                    j -= 1
        rotated = [[None] * len(boxGrid) for _ in range(len(boxGrid[0]))]

        for r in range(len(boxGrid)):
            for c in range(len(boxGrid[0])):
                rotated[c][len(boxGrid) - 1 - r] = boxGrid[r][c]

        return rotated