class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        max_radius = -inf
        for i in range(len(houses)):
            idx = bisect_left(heaters, houses[i])
            if idx == len(heaters):
                max_radius = max(max_radius, abs(heaters[-1] - houses[i]))
            elif idx == 0:
                max_radius = max(max_radius, abs(heaters[0] - houses[i]))
            else:
                minn = min(abs(heaters[idx] - houses[i]), abs(heaters[idx - 1] - houses[i]))
                max_radius = max(max_radius, minn)
        return max_radius