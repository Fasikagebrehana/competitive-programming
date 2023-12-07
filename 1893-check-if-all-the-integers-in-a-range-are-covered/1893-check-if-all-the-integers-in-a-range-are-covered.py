class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        sets = set()
        for start, end in ranges:
            for i in range(start, end + 1):
                sets.add(i)
        # for i in range(len(ranges)):
        #     for j in range(len(ranges[i])):
        #         for k in range(i, j+1):
        #             sets.add(k)
        print(sets)
        for i in range(left, right+1):
            if i not in sets:
                return False
        return True
#         maxim = max(sets)
#         minim = min(sets)
        
#         if left >= minim and right <= maxim:
#             return True
#         else:
#             return False