class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = set()
        nums.sort()
        for i in range(len(nums)-2):
            store = defaultdict(int)
            target = -nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] in store:
                    ans = (nums[i], nums[j], nums[store[nums[j]]])
                    answer.add(ans)
                store[target - nums[j]] = j
        return list(answer)