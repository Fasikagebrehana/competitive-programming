class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if words[i] in words[j]:
                    answer.append(words[i])
                    break
        return answer
