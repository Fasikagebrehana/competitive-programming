class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        totalpassengers = 0
        max_end = max(trip[2] for trip in trips)
        temp = [0] * (max_end + 1)
        for passengers, start, end in trips:
            temp[start] += passengers
            temp[end] -= passengers
        for i in range(1, len(temp)):
            temp[i] += temp[i-1]
        if max(temp) > capacity:
            return False
        else:
            return True
        