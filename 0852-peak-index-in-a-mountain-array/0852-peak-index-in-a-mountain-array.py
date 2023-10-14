class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        top = n-1
        bottom = 0
        while top >= bottom:
            middle = int((top + bottom)/2)
            if arr[middle] >= arr[middle + 1] and arr[middle] >= arr[middle - 1]:
                return middle
            elif arr[middle] < arr[middle+1]:
                bottom = middle
            else:
                top = middle