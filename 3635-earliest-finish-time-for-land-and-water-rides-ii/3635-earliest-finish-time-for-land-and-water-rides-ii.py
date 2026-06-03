class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def check(start1, dur1, start2, dur2):
            time1 = inf
            for i in range(len(start1)):
                time1 = min(time1, start1[i] + dur1[i])
            
            time2 = inf
            for j in range(len(start2)):
                time2 = min(time2, max(time1, start2[j]) + dur2[j])
            
            return time2
        starts_with_land = check(landStartTime, landDuration, waterStartTime, waterDuration)

        starts_with_water = check(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(starts_with_land, starts_with_water)
