class Solution:
    def getLucky(self, s: str, k: int) -> int:
        summ = 0
        ans = 0
        letters = ""
        for st in s:
            letters += str(ord(st) - ord('a') + 1)
        # print(letters)
        while k > 0:
            ans = 0
            for digits in letters:
                ans += int(digits)
            letters = str(ans)
            k -= 1
        return ans