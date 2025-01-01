class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            middle = (left + right) // 2
            if middle == 0:
                left = middle + 1
            elif middle == len(arr) - 1:
                right = middle - 1
            else:
                if arr[middle] > arr[middle - 1] and arr[middle] > arr[middle + 1]:
                    return middle
                elif arr[middle] < arr[middle - 1]:
                    right = middle - 1
                elif arr[middle] < arr[middle + 1]:
                    left = middle + 1
                    