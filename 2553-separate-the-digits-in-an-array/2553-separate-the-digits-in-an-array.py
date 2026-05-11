class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            temp = []
            while num > 0:
                rem = num % 10
                temp.append(rem)
                num = num // 10
            answer += temp[::-1]
        return answer