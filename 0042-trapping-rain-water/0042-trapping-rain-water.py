class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]
        maxRight = []

        maxl = 0
        for i in range(1, len(height)):
            if maxl < height[i-1]:
                maxl = height[i-1]
            maxLeft.append(maxl)
        maxr = 0


        for i in range(len(height)-1, -1, -1):
            maxRight.append(maxr)
            if maxr < height[i]:
                maxr = height[i]
        maxRight = maxRight[::-1]

        ans = 0
        for i in range(len(height)):
            temp = min(maxLeft[i], maxRight[i]) - height[i]
            if temp > 0:
                ans += temp
        return ans