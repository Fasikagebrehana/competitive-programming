class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # dp with 2 pointers for each array
        # min len
        # summ + new < summ pass
        n = min(len(nums1), len(nums2))
        store = {}
        def dp(i, j):
            if i >= len(nums1) or j >= len(nums2):
                return float("-inf")

            if (i, j) in store:
                return store[(i,j)]
            

            summ = max((nums1[i]*nums2[j]) + dp(i+1, j+1), (nums1[i]*nums2[j]), dp(i+1, j), dp(i, j+1))
            
            store[(i, j)] = summ
            return store[(i,j)]
        # print(dp(0, 0))
        return dp(0, 0)
