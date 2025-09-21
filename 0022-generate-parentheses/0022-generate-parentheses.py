class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # approach is using backtracking collect all the well formed parentheses
        # we need open and closed brace counts 
        parenthesis = []
        arr = []
        def backtrack(openBrace, closedBrace, arr):

            if closedBrace == n and openBrace == n:
                parenthesis.append(''.join(arr[:]))
                return
            
            if openBrace > n or closedBrace > n:
                return

            if openBrace < n:
                arr.append('(')
                backtrack(openBrace + 1, closedBrace, arr)
                arr.pop()
            if closedBrace < openBrace:
                arr.append(')')
                backtrack(openBrace, closedBrace + 1, arr)
                arr.pop()
        
        backtrack(0, 0, arr)
        # print(parenthesis)

        return parenthesis