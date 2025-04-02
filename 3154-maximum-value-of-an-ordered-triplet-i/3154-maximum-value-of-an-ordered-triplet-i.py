class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_triplets = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    temp = (nums[i] - nums[j])
                    for k in range(j + 1, len(nums)):
                        max_triplets = max(max_triplets, temp * nums[k])
        return max_triplets