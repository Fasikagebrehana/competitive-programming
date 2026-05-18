class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            
            else:
                merged.append(intervals[i])
        # print(merged)
        # time complexity - O(n log n) for the sorting O(n) traverse, appending amortized O(1) so its O(n log n)
        # space complexity - O(n) because of using merged and No merging happens.
        return merged