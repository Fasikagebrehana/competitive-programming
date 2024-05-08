class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        arr = []
        for i in range(len(speed)):
            arr.append((efficiency[i], speed[i]))
        arr.sort(reverse = True)
        heap = []
        mod = 10**9 + 7
        summ = 0
        i = 0
        maxx = 0
        while i < len(arr):
            heappush(heap, arr[i][1])
            summ += arr[i][1]
            if len(heap) > k:
                temp = heappop(heap)
                summ -= temp
            
            maxx = max(maxx, (summ * arr[i][0]))
            i += 1
        return maxx % mod


            