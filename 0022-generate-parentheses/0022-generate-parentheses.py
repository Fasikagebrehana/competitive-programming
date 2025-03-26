class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        answer = []
        brackets = ['(', ')']
        def backtrack(arr):
            nonlocal answer, brackets
            if len(arr) == (n * 2):
                answer.append(''.join(arr.copy()))
                return

            if arr.count('(') < n:
                arr.append('(')
                backtrack(arr)
                arr.pop()
            if arr.count(')') < arr.count('('):
                arr.append(')')
                backtrack(arr)
                arr.pop()


            
        backtrack([])

        # print(answer)
        return answer