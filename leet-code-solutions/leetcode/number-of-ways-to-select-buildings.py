class Solution:
    def numberOfWays(self, s: str) -> int:
        zero = [0] * len(s)
        one = [0] * len(s)
        count_zero, count_one = 0, 0
        for i in range(len(s)):
            if s[i] == '0':
                zero[i] = 1
            else:
                one[i] = 1
        

        for i in range(1, len(s)):
            zero[i] += zero[i-1]
            one[i] += one[i-1]
        
        zero_one = [0] * len(s)
        one_zero = [0] * len(s)
        for i in range(len(s)):
            if s[i] == '0':
                # count_zero += 1
                one_zero[i] += one[i]
            else:
                # count_one += 1
                zero_one[i] += zero[i]
        
        for i in range(1, len(s)):
            zero_one[i] += zero_one[i-1]
            one_zero[i] += one_zero[i-1]
        # print(zero_one)        
        # print(one_zero)   
        zero_one_zero = [0] * len(s)
        one_zero_one = [0] * len(s)
        for i in range(len(s)):
            if s[i] == '0':
                zero_one_zero[i] += zero_one[i]
            else:
                one_zero_one[i] += one_zero[i]
        for i in range(1, len(s)):
            zero_one_zero[i] += zero_one_zero[i-1]
            one_zero_one[i] += one_zero_one[i-1]
        return (zero_one_zero[len(s)-1] + one_zero_one[len(s)-1])

                
            