class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        count = 0
        maxx = 0
        for num in nums:
            maxx |= num
        # print(ored)

        def backtrack(start, arr):
            nonlocal count
            for i in range(start, len(nums)):
                arr.append(nums[i])
                backtrack(i + 1, arr)
                ored = 0
                for num in arr:
                    ored |= num
                if ored == maxx:
                    count += 1
                arr.pop()
        backtrack(0, [])
        
        return count