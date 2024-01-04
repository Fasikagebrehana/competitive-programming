class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common = -1
        n, m = 0, 0
        while n < len(nums1) and m < len(nums2):
            if nums1[n] == nums2[m]:
                common = nums1[n]
                break
            elif nums1[n] < nums2[m]:
                n += 1
            else:
                m += 1
        return common