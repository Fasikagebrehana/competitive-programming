class Solution:
    def reachNumber(self, target: int) -> int:
        left = 0
        right = 1000000000
        if target < 0:
            target = 0 - target

        def check(num):
            res = (num*(1+num)/2)
            return res

        while left+1 < right:
            middle = (left + right) // 2
            guess = check(middle)
            if guess < target:
                left = middle 
            else:
                right = middle
        

        while (check(right)-target)  %2:
            right += 1
        

        return right
