class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_distance = -inf
        initialMaxx = arrays[0][-1]
        initialMinn = arrays[0][0]

        for i in range(1, len(arrays)):
            maxx = max(abs(arrays[i][-1] - initialMinn), abs(initialMaxx - arrays[i][0]))
            max_distance = max(max_distance, maxx)
            initialMaxx = max(initialMaxx, arrays[i][-1])
            initialMinn = min(initialMinn, arrays[i][0])
        return max_distance