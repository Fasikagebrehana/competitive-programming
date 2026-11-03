class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        heap = []
        for key, val in freq.items():
            heappush(heap, (-val, key))
        answer = []
        while k > 0:
            f, num = heappop(heap)
            answer.append(num)
            k -= 1
        return answer