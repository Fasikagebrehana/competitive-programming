class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        store = {}
        # def partition(idx, summ1, summ2):
        #     if idx == len(nums):
        #         return summ1 == summ2
            
        #     if (idx, summ1, summ2) not in store:
        #         if (idx) < len(nums):
        #             store[(idx, summ1, summ2)] = partition(idx + 1, summ1 + nums[idx], summ2) | partition(idx + 1, summ1, summ2 + nums[idx])
        #         else:
        #             store[(idx, summ1, summ2)] = (summ1 == summ2)
        #     return store[(idx, summ1, summ2)]
        # ans = partition(0, 0, 0)
        # return ans
        if sum(nums) % 2 != 0:
            return False
        half = sum(nums) // 2
        def partition(idx, targetSum):
            if idx == len(nums):
                return False

            if targetSum == 0:
                return True
            if targetSum < 0:
                return False
            
            if (idx, targetSum) not in store:
                store[(idx, targetSum)] = partition(idx + 1, targetSum - nums[idx]) or partition(idx + 1, targetSum)

            return store[(idx, targetSum)]

        return partition(0, half)
                