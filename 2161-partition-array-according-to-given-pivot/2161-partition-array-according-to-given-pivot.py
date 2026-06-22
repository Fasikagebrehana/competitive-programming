class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        greater = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                smaller.append(nums[i])
            if nums[i] > pivot:
                greater.append(nums[i])

        smaller += ([pivot] * (len(nums) - (len(smaller) + len(greater))))
        smaller += greater
        return smaller