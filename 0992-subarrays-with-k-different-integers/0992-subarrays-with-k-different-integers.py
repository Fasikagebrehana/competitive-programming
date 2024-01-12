class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        length = len(nums)
        left = 0
        sum_k = 0
        counter = defaultdict(int)
        
        for right in range(length):
            counter[nums[right]] += 1
            
            while left < length and len(counter) > k:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
            sum_k += (right - left + 1)
        
        left = 0
        sumk = 0
        counter = defaultdict(int)
        for right in range(length):
            counter[nums[right]] += 1
            
            while left < length and len(counter) > k - 1:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
            sumk += (right - left + 1)
                
   
        return sum_k - sumk