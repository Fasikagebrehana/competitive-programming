class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hset = {}
        for i in range(len(nums)):
            if nums[i] in hset and abs(i-hset[nums[i]]) <= k:
                return True
            hset[nums[i]] = i
        return False