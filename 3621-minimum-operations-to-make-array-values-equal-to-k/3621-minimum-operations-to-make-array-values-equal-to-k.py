class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        greaterthanK = set()
        for num in nums:
            if num < k: 
                return -1
            if num > k:
                greaterthanK.add(num)
        
        return len(greaterthanK) if len(greaterthanK) > 0 else 0