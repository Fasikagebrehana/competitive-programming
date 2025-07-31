class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        store = defaultdict(list)
        answer = [words[0]]
        store[''.join(sorted(words[0]))].append(words[0])

        for i in range(1, len(words)):
            if sorted(words[i-1]) == sorted(words[i]):
                # if store[''.join(sorted(words[i]))]:
                #     continue
                # else:
                #     store[''.join(sorted(words[i]))].append(words[i])
                #     answer.append(words[i])
                continue
            else:
                answer.append(words[i])
            
            

        # print(answer)
        return answer