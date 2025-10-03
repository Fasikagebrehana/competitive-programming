class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        third = []

        for i in range(len(words)):
            if first == words[i]:
                if (i+2) < len(words) and words[i+1] == second:
                    third.append(words[i+2])
        # print(third)

        return third