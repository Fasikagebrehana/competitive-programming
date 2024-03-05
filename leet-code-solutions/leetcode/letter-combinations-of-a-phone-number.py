class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        dic = {2: ['a','b','c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 
        5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        s = []
        ans = []
        def helper(idx, dic):
            if len(s) == len(digits):
                ans.append(''.join(s[:]))
                return
            # for i in range(idx, len(digits)):
            for j in range(len(dic[int(digits[idx])])):
                s.append(dic[int(digits[idx])][j])
                helper(idx+1, dic)
                s.pop()
        helper(0, dic)
        return ans