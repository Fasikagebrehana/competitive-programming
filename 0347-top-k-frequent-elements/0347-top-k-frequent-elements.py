class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = 0
        store = defaultdict(int)
        for num in nums:
            store[num] += 1
        
        heap = []
        for key, val in store.items():
            heappush(heap, (-(val), key))
        
        answer = []
        while k > 0:
            answer.append((heappop(heap))[1])
            k -= 1
        return answer