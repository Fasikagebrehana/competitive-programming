class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            j, k =  i + 1, len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
        return res