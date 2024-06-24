class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
        else:
            for i in range(len(nums1)):
                if i+1 == m:
                    break
            nums1[:] = nums1[:i+1]
            for i in range(n):
                nums1.append(nums2[i])
            nums1.sort()