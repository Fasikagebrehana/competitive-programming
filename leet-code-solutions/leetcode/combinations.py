class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        # def helper(startNum, arr):
            # if len(arr) == k:
            #     ans.append(arr[:])
            #     # copying the whole array to ans
            #     return
            # for num in range(startNum, n+1):
            #     arr.append(num)
            #     helper(num + 1, arr)
            #     arr.pop()
        nums = [num for num in range(1, n+1)]
        def backtrack(i, arr):
            if len(arr) == k:
                ans.append(arr[:])
                return
            if i >= n:
                return
            backtrack(i+1, arr)
            arr.append(nums[i])
            backtrack(i+1, arr)
            arr.pop()
        backtrack(0, [])
        return ans
