class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking
        # cases: if the sum of elements inside the arr greater than target
        # 
        arr = []
        result = []
        summ = 0
        def backtrack(idx):
            nonlocal summ
            if summ == target:
                result.append(arr[:])
                return
            if summ > target:
                return
            
            for i in range(idx, len(candidates)):
                arr.append(candidates[i])
                summ += candidates[i]
                backtrack(i)
                temp = arr.pop()
                summ -= temp
        
        backtrack(0)
        # print(result)
        return result