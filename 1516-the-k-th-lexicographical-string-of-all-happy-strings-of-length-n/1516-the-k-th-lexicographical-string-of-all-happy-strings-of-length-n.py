class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['a', 'b', 'c']
        happystr = []
        def backtrack(idx, arr):
            nonlocal happystr
            if arr and len(arr) == n:
                happystr.append(arr.copy())
                return
                
            
            for i in range(3):
                if arr and arr[-1] == letters[i]:
                    continue
                arr.append(letters[i])
                backtrack(i, arr)
                arr.pop()
        
        backtrack(0, [])
        # print(happystr)
        return ''.join(happystr[k-1]) if k <= len(happystr) else ""