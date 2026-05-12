class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = defaultdict(int)
        for i in range(len(nums)):
            if (target - nums[i]) in store:
                return [store[target - nums[i]], i+1]
            else:
                store[nums[i]] = i+1
