class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for num in gifts:
            heappush(heap, -(num))
        
        while heap and k > 0:
            num = math.isqrt(-(heappop(heap)))
            # print(num)
            if num > 0:
                heappush(heap, -num)
            k -= 1
        
        return -(sum(heap))