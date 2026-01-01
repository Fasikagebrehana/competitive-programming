class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join(map(str, digits))
        num = int(num)
        num += 1
        answer = []
        for ch in str(num):
            answer.append(int(ch))
        return answer