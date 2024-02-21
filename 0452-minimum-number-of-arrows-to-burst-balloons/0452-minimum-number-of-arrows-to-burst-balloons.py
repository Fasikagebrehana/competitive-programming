class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        pt = sorted(points, key=lambda points:points[1])
        ans = 1
        temp = pt[0][1]
        for i in range(1, len(pt)):
            if temp < pt[i][0]:
                temp = pt[i][1]
                ans += 1
        return ans
                