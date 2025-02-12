class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        store = defaultdict(list)
        nums.sort(reverse = True)
        for i in range(len(nums)):
            summ = 0
            for s in str(nums[i]):
                summ += int(s)
            store[summ].append(i)
        # print(store)
        answer = -1
        for key, val in store.items():
            if len(val) > 1:
                answer = max(answer, nums[val[0]] + nums[val[1]])
        return answer