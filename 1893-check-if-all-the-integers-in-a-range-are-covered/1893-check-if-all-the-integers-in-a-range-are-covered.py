class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        sets = set()
        numbers = set()
        for start, end in ranges:
            for i in range(start, end + 1):
                sets.add(i)
        for i in range(left, right+1):
            numbers.add(i)
        return numbers.issubset(sets)
