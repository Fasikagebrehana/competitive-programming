class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # print(len(nums1), len(nums2))
        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return 0
        xor = 0
        if len(nums2) % 2 == 1:
            for i in range(len(nums1)):
                xor ^= nums1[i]
        if len(nums1) % 2 == 1:
            for i in range(len(nums2)):
                xor ^= nums2[i]
        return xor