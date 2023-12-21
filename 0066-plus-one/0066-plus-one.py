class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = int(''.join(map(str, digits)))
        s = int(digit) + 1
        int_ans = str(s)
        ans = []
        for i in range(len(int_ans)):
            ans.append(int(int_ans[i]))
        return ans