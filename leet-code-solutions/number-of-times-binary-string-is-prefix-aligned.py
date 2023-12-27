class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        arr = [0]*len(flips)
        count = 0
        leftcount = 0
        for i in range(len(flips)):
            arr[flips[i]-1] = 1
            if arr[i] == 1:
                leftcount += 1
            if (flips[i]-1) < i:
                leftcount += 1
            if leftcount == i+1:
                count += 1
        return count
                    