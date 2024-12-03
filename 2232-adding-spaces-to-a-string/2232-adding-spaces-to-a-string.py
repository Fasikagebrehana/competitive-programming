class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = ""
        idx = 0
        for i in range(len(s)):
            if idx < len(spaces) and i == spaces[idx]:
                # print("dfggtd")
                answer += " "
                idx += 1
            answer += s[i]
        return answer