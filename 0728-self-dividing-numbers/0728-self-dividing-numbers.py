class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []
        for num in range(left, right + 1):
            if num % 10 == 0:
                continue
            for n in str(num):
                if n == '0' or num % int(n) != 0:
                    break
            else:
                answer.append(num)
        # print(answer)
        return answer