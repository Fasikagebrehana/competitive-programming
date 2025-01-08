class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        prefixandsuffix = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                # if j == i:
                #     continue
                
                if words[i] in words[j]:
                    l ,r = words[j].index(words[i]), words[j].rindex(words[i])
                    # print(l, r)
                    if l == 0 and len(words[j][r:]) == len(words[i]) and len(words[i]) == len(words[j]):
                        prefixandsuffix += 1
                    elif l == 0 and l != r and len(words[j][r:]) == len(words[i]):
                        prefixandsuffix += 1
        return prefixandsuffix