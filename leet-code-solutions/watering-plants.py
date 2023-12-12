class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step = 0
        curr_water = capacity
        n = len(plants)
        for i in range(n):
            if plants[i] > curr_water:
                step += 2*i 
                curr_water = capacity
            curr_water -= plants[i]
            step += 1
        return step