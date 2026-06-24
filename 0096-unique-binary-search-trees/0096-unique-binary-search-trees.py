class Solution:
    def numTrees(self, n: int) -> int:
        # since only the count is needed I don't need to construct the tree only the possibilities

        memo = {0:1, 1:1}
        def dp(node):
            if node in memo:
                return memo[node]
            total = 0
            # the possibilities are currnode -1 are gonna be on left of the tree
            # node -  currnode will be to the right
            for root in range(1, node+1):
                left = root - 1
                right = node - root
                total += dp(left) * dp(right)
            
            memo[node] = total
            return total
        return dp(n)