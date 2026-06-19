class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        curr = 0
        for i in range(len(gain)):
            curr = gain[i] + curr
            
            max_altitude = max(max_altitude, curr)
            
        return max_altitude
