class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(arr, x)
        ans = []
        left, right = idx - 1, idx
        while left >= 0 or right < len(arr):
            if len(ans) == k:
                break
            if left < 0:
                ans.append(arr[right])
                right += 1
            elif right >= len(arr):
                ans.append(arr[left])
                left -= 1
            else:
                if x - arr[left] > abs(x - arr[right]):
                    ans.append(arr[right])
                    right += 1
                else:
                    ans.append(arr[left])
                    left -= 1
        ans.sort()
        return ans
