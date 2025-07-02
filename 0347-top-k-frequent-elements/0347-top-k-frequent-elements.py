class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Not which number is k times repeated
        # the most k frequent items
        counter = Counter(nums)
        frequent = []

        heap = []
        for key, val in counter.items():
            heappush(heap, (-val, key))
        # print(heap)
        while k > 0 and heap:
            count, num = heappop(heap)
            frequent.append(num)
            k -= 1
        return frequent