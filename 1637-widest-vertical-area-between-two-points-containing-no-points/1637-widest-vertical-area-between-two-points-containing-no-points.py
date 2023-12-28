class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        width = []
        dic = {}
        for x,y in points:
            width.append(x)
        width.sort()
        print(width)
        for i in range(1, len(width)-1):
            dic[i-1] = width[i] - width[i-1]
        return max(dic.values())