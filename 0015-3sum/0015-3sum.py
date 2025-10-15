class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for each element in nums we assume its target and do two sum on the rest
        answer = set()
        nums.sort()
        for i in range(len(nums)-2):
            store = defaultdict(int)
            target = -(nums[i])
            for j in range(i+1, len(nums)):
                if nums[j] in store:
                    ans = (nums[i], nums[j], nums[store[nums[j]]])
                    answer.add(ans)
                store[target - nums[j]] = j
        # print(answer)

        return list(answer)
        # time complexity = sorting nlogn + n^2 ~= n^2
        # space complexity = 2n ~= n best case