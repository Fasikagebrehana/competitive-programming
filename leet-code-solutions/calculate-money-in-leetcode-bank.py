class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        result = 0
        prev = 0
        for i in range(n):
            if i % 7 == 0:
                prev += 1
                result = prev
            else:
                result += 1
            total += result
        return total
        
            