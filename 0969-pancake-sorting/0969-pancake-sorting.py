class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if arr == sorted(arr):
            return []
        end = len(arr)
        ans = []
        for i in range(len(arr)):
            maxIndex = arr.index(end) + 1
            if 1 < maxIndex < end:
                segment = arr[0:maxIndex]
                segment.reverse()
                arr[0:maxIndex] = segment
                endseg = arr[0:end]
                endseg.reverse()
                arr[:end] = endseg
                ans.append(maxIndex)                
                ans.append(end)
            elif maxIndex == 1:
                seg = arr[0:end]
                seg.reverse()
                arr[0:end] = seg
                ans.append(end)
            end -= 1
            print(arr)
        return ans