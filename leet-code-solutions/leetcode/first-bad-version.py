# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        
        # while low <= high:
        #     middle = (low + high) // 2
        #     if isBadVersion(middle):
        #         temp = middle
        #         high = middle - 1 
        #     else:
        #         low = middle + 1
        # return temp
        while low <= high:
            middle = (low + high) // 2
            if isBadVersion(middle):
                high = middle - 1
            else:
                low = middle + 1
        return low