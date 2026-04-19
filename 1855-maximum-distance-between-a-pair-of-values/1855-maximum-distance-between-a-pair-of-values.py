class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        distance = 0
        while i < len(nums1) and j < len(nums2):
            while j < len(nums2) and nums1[i] <= nums2[j]:
                j += 1
            distance = max(distance, j - i-1)
            i += 1
        return distance