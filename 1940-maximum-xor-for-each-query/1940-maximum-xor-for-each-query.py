class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = []
        temp = nums[::-1]
        m = 2 ** maximumBit - 1
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
            ans.append(res^m)
        return ans[::-1]