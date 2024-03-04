class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        arr = []
        summ = 0
        candidates.sort()
        def helper(idx):
            nonlocal summ
            if summ == target:
                ans.append(arr[:])
                return
            if summ > target:
                return
            for i in range(idx, len(candidates)):
                arr.append(candidates[i])
                summ += candidates[i]
                helper(i)
                summ -= arr.pop()
                
        helper(0)
        return ans
