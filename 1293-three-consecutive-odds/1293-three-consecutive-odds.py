class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        left, right = 0, 0
        while right < len(arr):
            if arr[right] % 2 != 0:
                if right - left + 1 >= 3:
                    return True
                right += 1
            else:
                right += 1
                left = right
        return False