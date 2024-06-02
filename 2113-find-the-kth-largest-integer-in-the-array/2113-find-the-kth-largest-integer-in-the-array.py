class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(s) for s in nums]
        nums.sort(reverse = True)
        return str(nums[k-1])