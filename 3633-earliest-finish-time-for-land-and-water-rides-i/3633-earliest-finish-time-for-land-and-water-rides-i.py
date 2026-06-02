class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        early_time = inf
        time = inf
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                time1 = landStartTime[i] + landDuration[i]
                land_water = max(time1, waterStartTime[j]) + waterDuration[j]
                early_time = min(early_time, land_water)

                time2 = waterStartTime[j] + waterDuration[j]
                water_land = max(time2, landStartTime[i]) + landDuration[i]
                early_time = min(early_time, water_land)
        
        return early_time

