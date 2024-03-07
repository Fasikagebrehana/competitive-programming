class Solution:
    def hIndex(self, citations: List[int]) -> int:
        high, low = len(citations), 0
        def helper(middle):
            if (len(citations) - bisect_right(citations, middle)) > middle:
                return True
            return False
        
        while high >= low:
            middle = (high + low) // 2
            if helper(middle):
                low = middle + 1
            else:
                high = middle - 1
        return low
