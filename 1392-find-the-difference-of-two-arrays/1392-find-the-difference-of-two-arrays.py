class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        temp = set()
        for num in nums1:
            if num not in nums2:
                temp.add(num)
        ans.append(list(temp))
        temp = set()
        for num in nums2:
            if num not in nums1:
                temp.add(num)

        ans.append(list(temp))
        return ans