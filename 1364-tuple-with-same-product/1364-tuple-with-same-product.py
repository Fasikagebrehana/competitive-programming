class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        store = defaultdict(list)
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                store[nums[i] * nums[j]].append((nums[i], nums[j]))
                # store[nums[i] * nums[j]].append((nums[j], nums[i]))
        
        for key, val in store.items():
            if len(val) > 1:
                x = (len(val) * (len(val) - 1)) // 2
                count += (x * 8)
                
        return count