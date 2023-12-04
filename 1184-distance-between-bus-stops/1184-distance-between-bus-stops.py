class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        minimum = min(start, destination)
        maximum = max(start, destination)
        sum1 = sum(distance[minimum:maximum])
        sum2 = sum(distance[:minimum]) + sum(distance[maximum:])
        return min(sum1, sum2)