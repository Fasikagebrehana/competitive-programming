class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(st, l, r):
            # l, r = 0, len(st) - 1
            while l <= r:
                if st[l] != st[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        store = {}
        ans = []
        arr = []
        def dp(idx):
            nonlocal arr, ans
            if idx >= len(s):
                ans.append(arr.copy())
                return
            
            # if idx not in store :
            for j in range(idx, len(s)):
                if isPalindrome(s, idx, j):
                    arr.append(s[idx:j+1])
                    # store[idx] = dp(idx + 1)
                    dp(j + 1)
                    if arr:
                        arr.pop()
                            
        
        dp(0)
        return ans