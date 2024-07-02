class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, u1: int, u2: int) -> int:
        # def lcm(x, y):
        #     return abs(x * y) // math.gcd(x, y)

        def checker(mid):
            notdiviby1 = mid - mid // divisor1
            if notdiviby1 < u1:
                return False
            notdiviby2 = mid - mid // divisor2
            if notdiviby2  < u2:
                return False
            notdivibyboth = mid - mid // math.lcm(divisor1, divisor2)
            if notdivibyboth < (u1 + u2):
                return False
            
            return True
                
        left, right = 1, 10**10
        ans = right
        while left <= right:
            middle = (left + right) // 2
            if checker(middle):
                right = middle - 1
            else:
                left = middle + 1
        return left