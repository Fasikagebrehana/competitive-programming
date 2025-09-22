class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        arr = []
        letters = []
        phone_board = {
            '1': [], '2': ['a', 'b','c'],    '3': ['d','e','f'],
            '4': ['g','h','i'],     '5': ['j','k','l'],     '6': ['m','n','o'],
            '7': ['p','q','r','s'], '8': ['t','u','v'],     '9': ['w','x','y','z']
        }
        if not digits:
            return []

        # we have an index and a phone board, by iterating on the phone board using our index create a combination of the letters then collect them in arr then append them in our result arr
        # idx goes from 0 to  len of digits



        def backtrack(idx):
            nonlocal arr
            if len(arr) == len(digits):
                letters.append(''.join(arr[:]))
                return
            # iterating over phone_board and finding their combination
            for ch in phone_board[digits[idx]]:
                arr.append(ch)
                backtrack(idx + 1)
                arr.pop()
        
        backtrack(0)
        # print(letters)
        return letters