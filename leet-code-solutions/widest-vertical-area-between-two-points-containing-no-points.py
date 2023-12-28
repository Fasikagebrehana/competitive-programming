class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        width = []
        dic = {}
        for p in points:
            width.append(p[0])
        width.sort()
        
        for i in range(1, len(width)-1):
            dic[i-1] = width[i] - width[i-1]
        return max(dic.values())