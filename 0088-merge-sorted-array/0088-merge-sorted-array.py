class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
        else:
            
            nums1[:] = nums1[:m]
            for i in range(n):
                nums1.append(nums2[i])
            nums1.sort()