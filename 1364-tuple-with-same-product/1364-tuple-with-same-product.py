class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        store = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                store[nums[i] * nums[j]] += 1
                # store[nums[i] * nums[j]].append((nums[j], nums[i]))
        
        for key, val in store.items():
            if val > 1:
                x = (val * (val - 1)) // 2
                count += (x * 8)
                
        return count