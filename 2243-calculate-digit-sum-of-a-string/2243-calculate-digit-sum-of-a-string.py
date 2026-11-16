class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def helper(s):
            answer = ""
            for i in range(0,len(s), k):
                summ = 0
                for j in range(i, min(i + k, len(s))):
                    summ += int(s[j])
                answer += str(summ)
                # print(answer)
            return answer

        while len(s) > k:
            s = helper(s)
            # print(s)
        return s