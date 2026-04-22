class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # bruteforce
        answer = set()
        for i in range(len(queries)):
            w = queries[i]
            # w= sorted(w)
            for word in dictionary:
                count = 0
                for j in range(len(w)):
                    # word = sorted(words)
                    if word[j] != w[j]:
                        count += 1
                    if count > 2:
                        break
                if count <= 2:
                    answer.add((queries[i], i))
        answer = list(answer)
        answers = sorted(answer, key =lambda x: x[1]) 
        # print(answers)
        result = [ans for ans, idx in answers]
        # print(result)
        return result