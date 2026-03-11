class Solution:
    def bitwiseComplement(self, n: int) -> int:
        num = bin(n)[2:]
        # print(num[1])
        answer = ""
        for i in range(len(num)):
            if num[i] == '1':
                answer += '0'
            else:
                answer += '1'
        # print(answer)
        return int(answer, 2)