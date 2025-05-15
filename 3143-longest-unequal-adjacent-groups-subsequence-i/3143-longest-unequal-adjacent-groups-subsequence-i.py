class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        n = len(words)
        answer = []
        for i in range(n):
            curr = groups[i]
            arr = [words[i]]
            for j in range(i+1, n):
                if groups[j] != curr:
                    arr.append(words[j])
                    curr = groups[j]
                else:
                    continue
            if len(answer) < len(arr):
                answer = arr[:]
        # print(answer)
        return answer