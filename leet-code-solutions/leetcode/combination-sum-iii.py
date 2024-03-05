class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        summ = 0
        arr = []
        def helper(idx):
            nonlocal summ
            if summ == n and len(arr) == k:
                ans.append(arr[:])
                return
            if summ > n or len(arr) > k or idx > 9:
                return
            for i in range(idx, 10):
                arr.append(i)
                summ += i
                helper(i+1)
                summ -= arr.pop()
        helper(1)
        return ans