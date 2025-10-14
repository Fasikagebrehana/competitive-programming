class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        if ((sum(nums1) + nums1.count(0) < sum(nums2) + nums2.count(0)) and (nums1.count(0) ==0))  or ((sum(nums2) + nums2.count(0) < sum(nums1)  + nums1.count(0)) and (nums2.count(0) ==0)) :
            return -1


        max1 = sum(nums1) + nums1.count(0)
        max2 = sum(nums2) + nums2.count(0)

        return max(max1, max2)