class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_sub = 0
        store = {}
        # def dp(idx, prev):
            # if idx >= len(nums):
            #     return 0
            # if (idx, prev) not in store:
            #     if nums[idx] <= prev:
            #         store[(idx, prev)] = dp(idx + 1, prev)
            #     else:
            #         take = 1 + dp(idx + 1, nums[idx])
            #         notake = dp(idx + 1, prev)
            #         store[(idx, prev)] = max(take, notake)
            # return store[(idx, prev)]
        
        def dp(i):
            if i >= len(nums):
                return 0
            if i not in store:
                store[i] = 1
                for j in range(i+1, len(nums)):
                    if nums[j] > nums[i]:
                        store[i] = max(1 + dp(j), store[i])
            return store[i]

        for i in range(len(nums)):
            max_sub = max(max_sub, dp(i))
        return max_sub