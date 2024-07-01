class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        num = []
        for i in range(len(nums1)):
            num.append(nums1[i] - nums2[i])
        count = 0
        def merge(lefthalf, righthalf):
            nonlocal count
            i, j = 0, 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] <= righthalf[j] + diff:
                    count += len(righthalf) - j
                    i += 1
                else:
                    j += 1
            left, right = 0, 0
            arr = []
            while left < len(lefthalf) and right < len(righthalf):
                if lefthalf[left] < righthalf[right]:
                    arr.append(lefthalf[left])
                    left += 1
                else:
                    arr.append(righthalf[right])
                    right += 1
            arr.extend(lefthalf[left:])
            arr.extend(righthalf[right:])
            return arr
        def mergesort(nums):
            if len(nums) <= 1:
                return nums
            middle = len(nums) // 2
            lefthalf = mergesort(nums[:middle])
            righthalf = mergesort(nums[middle:])
            return merge(lefthalf, righthalf)
        mergesort(num)
        return count