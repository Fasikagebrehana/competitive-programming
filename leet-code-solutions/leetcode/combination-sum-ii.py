class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = []
        ans = []
        summ = 0
        candidates.sort()
        
        def helper(idx, prev):
            nonlocal summ
            if summ == target and arr not in ((ans)):
                ans.append(arr[:])
                return
            if summ > target:
                return
            for i in range(idx, len(candidates)):
                if candidates[i] == prev:
                    continue
                arr.append(candidates[i])
                summ += candidates[i]
                # prev = arr.pop()
                helper(i+1, prev)
                if arr:
                    prev = arr.pop()
                    summ -= prev
        helper(0, -1)
        return ans
