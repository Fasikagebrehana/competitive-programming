class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for j in range(len(operations)):
            x, y = operations[j]
            nums[dic[x]] = y
            dic[y] = dic[x]
        return nums