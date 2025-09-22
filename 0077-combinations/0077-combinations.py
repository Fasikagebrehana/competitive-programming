class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combinations = []
        arr = []
        def backtrack(num):
            nonlocal arr
            if len(arr) == k:
                combinations.append(arr[:])
                return
            if num > n:
                return
            
            for i in range(num, n+1):
                arr.append(i)
                backtrack(i+1)
                arr.pop()
        
        backtrack(1)
        # print(combinations)
        return combinations