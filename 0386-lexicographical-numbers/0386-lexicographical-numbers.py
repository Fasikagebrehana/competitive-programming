class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def dfs(current):
            nonlocal ans
            if current > n:
                return
            ans.append(current)

            for i in range(0, 10):
                if (current * 10) + i > n:
                    return
                else:
                    dfs((current * 10) + i)
        
        for i in range(1, 10):
            dfs(i)
        return ans