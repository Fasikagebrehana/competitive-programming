class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(arr, x)
        ans = []
        for i in range(len(arr)):
            ans.append((abs(arr[i]-x), arr[i]))
        ans.sort()
        res = []
        for i in range(k):
            res.append(ans[i][1])
        res.sort()
        return res