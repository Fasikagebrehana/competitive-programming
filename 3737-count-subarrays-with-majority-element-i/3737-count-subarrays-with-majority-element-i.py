class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        target_count = nums.count(target)
        count = 0
        # l, r = 0, 0
        # while l <len(nums) and r < len(nums):
        #     i

        for i in range(len(nums)):
            freq = defaultdict(int)
            for j in range(i, len(nums)):
                if nums[j] == target:
                    freq[nums[j]] += 1
                if 2 *(freq[target]) > (j- i + 1):
                    count += 1
        # print(count)
        return count