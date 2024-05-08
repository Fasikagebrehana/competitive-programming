class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        arr = []
        for i in range(len(speed)):
            arr.append((efficiency[i], speed[i]))
        arr.sort(reverse = True)
        heap = []
        summ = 0
        mod = 10 ** 9 + 7
        i = 0
        maxx = 0
        while i < len(arr):
            if len(heap) < k:
                heappush(heap, arr[i][1])
                summ += arr[i][1]
                maxx = max(maxx, (summ * arr[i][0]))
                i += 1
            else:
                temp = heappop(heap)
                maxx = max(maxx, (summ * arr[i-1][0]))
                summ -= temp
        return maxx % mod