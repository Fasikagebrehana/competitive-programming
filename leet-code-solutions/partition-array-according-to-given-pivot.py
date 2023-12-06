class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater = []
        ans = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                ans.append(nums[i])
        for i in range(len(nums)):
            if nums[i] == pivot:
                ans.append(nums[i])
        for i in range(len(nums)):
            if nums[i] > pivot:
                ans.append(nums[i])
        return ans