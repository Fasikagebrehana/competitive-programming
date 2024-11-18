class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        answer = []
        n = len(code)
        if k > 0:
            code[:] = code + code
            # print(code)
            for i in range(len(code)):
                summ = 0
                if i >= n:
                    return answer
                for j in range(i+1, i + k + 1):
                    summ += code[j]
                answer.append(summ)
        elif k < 0:
            code[:] = code + code
            # print(code[n])
            for i in range(n, len(code)):
                summ = 0
                # print(i-1-k)
                for j in range(i-1, i + k - 1, -1):
                    summ += code[j]
                    # print(summ)
                answer.append(summ)
        else:
            answer += [0] * n
        
        return answer
            