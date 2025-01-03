class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for num, count in counter.items():
            heappush(heap, (-count, num))
        
        freq_elements = []
        while heap and k > 0:
            c, num = heappop(heap)
            freq_elements.append(num)
            k -= 1
        return freq_elements