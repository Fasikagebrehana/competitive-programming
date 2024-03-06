class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        ans = []
        temp = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                temp = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        ans.append(temp)
        temp = -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                temp = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        ans.append(temp)
        return ans
