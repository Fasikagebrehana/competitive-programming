class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        answer = 0

        for i in range(len(nums)-1):
        #     if nums[i] > upper:
        #         return answer
            j = bisect_left(nums, lower - nums[i], i+1)
            idx = bisect_right(nums, upper - nums[i], i+1)
            # print(idx, j)
            if idx >= j:
                answer += idx - j
        return answer