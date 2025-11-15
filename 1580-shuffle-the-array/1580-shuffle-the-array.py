class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        i, j = 0, n
        while i < n and j < len(nums):
            result.append(nums[i])
            result.append(nums[j])
            i += 1
            j += 1
        return result