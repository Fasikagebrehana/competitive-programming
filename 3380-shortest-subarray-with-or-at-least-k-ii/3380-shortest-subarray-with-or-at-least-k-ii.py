class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_subArr = inf
        left = 0
        ored = 0
        bit_Count = [0] * 32

        for right in range(len(nums)):
            ored |= nums[right]
            for i in range(32):
                if nums[right] & (1<<i):
                    bit_Count[i] += 1
            while ored >= k and left <= right:
                min_subArr = min(min_subArr, right - left + 1)
                new_ored = 0
                for i in range(32):
                    if nums[left] & (1<<i):
                        bit_Count[i] -= 1
                    if bit_Count[i] > 0:
                        new_ored |= (1<<i)
                ored = new_ored
                left += 1
        return min_subArr if min_subArr != inf else -1