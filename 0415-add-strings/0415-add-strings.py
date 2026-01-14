class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        to_int = {str(i): i for i in range(10)}
        to_str = {i: str(i) for i in range(10)}

        if len(num1) < len(num2):
            p = len(num2) - len(num1)
            num1 = ('0' * p) + num1
        elif len(num1) > len(num2):
            p = len(num1) - len(num2)
            num2 = ('0' * p) + num2

        # print(num1, num2)
        result = []
        carry = 0
        for i in range(len(num1)-1, -1, -1):
            summ = to_int[num1[i]] + to_int[num2[i]] + carry
            carry = summ // 10
            result.append(to_str[summ % 10])
        if carry:
            result.append(to_str[carry])
             
        # print(result)

        return ''.join(reversed(result))