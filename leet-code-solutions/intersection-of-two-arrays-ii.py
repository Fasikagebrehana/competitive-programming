class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        c1 = Counter(nums1)        
        c2 = Counter(nums2)
        for n in nums1:
            if c1[n] > 0 and c2[n] > 0:
                ans.append(n)
                c1[n] -= 1
                c2[n] -= 1
        # print(ans)
        return ans