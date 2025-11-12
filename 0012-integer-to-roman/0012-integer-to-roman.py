class Solution:
    def intToRoman(self, num: int) -> str:
        # to compute in O(1) time
        # precompute the essential romans and numbers including numbers related to 4 and 9
        
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"]

        # iterate through the values and if its greater or equal we append corresponding roman symbol to our answer 
        answer = []

        for i in range(len(values)):
            while num >= values[i]:
                answer.append(romans[i])
                num -= values[i]
        # print(answer)
        return ''.join(answer)