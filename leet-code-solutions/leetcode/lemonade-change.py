class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = {5:0, 10:0, 20:0}
        for bill in bills:
            counter[bill] += 1
            if bill == 10:
                if counter[5] == 0:
                    return False
                counter[5] -= 1
            elif bill == 20:
                if counter[10] > 0 and counter[5] > 0:
                    counter[10] -= 1
                    counter[5] -= 1
                elif counter[5] >= 3:
                    counter[5] -= 3
                else:
                    return False
                    
        return True 