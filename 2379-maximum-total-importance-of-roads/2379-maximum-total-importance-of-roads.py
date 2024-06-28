class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        indegree = [0] * n
        for x, y in roads:
            indegree[x] += 1
            indegree[y] += 1
        value = []
        for i in range(n):
            value.append((indegree[i], i))
        value.sort(reverse = True)
        values = [0] * n
        temp = n
        for x, y in value:
            values[y] = temp
            temp -= 1
        max_sum = 0
        for x, y in roads:
            max_sum += values[x] + values[y]
        return max_sum