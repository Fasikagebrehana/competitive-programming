class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(nums, k):
            left = 0
            nice_subarray = 0
            counter = 0
            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    counter += 1
                while left < len(nums) and (counter) > k:
                    if nums[left] % 2 != 0:
                        counter -= 1
                        # if counter[nums[left]] == 0:
                        #     del counter[nums[left]]
                    left += 1
                nice_subarray += (right - left + 1)
            return nice_subarray
        # print(helper(k))        
        # print(helper(k-1))

        return (helper(nums, k) - helper(nums, k-1))
        