class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def backtrack(i, letter):
            if i == len(s):
                return ans.append(''.join(letter))
            if s[i].isalpha():
                # to lowercase
                letter.append(s[i].lower())
                backtrack(i+1, letter)
                letter.pop()
                # to uppercase
                letter.append(s[i].upper())
                backtrack(i+1, letter)
                letter.pop()
            else:
                letter.append(s[i])
                backtrack(i+1, letter)
                letter.pop()
        backtrack(0, [])
        return ans
