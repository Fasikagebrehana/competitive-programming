class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        larger = []
        equal = 0
        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                larger.append(num)
            else:
                equal += 1

        smaller += [pivot] * equal
        return smaller + larger