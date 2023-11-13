class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]